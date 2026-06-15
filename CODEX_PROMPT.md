# Codex 发布提示词

你现在需要将我提供的 GitHub Pages 发布包发布到目标 GitHub 仓库，使其成为一个可对外转发、可在手机浏览器正常访问的单页网页。

## 任务目标

1. 将发布包内容放到仓库根目录。
2. 使用 `index.html` 作为 GitHub Pages 首页。
3. 保留 `.nojekyll` 和 `.github/workflows/deploy-pages.yml`。
4. 不要重写页面内容，不要加入过程性说明，不要改变页面面向秘书长的最终呈现口径。
5. 提交并推送到 `main` 分支。
6. 确认 GitHub Pages 使用 GitHub Actions 部署。
7. 部署完成后返回线上 URL，并完成桌面和手机视口检查。

## 操作要求

- 如果仓库已有旧版 `index.html`，先确认差异，再用本发布包版本覆盖。
- 不要把发布包文件夹嵌套上传；`index.html` 必须位于仓库根目录。
- 不要删除 `.github/workflows/deploy-pages.yml`。
- 不要引入外部 CDN、远程字体、远程图片或额外构建工具。
- 保持静态站点结构，确保 GitHub Pages 可以直接部署。

## 建议执行步骤

```bash
# 1. 检查仓库状态
git status

# 2. 确认关键文件存在
ls -la
ls -la .github/workflows

# 3. 可选：运行本地校验
python3 scripts/verify_package.py

# 4. 提交发布文件
git add index.html .nojekyll README.md DEPLOYMENT.md CODEX_PROMPT.md MANIFEST.json AUDIT.md scripts/verify_package.py .github/workflows/deploy-pages.yml
git commit -m "Publish GDAI secretary work planning page"
git push origin main
```

## 验收标准

发布后请检查并反馈：

1. GitHub Actions 是否成功。
2. GitHub Pages URL 是什么。
3. 桌面浏览器是否正常显示。
4. 手机竖屏是否正常浏览。
5. 顶部导航、搜索、返回顶部是否可用。
6. 页面是否无 404、无远程资源加载失败。

最终输出：

- 发布结果：Go / No-Go
- 线上 URL
- 检查结果
- 如 No-Go，列出阻塞原因和修复动作
