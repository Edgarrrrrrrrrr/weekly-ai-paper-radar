# Setup Notes

这里保留仓库的运行和配置说明，避免影响仓库首页的阅读体验。

## 本地运行

```bash
cp .env.example .env
export OPENAI_API_KEY="你的 OpenAI Key"
export OPENAI_MODEL="gpt-4.1-mini"
make run
```

如果你只是想看输出格式：

```bash
make demo
```

## GitHub Actions 所需配置

必填 Secret：

- `OPENAI_API_KEY`

可选 Variables：

- `OPENAI_MODEL`
- `OPENAI_BASE_URL`
- `OPENAI_API_STYLE`

## 如果你使用 OpenAI 兼容中转

例如：

- `OPENAI_BASE_URL=https://api-vip.codex-for.me/v1`
- `OPENAI_API_STYLE=responses`
- `OPENAI_MODEL=gpt-5.3-codex`

## 自动更新

工作流文件位于 `.github/workflows/weekly-papers.yml`，默认每周一自动运行一次，也支持手动触发。
