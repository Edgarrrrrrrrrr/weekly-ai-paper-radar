from __future__ import annotations

from dataclasses import asdict
from datetime import date
import json
from pathlib import Path
import shutil

from weekly_paper.models import PaperAnalysis, RankedPaper, TopicReport, WeeklyEditorial
from weekly_paper.utils import display_date, slugify, week_folder_name


def write_report_bundle(
    output_root: Path,
    target_date: date,
    editorial: WeeklyEditorial,
    topic_reports: list[TopicReport],
    analyses: dict[str, PaperAnalysis],
) -> Path:
    bundle_dir = output_root / week_folder_name(target_date)
    papers_dir = bundle_dir / "papers"
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    papers_dir.mkdir(parents=True, exist_ok=True)

    unique_papers = collect_unique_ranked_papers(topic_reports)
    detail_paths: dict[str, str] = {}
    manifest_topics: list[dict[str, object]] = []

    for ranked in unique_papers:
        analysis = analyses[ranked.paper.paper_id]
        filename = f"{slugify(ranked.paper.paper_id)}-{slugify(ranked.paper.title)}.md"
        paper_path = papers_dir / filename
        paper_path.write_text(render_paper_detail(ranked, analysis), encoding="utf-8")
        detail_paths[ranked.paper.paper_id] = f"papers/{filename}"

    for report in topic_reports:
        manifest_topics.append(
            {
                "topic_name": report.topic_name,
                "topic_name_zh": report.topic_name_zh,
                "summary": report.summary,
                "trend_signals": report.trend_signals,
                "landmark_papers": [serialize_ranked_paper(item, detail_paths[item.paper.paper_id]) for item in report.landmark_papers],
                "recent_papers": [serialize_ranked_paper(item, detail_paths[item.paper.paper_id]) for item in report.recent_papers],
            }
        )

    manifest: dict[str, object] = {
        "week": week_folder_name(target_date),
        "headline": editorial.headline,
        "overview": editorial.overview,
        "topics": manifest_topics,
        "paper_details": detail_paths,
    }

    readme_path = bundle_dir / "README.md"
    readme_path.write_text(
        render_weekly_index(target_date, editorial, topic_reports, detail_paths),
        encoding="utf-8",
    )

    repo_root = output_root.parent
    repo_readme_path = repo_root / "README.md"
    repo_readme_path.write_text(
        render_repository_readme(repo_root, output_root, target_date, editorial, topic_reports, detail_paths),
        encoding="utf-8",
    )

    manifest_path = bundle_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return bundle_dir


def render_weekly_index(
    target_date: date,
    editorial: WeeklyEditorial,
    topic_reports: list[TopicReport],
    detail_paths: dict[str, str],
) -> str:
    iso_year, iso_week, _ = target_date.isocalendar()
    lines = [
        f"# Weekly Paper Radar | {iso_year} 第 {iso_week:02d} 周",
        "",
        f"> {editorial.headline}",
        "",
        "## 本期总览",
        "",
        editorial.overview,
        "",
        "## 总体趋势",
        "",
    ]
    for item in editorial.trend_signals:
        lines.append(f"- {item}")

    lines.extend(["", "## 继续关注", ""])
    for item in editorial.watchlist:
        lines.append(f"- {item}")

    for report in topic_reports:
        lines.extend(
            [
                "",
                f"## {report.topic_name_zh}",
                "",
                report.summary,
                "",
                "### 长期重要论文",
                "",
            ]
        )
        lines.extend(render_paper_table(report.landmark_papers, detail_paths, include_published=False))
        lines.extend(["", "### 本期关注的新工作", ""])
        lines.extend(render_paper_table(report.recent_papers, detail_paths, include_published=True))
        lines.extend(["", "### 趋势判断", ""])
        for item in report.trend_signals:
            lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- 现在的周报结构按方向组织，不再只看最近一周发了什么。",
            "- 每个方向都会同时保留长期重要论文、近期关注新工作和趋势判断。",
            "- 权威论文 seed 清单可以直接在 `config/pipeline.json` 里维护。",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def render_paper_table(
    papers: list[RankedPaper],
    detail_paths: dict[str, str],
    include_published: bool,
) -> list[str]:
    if include_published:
        lines = [
            "| 排名 | 论文 | 发布时间 | 为什么值得看 | 原文 | 精读 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    else:
        lines = [
            "| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |",
            "| --- | --- | --- | --- | --- |",
        ]

    if not papers:
        lines.append("| - | 暂无强匹配论文 | - | - | - | - |" if include_published else "| - | 暂无已配置论文 | - | - | - |")
        return lines

    for ranked in papers:
        original = f"[Abstract]({ranked.paper.abs_url}) / [PDF]({ranked.paper.pdf_url})"
        detail = f"[阅读精读]({detail_paths[ranked.paper.paper_id]})"
        if include_published:
            lines.append(
                "| "
                f"{ranked.rank} | "
                f"{escape_table(ranked.paper.title)} | "
                f"{escape_table(format_published(ranked.paper))} | "
                f"{escape_table(ranked.selection_reason)} | "
                f"{original} | "
                f"{detail} |"
            )
        else:
            lines.append(
                "| "
                f"{ranked.rank} | "
                f"{escape_table(ranked.paper.title)} | "
                f"{escape_table(ranked.selection_reason)} | "
                f"{original} | "
                f"{detail} |"
            )
    return lines


def render_paper_detail(ranked: RankedPaper, analysis: PaperAnalysis) -> str:
    authors = ", ".join(ranked.paper.authors[:6]) if ranked.paper.authors else "Unknown"
    topics = " / ".join(ranked.paper.matched_topics) if ranked.paper.matched_topics else ranked.direction_fit
    lines = [
        f"# {ranked.paper.title}",
        "",
        f"> 中文标题：{analysis.title_zh}",
        "",
        f"> {analysis.tagline}",
        "",
        "| 字段 | 内容 |",
        "| --- | --- |",
        f"| 方向 | {topics} |",
        f"| 类型 | {paper_kind_label(ranked.paper.collection_kind)} |",
        f"| 来源 | {ranked.paper.source} |",
        f"| 发布时间 | {format_published(ranked.paper)} |",
        f"| 作者 | {authors} |",
        f"| 原文入口 | [Abstract]({ranked.paper.abs_url}) |",
        f"| PDF | [Download PDF]({ranked.paper.pdf_url}) |",
        "",
        "## 为什么值得看",
        "",
        analysis.importance,
        "",
        "## 核心方法 / 关键贡献",
        "",
        analysis.core_innovation,
        "",
        "## 技术要点",
        "",
    ]
    for item in analysis.technical_takeaways:
        lines.append(f"- {item}")

    lines.extend(["", "## 应用价值", ""])
    for item in analysis.applications:
        lines.append(f"- {item}")

    lines.extend(["", "## 风险与局限", ""])
    for item in analysis.limitations:
        lines.append(f"- {item}")

    lines.extend(["", "## 推荐谁读", ""])
    for item in analysis.who_should_read:
        lines.append(f"- {item}")

    lines.extend(["", "## 建议继续追问的问题", ""])
    for item in analysis.follow_ups:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 摘要 / 内容摘记",
            "",
            ranked.paper.abstract,
            "",
            "## 一句话结论",
            "",
            analysis.one_line,
            "",
        ]
    )
    return "\n".join(lines)


def render_repository_readme(
    repo_root: Path,
    reports_root: Path,
    target_date: date,
    editorial: WeeklyEditorial,
    topic_reports: list[TopicReport],
    detail_paths: dict[str, str],
) -> str:
    latest_week = week_folder_name(target_date)
    latest_readme = (reports_root / latest_week / "README.md").relative_to(repo_root).as_posix()
    recent_reports = list_recent_reports(reports_root, repo_root)
    repo_detail_paths = {
        paper_id: f"reports/{latest_week}/{path}"
        for paper_id, path in detail_paths.items()
    }

    lines = [
        "# Weekly Paper Radar",
        "",
        "每周自动更新三个方向的长期重要论文、近期新工作、原文链接和中文精读：Agentic AI、文生图 + Agentic AI、文生视频 + Agentic AI。",
        "",
        f"- 最新周报：[查看 {target_date.isocalendar()[0]} 第 {target_date.isocalendar()[1]:02d} 周]({latest_readme})",
        "- 自动更新：每周一 09:00（北京时间）",
        "- 结构：长期重要论文 + 本期关注 + 趋势判断",
        "",
        f"> {editorial.headline}",
    ]

    for report in topic_reports:
        lines.extend(["", f"## {report.topic_name_zh}", ""])
        lines.append(report.summary)
        lines.extend(["", "### 长期重要论文", ""])
        lines.extend(render_repository_topic_links(report.landmark_papers, repo_detail_paths))
        lines.extend(["", "### 本期关注", ""])
        lines.extend(render_repository_topic_links(report.recent_papers, repo_detail_paths))

    lines.extend(["", "## 历史周报", ""])
    for label, path in recent_reports:
        lines.append(f"- [{label}]({path})")

    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- 仓库首页只展示论文入口和方向导航。",
            "- 运行与配置说明已移到 [docs/SETUP.md](docs/SETUP.md)。",
            "",
        ]
    )
    return "\n".join(lines)


def render_repository_topic_links(
    papers: list[RankedPaper],
    detail_paths: dict[str, str],
) -> list[str]:
    if not papers:
        return ["- 暂无条目"]
    lines: list[str] = []
    for ranked in papers:
        lines.append(
            "- "
            f"[{ranked.paper.title}]({ranked.paper.abs_url})"
            f" | [PDF]({ranked.paper.pdf_url})"
            f" | [精读]({detail_paths[ranked.paper.paper_id]})"
        )
    return lines


def serialize_ranked_paper(ranked: RankedPaper, detail_path: str) -> dict[str, object]:
    return {
        "rank": ranked.rank,
        "importance_score": ranked.importance_score,
        "selection_reason": ranked.selection_reason,
        "direction_fit": ranked.direction_fit,
        "detail_path": detail_path,
        "paper": asdict(ranked.paper),
    }


def collect_unique_ranked_papers(topic_reports: list[TopicReport]) -> list[RankedPaper]:
    by_paper_id: dict[str, RankedPaper] = {}
    for report in topic_reports:
        for ranked in report.landmark_papers + report.recent_papers:
            existing = by_paper_id.get(ranked.paper.paper_id)
            if existing is None:
                by_paper_id[ranked.paper.paper_id] = ranked
                continue
            if existing.paper.collection_kind != "landmark" and ranked.paper.collection_kind == "landmark":
                by_paper_id[ranked.paper.paper_id] = ranked
    return list(by_paper_id.values())


def list_recent_reports(reports_root: Path, repo_root: Path, limit: int = 8) -> list[tuple[str, str]]:
    readmes = sorted(reports_root.glob("*/week-*/README.md"), reverse=True)
    items: list[tuple[str, str]] = []
    for readme in readmes[:limit]:
        year = readme.parent.parent.name
        week = readme.parent.name.replace("week-", "")
        label = f"{year} 第 {week} 周"
        items.append((label, readme.relative_to(repo_root).as_posix()))
    return items


def escape_table(value: str) -> str:
    return value.replace("|", "\\|")


def format_published(paper) -> str:
    return paper.published_label or display_date(paper.published)


def paper_kind_label(kind: str) -> str:
    if kind == "landmark":
        return "长期重要论文"
    return "本期关注"
