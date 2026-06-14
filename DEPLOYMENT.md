# GitHub Pages 发布说明

## 1. 发布目标

将 `index.html` 发布为 GitHub Pages 静态站点，用于对外展示《广东省人工智能产业协会副秘书长工作规划与沟通引导》。

## 2. 推荐仓库结构

请将资源包解压到目标 GitHub 仓库根目录，确保根目录存在：

```text
index.html
.nojekyll
.github/workflows/deploy-pages.yml
```

## 3. 使用 GitHub Actions 发布

1. 将本资源包全部文件复制到目标仓库根目录。
2. 提交并推送到 `main` 分支。
3. 打开 GitHub 仓库：Settings → Pages。
4. 将 Build and deployment 的 Source 设置为 `GitHub Actions`。
5. 打开 Actions 页面，确认 `Deploy static HTML to GitHub Pages` workflow 成功运行。
6. 在 Pages 页面获取公开访问 URL。

## 4. 发布后验证

至少完成以下验证：

- 桌面 Chrome/Edge 打开页面正常。
- 手机端 Safari/Chrome 打开页面正常。
- 首页标题区、搜索区、横向导航不遮挡正文。
- 搜索框输入关键词后可高亮命中内容。
- “上一个 / 下一个 / 清除”功能正常。
- 底部“回到顶部”和右下角悬浮回到顶部功能正常。
- 页面正文无“版本、基准、适用、附录、SOP、评分器、项目组合、整改、修订、勾选、checkbox”等不应出现的词。
- 打印或导出 PDF 时，页面结构清晰，无明显遮挡。

## 5. 回滚方式

若上线后发现问题：

1. 回退最近一次提交，或将旧版 `index.html` 覆盖当前文件。
2. 推送到 `main`。
3. 等待 GitHub Actions 重新发布。
4. 重新验证页面。
