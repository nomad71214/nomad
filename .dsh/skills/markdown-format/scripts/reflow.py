# -*- coding: utf-8 -*-
"""按 STYLES.md 的版式规则整理 markdown.

用法
    python reflow.py 文件或目录 [--write]

不加 --write 只打印统计, 不落盘
"""
import io
import os
import re
import sys

FULLWIDTH = {
    '\uff0c': ', ',
    '\u3001': ', ',
    '\uff1b': '; ',
    '\uff1a': ': ',
    '\uff08': '(',
    '\uff09': ')',
    '\uff1f': '?',
    '\uff01': '!',
    '\u201c': '"',
    '\u201d': '"',
    '\u2018': "'",
    '\u2019': "'",
    '\u300a': '"',
    '\u300b': '"',
    '\u2014': ', ',
    '\u2026': '...',
}

SEPARATORS = ('------', '---', '***', '___')
EMOJI = re.compile(
    '[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\u2b50\u2705\u274c\u2757]'
)
CJK = '\u4e00-\u9fff'


def split_blocks(text):
    """返回 (前缀行, 段落列表), 段落内保留内容行, 便于统一处理空行."""
    return None


def collapse(lines):
    out = []
    for line in lines:
        if line.strip() == '':
            if not out or out[-1].strip() == '':
                continue
            out.append('')
        else:
            out.append(line)
    while out and out[-1].strip() == '':
        out.pop()
    return out


def title_of(path):
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r'^\(\d+\)', '', base)
    return base.strip()


def demote(line):
    m = re.match(r'^(#{1,5}) (.*)$', line)
    if not m:
        return line
    return '#' * (len(m.group(1)) + 1) + ' ' + m.group(2)


def anchor(text):
    t = text.replace(' ', '%20').replace('(', '%28').replace(')', '%29')
    t = t.replace('|', '%7C').replace('[', '%5B').replace(']', '%5D')
    return '#' + t


CODE_SPAN = re.compile(r'(`+[^`]*`+)')


def outside_code(line, fn):
    """只对行内代码以外的片段应用 fn."""
    parts = CODE_SPAN.split(line)
    return ''.join(p if CODE_SPAN.fullmatch(p or '') else fn(p) for p in parts)


def strip_bold(text):
    return re.sub(r'\*\*(.+?)\*\*', r'\1', text)


def to_half(text):
    for k, v in FULLWIDTH.items():
        text = text.replace(k, v)
    return text


def split_long(line, limit=60):
    """把长句按逗号断开, 切点落在行内代码之外."""
    if len(line) <= limit:
        return [line]
    stripped = line.strip()
    if stripped.startswith(('|', '#', '-', '!', '>')) or '://' in line:
        return [line]
    segs = []
    rest = line
    while len(rest) > limit:
        cut = -1
        for m in re.finditer(r'[,;] ', rest):
            if m.end() > limit - 2:
                continue
            if inside_code(rest, m.start()):
                continue
            cut = m.end()
        if cut <= 0:
            for m in re.finditer(' ', rest):
                if m.start() >= limit - 2:
                    break
                if not inside_code(rest, m.start()):
                    cut = m.start() + 1
        if cut <= 0:
            break
        segs.append(rest[:cut].rstrip(' ,;'))
        rest = rest[cut:].lstrip()
    if len(rest) > limit and segs:
        return segs + [rest]
    segs.append(rest)
    return segs


def inside_code(line, pos):
    """判断位置 pos 是否落在反引号包裹的代码片段里."""
    count = 0
    for m in CODE_SPAN.finditer(line):
        if m.start() < pos < m.end():
            return True
        count += 1
    return False


def reflow(path, write=False):
    raw = io.open(path, encoding='utf-8').read().replace('\r\n', '\n')
    lines = raw.split('\n')
    done = bool(lines) and lines[0].startswith('# ') and any(
        re.match(r'^\s*- \[.+\]\(#', l) for l in lines[:60]
    )
    stat = {'fullwidth': 0, 'sep': 0, 'quote': 0, 'bold': 0, 'emoji': 0, 'blank': 0}
    out = []
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if stripped in SEPARATORS:
            stat['sep'] += 1
            continue
        if line.startswith('>'):
            stat['quote'] += 1
            body = line[1:]
            if body.startswith(' '):
                body = body[1:]
            line = body
        if '**' in line:
            before = line
            line = outside_code(line, strip_bold)
            stat['bold'] += (before.count('**') - line.count('**')) // 2
        emo = EMOJI.findall(line)
        if emo:
            stat['emoji'] += len(emo)
            line = EMOJI.sub('', line)
        if any(ch in line for ch in FULLWIDTH):
            stat['fullwidth'] += sum(1 for ch in line if ch in FULLWIDTH)
            line = outside_code(line, to_half)
        if not done:
            line = demote(line)
        out.extend(split_long(line))

    # 中文与公式之间的空格
    out = [re.sub('([' + CJK + r'])\$', r'\1 $', l) for l in out]
    out = [re.sub(r'\$([' + CJK + '])', r'$ \1', l) for l in out]

    out = collapse(out)
    while out and out[0].strip() == '':
        out.pop(0)

    # 独行的含等号公式改成 $$
    promoted = 0
    res = []
    in_fence = False
    for line in out:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            res.append(line)
            continue
        if in_fence:
            res.append(line)
            continue
        s = line.strip()
        if (
            s.startswith('$')
            and s.endswith('$')
            and not s.startswith('$$')
            and s.count('$') == 2
            and re.search(r'[=<>]', s)
        ):
            res.append('$$' + s[1:-1] + '$$')
            promoted += 1
        else:
            res.append(line)
    out = res

    # 目录
    heads = []
    in_fence = False
    for line in out:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r'^(#{2,4}) (.+)$', line)
        if m:
            heads.append((len(m.group(1)), m.group(2).strip()))

    seen = {}
    toc = []
    for level, text in heads:
        key = text
        if key in seen:
            seen[key] += 1
            key = '%s-%d' % (text, seen[text])
        else:
            seen[key] = 0
        indent = '  ' * (level - 2)
        toc.append('%s- [%s](%s)' % (indent, text, anchor(key)))

    title = title_of(path)
    if done:
        body = out
    else:
        body = ['# ' + title, ''] + (toc + [''] if toc else []) + out

    final = collapse(body)
    text = '\n'.join(final) + '\n'

    if write:
        io.open(path, 'w', encoding='utf-8', newline='\n').write(text)

    stat['heads'] = len(heads)
    stat['promoted'] = promoted
    return stat


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    targets = []
    for a in args:
        if os.path.isdir(a):
            for dirpath, dirnames, filenames in os.walk(a):
                dirnames[:] = [d for d in dirnames if d not in ('.git', '.obsidian', '.dsh')]
                for fn in filenames:
                    if fn.endswith('.md'):
                        targets.append(os.path.join(dirpath, fn))
        elif a.endswith('.md'):
            targets.append(a)
    targets.sort()
    for p in targets:
        st = reflow(p, write=write)
        rel = os.path.basename(p)
        print(
            '%-46s 全角=%d 分隔线=%d 引用=%d 加粗=%d emoji=%d 公式提升=%d 目录项=%d%s'
            % (
                rel[:46],
                st['fullwidth'],
                st['sep'],
                st['quote'],
                st['bold'],
                st['emoji'],
                st['promoted'],
                st['heads'],
                '' if write else ' (演练)',
            )
        )


if __name__ == '__main__':
    main()
