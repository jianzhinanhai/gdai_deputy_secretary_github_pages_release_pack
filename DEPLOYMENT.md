# 部署说明

## 1. 解压发布包

将本 ZIP 解压到目标 GitHub 仓库根目录。根目录应直接包含：

```text
index.html
.nojekyll
README.md
.github/workflows/deploy-pages.yml
```

不要把整个发布包文件夹作为子目录上传，否则 GitHub Pages 无法从根路径访问页面。

## 2. 提交到 GitHub

```bash
git status
git add index.html .nojekyll README.md DEPLOYMENT.md CODEX_PROMPT.md MANIFEST.json AUDIT.md scripts/verify_package.py .github/workflows/deploy-pages.yml
git commit -m "Publish GDAI secretary work planning page"
git push origin main
```

## 3. 设置 GitHub Pages

在 GitHub 仓库页面：

1. 进入 `Settings`。
2. 进入 `Pages`。
3. Source 选择 `GitHub Actions`。
4. 等待 Actions 中的 `Deploy GitHub Pages` workflow 成功完成。

## 4. 线上验收

发布完成后检查：

- 首页是否正常打开。
- 手机竖屏是否可读，顶部导航是否可横向滑动。
- 锚点跳转是否正常。
- 搜索框是否可搜索关键词并定位结果。
- 页面是否无 404、无远程资源加载失败。
- 对外转发 URL 后，非登录用户是否可访问。

## 5. 回滚方式

如需回滚，可在 Git 中回退上一个提交：

```bash
git log --oneline
git revert <commit_hash>
git push origin main
```
