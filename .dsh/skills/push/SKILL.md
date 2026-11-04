---
name: push
description: "NOMAD 笔记仓库的提交约定: 用户说 push / 提交 / commit / 推送时, 按固定格式写 commit 并推送到 GitHub"
user-invocable: true
---

# 提交格式

统一写成

```
[26/10/28 16:38] 中文一句话简要概括
```

- 方括号内是提交时刻, 格式 `yy/M/d H:mm`, 月日时不补零, 分钟补两位
- 时刻由 agent 取本机当前时间填入, 不从用户消息里抄
- 概述压到一句话, 写不下时先空一行, 再补正文, 正文一行一件事
- 不用 `-m` 拼多段 patch note

取时间

```
(Get-Date).ToString('yy/M/d H:mm')
```

# 执行流程

1. 确认范围
   用户说 `push` 时, 只提交用户点名的改动
   没有点名就提交工作区里已有的全部改动
   遇到临时文件, 草稿, 未裁剪的中间图片, 先列出来问, 确认后再决定是否加入
2. 一条命令完成 add 与 commit

```
git add -A; git commit -m "[26/10/28 16:38] 补第 1 章笔记"
```

   需要只提交部分文件时, 把 `-A` 换成具体路径, 仍然一条命令

3. 推送

```
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\publish_site.ps1 -Message "一句话"
```

   有改动时这一步同时完成 add, commit 与 push
   只推已经提交的内容时加 `-NoCommit`

# 注意

- 不做 `git status` / `git diff` 的来回确认, 一次看够再提交
- 不改 `user.name` 与 `user.email`, 不改 remote
- 不使用 `--force`, 不使用 `git reset --hard`
- 提交前确认没有把大文件(教材 PDF, 中间渲染图)带进仓库
  教材 PDF 与 `$env:TEMP\nomad-pdf\` 下的中间文件都不进仓库

# 发布到网站

站点是 GitHub Pages, 地址 https://nomad71214.github.io/nomad/
构建由 `.github/workflows/deploy.yml` 跑 `scripts/build_site.py` 完成
只在 push 到 main 时触发, 本地 commit 不会让网站变化

`dist/` 在 `.gitignore` 里, 是本地预览产物, 不进仓库

## 环境事实

- 本机只有 Windows PowerShell 5.1, 没有 pwsh 7
- 带中文的 `.ps1` 必须存成 UTF-8 BOM, 否则 5.1 按 GBK 解析时报语法错误
- GitHub 直连不稳定, 推送与查 API 都走本地代理 `127.0.0.1:7897`
- 沙箱里 GCM 弹不出登录窗, 推送直接用凭据管理器里的令牌
  target 为 `GitHub - https://api.github.com/nomad71214`, 账号 nomad71214
  取不到令牌时, 让用户在 GitHub Desktop 里登录一次

## 校验发布

推送后等 Actions 跑完再报成功

```
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\publish_site.ps1 -NoCommit
```

线上路径规则: 目录名与文件名去掉方括号与圆括号, 保留括号里的编号
`Coursera/[2]电子/(2)Python程序设计/(6)列表.md` 对应
https://nomad71214.github.io/nomad/2电子/2Python程序设计/6列表.html
抓页面时中文要 percent-encode, 确认正文出现新版独有的小标题或规则编号
