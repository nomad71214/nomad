---
name: figures
description: "把笔记插图存进 Annex/assets, 并把 Markdown 里的空占位换成相对路径"
user-invocable: true
---

# 存放规则

- 目录按年月建, 写成 `Annex/assets/<年月>/`, 例如 `Annex/assets/2610/`
- 文件名为拉丁字母与数字, 写成 `fig-<章>-<序号>.png`
  章号与笔记的章号一致, 例如第 1 章第 3 张图为 `fig-1-3.png`
- 不把图片散放在笔记目录里, 不放 `assets` 以外的位置

# 引用规则

- 一律用相对路径, 相对笔记文件所在目录计算
- 从 `Coursera/[3]化学/(2)物理化学/(1)绪论.md` 引用 `Annex/assets/2610/fig-1-1.png`, 写成

```
![图1-1](../../../Annex/assets/2610/fig-1-1.png)
```

- 路径里的 `[ ]` `( )` 与中文保持原样, 不做 URL 编码, GitHub 能正常显示
- 不使用 `http` 开头的地址, 不引用图床
- 需要控制显示宽度时, 在路径后加 `=400x`

```
![图1-1](../../../Annex/assets/2610/fig-1-1.png =400x)
```

  [这依赖 VSCode 扩展 Markdown Image Size, 只在本地预览生效, GitHub 页面按原尺寸显示]

# 常规流程

1. 确认图片来源: 从 PDF 页面图裁出, 还是已有的图片文件
2. 从 PDF 裁图走 `pdf-figure-crop`
3. 落位

```
$dir = "Annex/assets/2610"
New-Item -ItemType Directory -Force $dir
Move-Item "<裁好的图>" "$dir\fig-1-1.png"
```

4. 改占位
   把笔记里的 `![图1-1]()` 换成带相对路径的写法
5. 验证
   Read 一张图确认内容对, 再核一遍路径层数

# 注意

- 补图在整章或整篇笔记写完之后统一做, 不在写作中途插
- 裁图不带教材印刷的图注, 图注信息写进正文
- 同一张图被多篇笔记引用时, 只存一份, 各篇分别写相对路径
- 图片文件名不用中文, 不用空格, 避免在命令行里反复转义
