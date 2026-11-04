# Personal Agent 学习笔记

记录学习 Personal Agent（个人智能体）的过程和相关资料，使用 Hugo + Docsy 构建。

- [在线阅读](https://skyao.net/learning-personal-agent/)
- [GitHub 源码](https://github.com/skyao/learning-personal-agent)

## 本地预览

环境沿用 [学习笔记本地搭建指南](https://skyao.net/learning-hugo/docsy/customization/skyao-learning/setup/)：Hugo **0.121.1 Extended**、Go、Node.js/npm。当前模板配套的目录结构如下：

```text
learning/
├── docsy/                    # skyao/docsy-learning 的 learning2024 分支
└── learning-personal-agent/  # 当前仓库
```

`docsy.work` 引用 `../docsy/`。主题准备步骤见上面的环境指南。在当前笔记仓库安装站点的 PostCSS 依赖，再启动预览：

```bash
npm install
npm run serve
```

打开终端输出的本地地址，通常为 `http://localhost:1313/`。这些命令使用系统已安装的 Hugo 0.121.1 Extended，不通过 npm 另行下载 Hugo。正文放在 `content/zh-cn/`，学习笔记入口为 `content/zh-cn/docs/_index.md`。

## 构建

```bash
npm run build:production
```

产物默认输出到 `public/`。`hugo.toml` 的 `baseURL` 沿用模板的 `/`，方便本地预览；生产脚本通过 `--baseURL https://skyao.net/learning-personal-agent/` 设置站点子路径。此命令只生成文件，发布由现有发布流程处理。

## Google 站内搜索

已配置独立搜索引擎，`gcs_engine_id` 为 `60a2e26713b10403f`。可在 [Google Programmable Search Engine](https://cse.google.com/cse/all) 中管理：

- 名称：`learning-personal-agent`
- 搜索范围：`skyao.net/learning-personal-agent/*`

以后更换引擎时，取生成代码中 `cx=` 后的 ID，填入 `hugo.toml` 现有 `gcs_engine_id` 位置，然后重新构建。

## 初始化记录

本仓库按 [创建新笔记指南](https://skyao.net/learning-hugo/docsy/customization/skyao-learning/create-new/) 从 `upstream/learning-clean-2024` 初始化，已完成名称、描述、首页、笔记入口和仓库链接替换。

## 版权申明

本笔记内容可以任意转载，但请注明来源并提供链接。继承自 Docsy 示例的代码许可见 [LICENSE](LICENSE)。

