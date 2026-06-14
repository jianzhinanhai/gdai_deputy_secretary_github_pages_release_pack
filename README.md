# 广东省人工智能产业协会副秘书长工作规划与沟通引导

本资源包用于将单页 HTML 发布到 GitHub Pages，形成可对外访问、手机可浏览的静态页面。

## 文件结构

```text
.
├── index.html                         # 正式页面，GitHub Pages 默认入口
├── .nojekyll                          # 禁用 Jekyll 处理，避免静态文件被误处理
├── .github/workflows/deploy-pages.yml # GitHub Actions 自动发布配置
├── CODEX_PROMPT.md                    # 交给 Codex 的执行提示词
├── DEPLOYMENT.md                      # 发布步骤与验证说明
├── AUDIT_CHECKLIST.md                 # 上线前后审计清单
└── MANIFEST.json                      # 资源包清单
```

## 页面要求

- 面向最终使用者：副秘书长。
- 页面正文不包含版本、基准材料、适用场景、过程性讨论、修改建议、操作人说明。
- 不包含勾选功能；调研问卷统一放到飞书多维表格。
- 手机端可浏览；导航不应大面积遮挡正文。
- 搜索支持：上一个、下一个、清除。
- 底部与右下角保留回到顶部功能。

## 推荐发布方式

推荐使用 GitHub Actions 发布 GitHub Pages。将本包文件放入目标仓库根目录，推送到 `main` 分支后，在 GitHub 仓库 Settings → Pages 中将 Source 设置为 GitHub Actions。
