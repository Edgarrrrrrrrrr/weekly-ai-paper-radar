# Weekly Paper Radar

一个面向 `文生图`、`文生视频`、`Agentic AI` 的私有研究跟踪仓库。

这个仓库会每周自动做 4 件事：

1. 从近期 arXiv 论文里抓取和这三个方向相关的候选论文。
2. 按相关性、潜在影响力、工程价值做筛选。
3. 给每篇入选论文生成单独的精读 Markdown。
4. 产出一份周报首页，集中展示本周重点、论文原文链接和我的分析结论。

当前版本默认以 `arXiv` 为主，代码结构已经留好了，后面要扩展到其他论文收录站也比较直接。

## 目录结构

```text
.
├── .github/workflows/weekly-papers.yml
├── config/pipeline.json
├── scripts/create_github_repo.sh
├── scripts/generate_weekly_report.py
├── src/weekly_paper/
└── tests/
```

生成结果会写到：

```text
reports/<year>/week-<iso-week>/
├── README.md
├── manifest.json
└── papers/
    ├── 01-xxxx.md
    ├── 02-xxxx.md
    └── ...
```

## 先本地跑起来

1. 配置环境变量

```bash
cp .env.example .env
export OPENAI_API_KEY="你的 OpenAI Key"
export OPENAI_MODEL="gpt-4.1-mini"
```

2. 手动生成一次周报

```bash
make run
```

3. 如果你只是想看输出样式，不连外网也可以跑演示数据

```bash
make demo
```

## 建 GitHub Private Repo

这个仓库里已经放了一个辅助脚本，会用 GitHub API 创建私有仓库并自动绑定 `origin`：

```bash
export GITHUB_TOKEN="你的 GitHub Personal Access Token"
bash scripts/create_github_repo.sh weekly-ai-paper-radar
git add .
git commit -m "chore: initialize weekly paper radar"
git push -u origin main
```

Token 需要最少具备创建仓库和写仓库内容的权限。

## 打开每周自动更新

仓库里已经带了 GitHub Actions 工作流：

- 每周一自动运行一次
- 支持 GitHub Actions 页面手动触发
- 有新报告时自动提交到仓库

你只需要在 GitHub 仓库里配置：

- `OPENAI_API_KEY` repo secret
- 可选：`OPENAI_MODEL` repo variable
- 可选：`OPENAI_BASE_URL` repo variable
- 可选：`OPENAI_API_STYLE` repo variable

## 如果你用的是 OpenAI 兼容中转

当前代码同时支持两种风格：

- `chat_completions`
- `responses`

如果你的中转配置像下面这样：

- `base_url = "https://api-vip.codex-for.me/v1"`
- `wire_api = "responses"`

那推荐在 GitHub 仓库里这样配：

```text
Secret:
OPENAI_API_KEY = 你的中转 key

Variables:
OPENAI_BASE_URL = https://api-vip.codex-for.me/v1
OPENAI_API_STYLE = responses
OPENAI_MODEL = gpt-5.3-codex
```

如果你的中转支持别的模型，也可以把 `OPENAI_MODEL` 换成你可用且更省钱的模型。

## 生成内容长什么样

每周首页会包含：

- 本周研究概览
- 重点信号
- Top 论文榜单
- 每篇原文入口：Abstract / PDF
- 每篇独立精读文件链接

每篇独立论文文件会包含：

- 为什么值得看
- 核心方法概括
- 对图像 / 视频 / Agent 方向的关联判断
- 潜在应用价值
- 风险与局限
- 推荐谁读
- 一句话结论

## 后面如果你想继续升级

比较值得加的下一步有：

- 接入 Semantic Scholar / OpenReview / Hugging Face Daily Papers
- 为不同方向拆成单独榜单
- 把产出同步到 Notion 或飞书
- 自动生成中文标题图和更强的排版
