# 广东省人工智能产业协会｜秘书长工作规划与沟通引导

本仓库用于通过 GitHub Pages 发布单页 HTML 页面。

## 发布内容

- `index.html`：对外访问页面，适配桌面与手机浏览。
- `.nojekyll`：避免 GitHub Pages 对静态文件做 Jekyll 处理。
- `.github/workflows/deploy-pages.yml`：GitHub Actions 自动部署配置。

## 访问方式

发布成功后，页面通常为：

```text
https://<GitHub用户名>.github.io/<仓库名>/
```

如使用个人或组织主页仓库，访问地址可能为：

```text
https://<GitHub用户名>.github.io/
```

## 页面特性

- 单文件静态页面，无需后端服务。
- 内置顶部导航、关键词搜索、阅读进度条和返回顶部。
- 已包含 `viewport` 设置，支持手机竖屏浏览。
- 无外部图片、字体或远程脚本依赖，便于公开转发。

## 建议

请将 GitHub Pages 设置为 **GitHub Actions** 部署方式。部署完成后，分别使用桌面浏览器和手机浏览器打开线上 URL 检查显示效果。
