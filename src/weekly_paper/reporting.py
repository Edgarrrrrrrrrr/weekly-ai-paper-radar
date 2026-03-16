from __future__ import annotations

from dataclasses import asdict
from datetime import date
import json
from pathlib import Path

from weekly_paper.models import PaperAnalysis, RankedPaper, WeeklyEditorial
from weekly_paper.utils import display_date, slugify, week_folder_name


def write_report_bundle(
    output_root: Path,
    target_date: date,
    editorial: WeeklyEditorial,
    ranked_papers: list[RankedPaper],
    analyses: dict[str, PaperAnalysis],
) -> Path:
    bundle_dir = output_root / week_folder_name(target_date)
    papers_dir = bundle_dir / "papers"
    papers_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, object] = {
        "week": week_folder_name(target_date),
        "headline": editorial.headline,
        "papers": [],
    }

    paper_links: list[tuple[RankedPaper, PaperAnalysis, str]] = []
    for ranked in ranked_papers:
        analysis = analyses[ranked.paper.paper_id]
        filename = f"{ranked.rank:02d}-{slugify(ranked.paper.title)}.md"
        paper_path = papers_dir / filename
        paper_path.write_text(render_paper_detail(ranked, analysis), encoding="utf-8")
        paper_links.append((ranked, analysis, f"papers/{filename}"))
        manifest["papers"].append(
            {
                "rank": ranked.rank,
                "paper": asdict(ranked.paper),
                "analysis": asdict(analysis),
                "detail_path": f"papers/{filename}",
            }
        )

    readme_path = bundle_dir / "README.md"
    readme_path.write_text(render_weekly_index(target_date, editorial, paper_links), encoding="utf-8")
    repo_root = output_root.parent
    repo_readme_path = repo_root / "README.md"
    repo_readme_path.write_text(
        render_repository_readme(repo_root, output_root, target_date, editorial, paper_links),
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
    paper_links: list[tuple[RankedPaper, PaperAnalysis, str]],
) -> str:
    iso_year, iso_week, _ = target_date.isocalendar()
    lines = [
        f"# Weekly Paper Radar | {iso_year} 第 {iso_week:02d} 周",
        "",
        f"> {editorial.headline}",
        "",
        "## 本周概览",
        "",
        editorial.overview,
        "",
        "## 重点信号",
        "",
    ]
    for item in editorial.trend_signals:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 建议跟踪",
            "",
        ]
    )
    for item in editorial.watchlist:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 本周重点论文",
            "",
            "| 排名 | 论文 | 方向 | 为什么重要 | 原文 | 精读 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    for ranked, analysis, detail_link in paper_links:
        original = f"[Abstract]({ranked.paper.abs_url}) / [PDF]({ranked.paper.pdf_url})"
        detail = f"[阅读精读]({detail_link})"
        lines.append(
            "| "
            f"{ranked.rank} | "
            f"{escape_table(ranked.paper.title)} | "
            f"{escape_table(ranked.direction_fit)} | "
            f"{escape_table(analysis.one_line)} | "
            f"{original} | "
            f"{detail} |"
        )

    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- 当前版本优先抓取 arXiv。",
            "- 排名结合了关键词过滤和编辑式筛选。",
            "- 目前深度分析主要基于元数据和摘要，如需更强精读可继续扩展全文抓取。",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def render_paper_detail(ranked: RankedPaper, analysis: PaperAnalysis) -> str:
    authors = ", ".join(ranked.paper.authors[:6])
    topics = " / ".join(ranked.paper.matched_topics)
    lines = [
        f"# {ranked.rank}. {ranked.paper.title}",
        "",
        f"> 中文标题：{analysis.title_zh}",
        "",
        f"> {analysis.tagline}",
        "",
        "| 字段 | 内容 |",
        "| --- | --- |",
        f"| 方向 | {topics} |",
        f"| 来源 | {ranked.paper.source} |",
        f"| 发布时间 | {display_date(ranked.paper.published)} |",
        f"| 作者 | {authors} |",
        f"| 原文入口 | [Abstract]({ranked.paper.abs_url}) |",
        f"| PDF | [Download PDF]({ranked.paper.pdf_url}) |",
        "",
        "## 为什么值得看",
        "",
        analysis.importance,
        "",
        "## 核心方法",
        "",
        analysis.core_innovation,
        "",
        "## 技术要点",
        "",
    ]
    for item in analysis.technical_takeaways:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 应用价值",
            "",
        ]
    )
    for item in analysis.applications:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 风险与局限",
            "",
        ]
    )
    for item in analysis.limitations:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 推荐谁读",
            "",
        ]
    )
    for item in analysis.who_should_read:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 建议继续追问的问题",
            "",
        ]
    )
    for item in analysis.follow_ups:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 摘要摘录",
            "",
            f"> {ranked.paper.abstract}",
            "",
            "## 一句话结论",
            "",
            analysis.one_line,
            "",
        ]
    )
    return "\n".join(lines)


def escape_table(value: str) -> str:
    return value.replace("|", "\\|")


def render_repository_readme(
    repo_root: Path,
    reports_root: Path,
    target_date: date,
    editorial: WeeklyEditorial,
    paper_links: list[tuple[RankedPaper, PaperAnalysis, str]],
) -> str:
    latest_week = week_folder_name(target_date)
    latest_readme = (reports_root / latest_week / "README.md").relative_to(repo_root).as_posix()
    recent_reports = list_recent_reports(reports_root, repo_root)

    lines = [
        "# Weekly Paper Radar",
        "",
        "每周自动更新文生图、文生视频、Agentic AI 的重点论文、原文链接和中文精读。",
        "",
        f"- 最新周报：[查看 {target_date.isocalendar()[0]} 第 {target_date.isocalendar()[1]:02d} 周]({latest_readme})",
        "- 自动更新：每周一 09:00（北京时间）",
        "- 覆盖方向：Text-to-Image / Text-to-Video / Agentic AI",
        "",
        f"> {editorial.headline}",
        "",
        "## 本周文章直达",
        "",
        "| 排名 | 论文 | 方向 | 原文 | 精读 |",
        "| --- | --- | --- | --- | --- |",
    ]

    for ranked, _, detail_link in paper_links:
        detail_path = f"{latest_week}/{detail_link}" if not detail_link.startswith(latest_week) else detail_link
        lines.append(
            "| "
            f"{ranked.rank} | "
            f"{escape_table(ranked.paper.title)} | "
            f"{escape_table(ranked.direction_fit)} | "
            f"[Abstract]({ranked.paper.abs_url}) / [PDF]({ranked.paper.pdf_url}) | "
            f"[阅读精读](reports/{detail_path}) |"
        )

    lines.extend(
        [
            "",
            "## 历史周报",
            "",
        ]
    )

    for label, path in recent_reports:
        lines.append(f"- [{label}]({path})")

    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- 仓库首页只保留最新论文入口和周报导航。",
            "- 生成与配置说明已移到 [docs/SETUP.md](docs/SETUP.md)。",
            "",
        ]
    )
    return "\n".join(lines)


def list_recent_reports(reports_root: Path, repo_root: Path, limit: int = 8) -> list[tuple[str, str]]:
    readmes = sorted(reports_root.glob("*/week-*/README.md"), reverse=True)
    items: list[tuple[str, str]] = []
    for readme in readmes[:limit]:
        year = readme.parent.parent.name
        week = readme.parent.name.replace("week-", "")
        label = f"{year} 第 {week} 周"
        items.append((label, readme.relative_to(repo_root).as_posix()))
    return items
