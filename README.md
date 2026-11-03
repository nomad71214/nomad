# 笔记目录

- [NOMAD](#NOMAD)
  - [目录结构](#目录结构)
  - [命名规则](#命名规则)
  - [电子书映射表](#电子书映射表)
  - [技能清单](#技能清单)
  - [开始写第一篇](#开始写第一篇)
  - [同步到 GitHub](#同步到%20GitHub)
  - [网页版](#网页版)
  - [本地预览](#本地预览)

## NOMAD

个人笔记仓库
笔记用 Markdown 写, 按学科组织在 `Coursera/` 下
配套的电子书放在本机固定目录, 两边用同一套编号命名, 便于互相对照

### 目录结构

| 名称             | 内容                                     |
| ---------------- | ---------------------------------------- |
| `.dsh/skills/`   | 技能文件, 见下面的技能清单               |
| `Annex/`         | 杂项: 样式备份, 自己写的工具             |
| `Annex/assets/`  | 笔记插图, 按 `年月` 建子目录, 例如 `2610` |
| `Coursera/`      | 学科笔记                                 |
| `Paper/`         | 论文笔记                                 |
| `Skill/`         | 环境配置备忘录                           |
| `AGENTS.md`      | 仓库级说明: 结构, 技能, 文风, 编码       |
| `STYLES.md`      | 笔记的版式细则                           |

`AGENTS.md` 与 `STYLES.md` 是给 agent 读的
自己写笔记时看 `STYLES.md` 这一份就够

### 命名规则

- 一级目录按学科, 写成 `[N]学科`, `N` 是排序号, 用方括号与学科名隔开
- 二级目录按课程, 写成 `(N)课程名`
- 课程下每章一个文件, 写成 `(N)章节名.md`, 不开子目录
- 论文笔记写成 `年份-论文简称.md`, 放在 `Paper/`
- 环境配置备忘录放在 `Skill/`, 一个主题一个文件
- 编号只用于排序, 不要求连续

目录形态如下

```text
Coursera/
  [0]示例/
    (1)示例课程/
      (0)示例笔记.md
  [1]数学/
    (1)数学分析/
      (1)实数与函数.md
      (2)数列极限.md
Paper/
Skill/
Annex/
  assets/
    2610/
```

### 电子书映射表

电子书统一放在一个根目录下
本仓库不收录电子书文件, 只用目录名与文件名建立对应关系

根目录

```text
D:\电子书
```

[改成自己的路径, 下面的相对路径都相对这个根目录]

| 笔记目录                       | 电子书文件            |
| ------------------------------ | --------------------- |
| `Coursera/[0]示例/(1)示例课程` | `[0]示例/示例教材.pdf` |
|                                |                       |

新增课程时在表里加一行, 目录名与文件名尽量保持一致

### 技能清单

| 技能                | 用途                                    |
| ------------------- | --------------------------------------- |
| `markdown-format`   | 本仓库 markdown 版式标准与自检, 批量改格式 |
| `textbook-to-notes` | 从教材 PDF 写章节笔记, 一次走完四步     |
| `pdf-bookmark`      | 读 PDF 目录, 按章标识批量写入书签       |
| `pdf-page-image`    | 判定 PDF 是否可读, 渲染指定页为图片     |
| `pdf-figure-crop`   | 按坐标从页面图裁出插图                  |
| `figures`           | 把插图存进 `Annex/assets/` 并写相对路径 |
| `push`              | 按固定格式提交, 推送到 GitHub           |
| `debug-skill`       | 用子 agent 试跑 skill, 记录问题并改     |

技能文件都在 `.dsh/skills/<技能名>/SKILL.md`
脚本放在同名目录的 `scripts/` 下, 依赖 `pymupdf` 与 `pillow`

```python
python -m pip install pymupdf pillow
```

### 开始写第一篇

1. 把要用的教材 PDF 放进电子书根目录, 在映射表里登记
2. 建目录 `Coursera/[N]学科/(N)课程名/`
3. 在 DeepSeek Harness 里把工作目录设为 `NOMAD`, 然后说

`读 AGENTS.md 与 STYLES.md, 用 textbook-to-notes 把 <教材文件名> 第 1 章写成笔记`
4. agent 会自己走: 对齐风格, 渲染页面, 读图写作, 问是否补图

harness 会自动读取本目录的 `AGENTS.md`, 也会自动发现 `.dsh/skills/` 下的技能
不需要手动加载

### 同步到 GitHub

仓库已发布

```text
https://github.com/nomad71214/nomad
```

之后每次提交

1. 左侧看改动列表, 确认只勾选了要提交的文件
2. 在左下 `Summary` 里写 `[26/10/28 16:38] 一句话概括`
3. 点 `Commit to main`, 再点 `Push origin`

用 `push` 技能提交时, agent 会按同样的格式写好 commit
只剩点 `Push origin` 这一步

### 网页版

站点地址

```text
https://nomad71214.github.io/nomad/
```

推送 `main` 后由 GitHub Actions 自动构建发布, 一般一两分钟生效
构建状态见仓库的 `Actions` 页

站点由 `scripts/build_site.py` 生成, 不依赖 npm

1. 读 `Coursera/` 下的笔记, 渲染成 HTML 放进 `dist/`
2. 生成首页封面, 分区页, 笔记页与搜索索引 `dist/assets/search.json`
3. `dist/` 整体上传到 Pages

版式在 `site/theme.css`, 交互在 `site/app.js`, 两者都会被复制进 `dist/assets/`
页面用相对路径互链, 所以本地直接打开 `dist/index.html` 也能看

`dist/` 是生成目录, 已写进 `.gitignore`, 不要手动改
每次改动笔记后重跑一次脚本即可, 脚本会先清空 `dist/` 再重建

本地预览

```powershell
pip install markdown-it-py mdit-py-plugins
python scripts/build_site.py
python -m http.server 8899 --directory dist
```

然后打开 `http://127.0.0.1:8899/`
公式与代码高亮从 CDN 取 KaTeX 与 Prism, 预览时需要联网

### 本地预览

- 在 VSCode 里按 `Ctrl+Shift+V` 预览 Markdown
- 图片宽度写法 `=400x` 依赖扩展 `Markdown Image Size`, GitHub 页面不认, 只在本地生效
- 推荐扩展: `Markdown All in One`, `Markdown Image Size`
- 数学公式在 GitHub 页面可以直接显示, 本地预览可装 `Markdown Preview Enhanced`
