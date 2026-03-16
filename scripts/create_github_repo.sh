#!/usr/bin/env bash

set -euo pipefail

REPO_NAME="${1:-weekly-ai-paper-radar}"
DESCRIPTION="${2:-Weekly digest for text-to-image, text-to-video, and agentic AI papers.}"
VISIBILITY="${VISIBILITY:-private}"
TOKEN="${GITHUB_TOKEN:-${GH_TOKEN:-}}"

if [[ -z "${TOKEN}" ]]; then
  echo "Missing GitHub token. Export GITHUB_TOKEN or GH_TOKEN first."
  exit 1
fi

if [[ "${VISIBILITY}" != "private" && "${VISIBILITY}" != "public" ]]; then
  echo "VISIBILITY must be either 'private' or 'public'."
  exit 1
fi

get_login() {
  curl -fsSL \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    https://api.github.com/user
}

create_repo() {
  python3 - "$REPO_NAME" "$DESCRIPTION" "$VISIBILITY" <<'PY'
import json
import sys

name, description, visibility = sys.argv[1:4]
payload = {
    "name": name,
    "description": description,
    "private": visibility == "private",
    "has_issues": True,
    "has_projects": False,
    "has_wiki": False,
}
print(json.dumps(payload))
PY
}

OWNER="$(get_login | python3 -c 'import json,sys; print(json.load(sys.stdin)["login"])')"

RESPONSE="$(
  curl -fsSL \
    -X POST \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    https://api.github.com/user/repos \
    -d "$(create_repo)"
)"

CLONE_URL="$(printf '%s' "${RESPONSE}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["clone_url"])')"
SSH_URL="$(printf '%s' "${RESPONSE}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["ssh_url"])')"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "${CLONE_URL}"
else
  git remote add origin "${CLONE_URL}"
fi

echo "Created ${VISIBILITY} repo: ${OWNER}/${REPO_NAME}"
echo "HTTPS remote: ${CLONE_URL}"
echo "SSH remote:   ${SSH_URL}"
