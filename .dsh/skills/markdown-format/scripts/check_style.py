# -*- coding: utf-8 -*-
"""按 STYLES.md 检查 markdown 版式.

用法
    python check_style.py 文件或目录
"""
import io
import os
import re
import sys

FULLWIDTH = '，、；：（）？！“”‘’《》—…'
SEPARATORS = ('------', '---', '***', '___')
CJK = '\u4e00-\u9fff'


def check(path):
    raw = io.open(path, encoding='utf-8').read().replace('\r\n', '\n')
    lines = raw.split('\n')
    off = 0
    if lines and lines[0].strip() == '---':
        for j in range(1, len(lines)):
            if lines[j].strip() == '---':
                off = j + 1
                lines = lines[off:]
                while lines and lines[0].strip() == '':
                    lines = lines[1:]
                    off += 1
                break
    problems = []

    def add(name, detail):
        problems.append((name, detail))

    if lines and lines[0].strip() != '' and not lines[0].startswith('# '):
        add('标题', '首行不是一级标题')

    lead = 0
    for line in lines:
        if line.strip() == '':
            lead += 1
        else:
            break
    if lead:
        add('开头空行', '%d 行' % lead)

    prev_blank = False
    for idx, line in enumerate(lines, 1):
        blank = line.strip() == ''
        if blank and prev_blank:
            add('连续空行', '第 %d 行' % (idx + off))
        prev_blank = blank

    in_fence = False
    fence_no_lang = 0
    h1 = 0
    levels = []
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```'):
            if not in_fence and len(stripped) <= 3:
                fence_no_lang += 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped in SEPARATORS:
            add('分隔线', '第 %d 行' % (idx + off))
        if line.startswith('>'):
            add('引用块', '第 %d 行' % (idx + off))
        bad = [ch for ch in line if ch in FULLWIDTH]
        if bad:
            add('全角标点', '第 %d 行 %s' % (idx + off, ''.join(sorted(set(bad)))))
        plain = re.sub(r'(`+[^`]*`+)', '', line)
        if '**' in plain:
            add('加粗', '第 %d 行' % (idx + off))
        if re.search('([' + CJK + r'])\$|\$([' + CJK + '])', line):
            add('中文与公式缺空格', '第 %d 行' % (idx + off))
        if stripped.startswith('#') and re.match(r'^#{1,6} ', stripped):
            n = len(stripped) - len(stripped.lstrip('#'))
            levels.append(n)
            if n == 1:
                h1 += 1
        if not stripped.startswith('|') and len(plain) > 60:
            if '://' in line:
                continue
            if not stripped.startswith('#') and '$' not in line and '](' not in line:
                add('超过 60 字符', '第 %d 行 长度 %d' % (idx + off, len(plain)))
    if fence_no_lang:
        add('代码围栏缺语言', '%d 处' % fence_no_lang)
    if h1 != 1:
        add('一级标题数', '%d 个' % h1)
    for a, b in zip(levels, levels[1:]):
        if b - a > 1:
            add('标题跳级', '%d 跳到 %d' % (a, b))

    text = '\n'.join(lines)
    heads = re.findall(r'^(#{2,4}) (.+)$', text, re.M)
    toc = re.findall(r'^\s*- \[(.+?)\]\(#', text, re.M)
    if heads:
        want = [h[1].strip() for h in heads]
        if toc != want:
            add('目录不匹配', '正文 %d 项, 目录 %d 项' % (len(want), len(toc)))

    figs = re.findall(r'!\[图(\d+)-(\d+)\]\(\)', text)
    if figs:
        nums = [int(f[1]) for f in figs]
        if nums != list(range(1, len(nums) + 1)):
            add('图号不连续', str(nums))

    if problems:
        print('===== %s' % os.path.basename(path))
        for name, detail in problems:
            print('  FAIL %-16s %s' % (name, detail))
    return problems


def main():
    args = sys.argv[1:]
    targets = []
    for a in args:
        if os.path.isdir(a):
            for dirpath, dirnames, filenames in os.walk(a):
                dirnames[:] = [d for d in dirnames if d not in ('.git', '.obsidian')]
                for fn in filenames:
                    if fn.endswith('.md'):
                        targets.append(os.path.join(dirpath, fn))
        elif a.endswith('.md'):
            targets.append(a)
    targets.sort()
    bad = 0
    for p in targets:
        if check(p):
            bad += 1
    print('检查 %d 篇, 有问题 %d 篇' % (len(targets), bad))


if __name__ == '__main__':
    main()
