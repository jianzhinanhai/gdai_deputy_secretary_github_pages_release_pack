#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
index = root / "index.html"
workflow = root / ".github" / "workflows" / "deploy-pages.yml"
required = [index, root/".nojekyll", root/"README.md", root/"DEPLOYMENT.md", root/"CODEX_PROMPT.md", workflow]

errors = []
for p in required:
    if not p.exists():
        errors.append(f"Missing required file: {p.relative_to(root)}")

if index.exists():
    html = index.read_text(encoding="utf-8", errors="replace")
    checks = {
        "doctype": "<!doctype html" in html.lower(),
        "lang_zh_cn": 'lang="zh-CN"' in html or "lang='zh-CN'" in html,
        "viewport": "viewport" in html and "width=device-width" in html,
        "title": "<title>" in html.lower(),
        "top_nav": "页面导航" in html or "nav" in html.lower(),
        "search": "searchInput" in html,
        "backtop": "backtop" in html,
        "mobile_css": "@media (max-width:760px)" in html,
    }
    for name, ok in checks.items():
        if not ok:
            errors.append(f"HTML check failed: {name}")
    remote_refs = re.findall(r'(?:src|href)=["\'](https?://[^"\']+)["\']', html, flags=re.I)
    if remote_refs:
        errors.append("Remote resource references found: " + ", ".join(remote_refs[:5]))
    local_abs = re.findall(r'(?:src|href)=["\'](?:file:|/[A-Za-z]:|/mnt/)[^"\']+["\']', html, flags=re.I)
    if local_abs:
        errors.append("Local absolute references found: " + ", ".join(local_abs[:5]))

if workflow.exists():
    yml = workflow.read_text(encoding="utf-8", errors="replace")
    if "actions/deploy-pages" not in yml or "actions/upload-pages-artifact" not in yml:
        errors.append("Workflow does not appear to use GitHub Pages deployment actions.")

if errors:
    print("NO-GO")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("GO")
print("Static GitHub Pages package checks passed.")
