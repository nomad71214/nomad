# NOMAD 笔记仓库说明

- [NOMAD](#NOMAD)
- [仓库结构](#仓库结构)
- [Skill](#Skill)
- [文风](#文风)
  - [用词](#用词)
    - [高危用词](#高危用词)
  - [文件形态](#文件形态)
- [校验](#校验)
- [系统编码](#系统编码)

## NOMAD

个人笔记仓库
本文件是仓库级说明, DeepSeek Harness 与其他 agent 打开本目录时会先读它
文件形态与版式的细则在 `STYLES.md`

## 仓库结构

笔记按学科组织在 `Coursera/` 下
笔记目录与配套电子书的对应关系见 `README.md`
杂项与插图放 `Annex/`, 论文笔记放 `Paper/`, 环境配置备忘录放 `Skill/`

## Skill

本仓库的 skill 放在 `.dsh/skills/` 下, Harness 会自动发现这个目录
新增 skill 时, frontmatter 默认写 `user-invocable: false`
不需要用户直接点名调用的流程写成 skill, 由主 agent 读它执行

写入任何 Markdown 之前先读 `STYLES.md` 与 `.dsh/skills/markdown-format/SKILL.md`
写完用 `.dsh/skills/markdown-format/scripts/check_style.py` 自检, 有问题必须修到 0

从教材 PDF 做笔记走 `textbook-to-notes`, 分对齐风格, 渲染, 写作, 补图四步
笔记的版式细则在仓库根 `STYLES.md`

调试 skill 走 `debug-skill`, 分起子 agent 试跑, 记录问题, 改 skill, 复查四步

skill 里的脚本路径一律相对仓库根写, 例如

```bash
python .dsh/skills/pdf-page-image/scripts/render.py info "<pdf>"
```

## 文风

### 用词

适用于写入本仓库的文件, 也适用于对话回复

- 用平实的说明文, 接近产品说明书的写法
- 陈述事实与操作, 以可读性和准确性为准
- 不用夸张, 煽动, 摆谱的措辞
- 不用口语化说法
- 不拟人, 不调侃, 不评价读者, 不表演共情
- 补充解释之前不写俏皮话
- 动词选最普通的: 由...组成, 演示, 决定, 换成, 生成

#### 高危用词

下面这些词 AI 味重, 读起来别扭, 写作时不要用这样的语气

| 类别     | 词                       | 问题                       |
| -------- | ------------------------ | -------------------------- |
| 动宾连写 | 管用词, 管样式           | 动词与宾语连写, 会产生歧义 |
| 比喻动作 | 憋到, 攒到, 攒够         | 把普通动作说成比喻         |
| 拟人动作 | 跟着走, 自己判断, 自己挑 | 把无生命对象写成人         |
| 缩略动宾 | 落盘, 存档               | 行业口语缩略               |
| 程度修饰 | 不堆, 堆长段             | 口语化程度词               |
| 口语依赖 | 靠, 靠...实现            | 用口语动词代替具体手段     |
| 口语代指 | 长什么样, 长啥样         | 用口语疑问代替名词         |

改法: 换成动词加宾语的完整说法

1. 管用词 -> 用词按...定
2. 憋到最后 -> 等到最后再...
3. 跟着走 -> 与...一致
4. 自己判断 -> 自行判断, 或写明由谁决定
5. 落盘 -> 写入
6. 不堆长段 -> 不合并成长段
7. 靠...实现 -> 用...实现, 或由...决定
8. 文件长什么样 -> 文件的结构, 版式

### 文件形态

笔记与仓库内 Markdown 文件的结构, 标点, 公式, 插图写法见 `STYLES.md`
本文件的「文风」一节只规定用词与语气, 文件的结构与版式一律按 `STYLES.md`

## 校验

- 写完尽量自己 Read 通读一遍验收, 不要写一堆 Python 校验脚本
- 脚本尽量只用在真正机械的操作上, 例如批量插入空行

## 系统编码

本机代码页为 936 (GBK) 时, Python 的 stdout 默认编码是 gbk, 命令行输出中文会乱码
临时规避: 运行前设 `$env:PYTHONIOENCODING="utf-8"`
彻底改为 UTF-8 需写以下三个注册表值

[需要管理员权限, 且必须重启后生效]

```powershell
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name ACP   -Value 65001
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name OEMCP -Value 65001
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Nls\CodePage' -Name MACCP -Value 65001
```

重启后用
`python -I -c "import sys; print(sys.stdout.encoding)"`
验证, 输出 utf-8 即生效
