# -*- coding: utf-8 -*-
"""把 Inbox 里的内容整理成笔记, 提交并推送.

用法
    python scripts/inbox.py              处理 Inbox 下所有 .md 与 .txt
    python scripts/inbox.py --no-push    只提交本地, 不推送
    python scripts/inbox.py --dry-run    只看会写到哪里, 不落盘

内容开头可以写两行指令, 决定存到哪个目录, 用什么标题

    <!-- folder: Coursera/[1]数学/(1)数学分析 -->
    <!-- title: (13)反常积分 -->

不写就存到 Skill/速记, 标题取正文的第一个一级标题或文件名
"""
import argparse
import datetime
import io
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INBOX = os.path.join(ROOT, 'Inbox')
ARCHIVE = os.path.join(INBOX, '_done')
DEFAULT_FOLDER = 'Skill/速记'
SCRIPTS = os.path.join(ROOT, '.dsh', 'skills', 'markdown-format', 'scripts')
sys.path.insert(0, SCRIPTS)
import reflow as reflow_mod  # noqa: E402

DIRECTIVE = re.compile(r'^<!--\s*([A-Za-z_]+)\s*:\s*(.+?)\s*-->$')
HEADING = re.compile(r'^(#{1,6}) (.+)$')
BAD_CHARS = re.compile(r'[\\/:*?"<>|]')


def parse_directives(text):
    """取出开头的 <!-- key: value --> 指令, 返回 (指令字典, 剩余正文)."""
    meta = {}
    lines = text.replace('\r\n', '\n').split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        m = DIRECTIVE.match(line)
        if not m:
            break
        meta[m.group(1).lower()] = m.group(2).strip()
        i += 1
    return meta, '\n'.join(lines[i:])


def split_title(text, fallback):
    """正文里的第一个一级标题当作笔记标题, 去掉它."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# '):
            return line[2:].strip(), '\n'.join(lines[i + 1:])
    return fallback, text


def normalize_heads(body):
    """把正文里最高一级标题统一压成二级, 其余顺次下移."""
    lines = body.split('\n')
    levels = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if m:
            levels.append(len(m.group(1)))
    if not levels:
        return body
    shift = 2 - min(levels)
    if shift == 0:
        return body
    out = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = HEADING.match(line)
        if m:
            level = max(2, min(6, len(m.group(1)) + shift))
            out.append('#' * level + ' ' + m.group(2))
        else:
            out.append(line)
    return '\n'.join(out)


def build_toc(body):
    """按二级到四级标题生成目录, 锚点规则与站点一致."""
    toc = []
    seen = {}
    in_fence = False
    for line in body.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r'^(#{2,4}) (.+)$', line)
        if not m:
            continue
        text = m.group(2).strip()
        key = text
        if key in seen:
            seen[key] += 1
            key = '%s-%d' % (text, seen[key])
        else:
            seen[key] = 0
        indent = '  ' * (len(m.group(1)) - 2)
        toc.append('%s- [%s](%s)' % (indent, text, reflow_mod.anchor(key)))
    return toc


def target_path(folder, title):
    folder = folder.replace('\\', '/').strip('/')
    if folder.startswith('['):
        folder = 'Coursera/' + folder
    name = BAD_CHARS.sub('-', title).strip() or '未命名'
    return os.path.join(ROOT, *folder.split('/')) , name


def reflow_file(path, title):
    """用仓库自带的整理脚本跑一遍, 临时文件名取干净标题, 免得一级标题带上编号."""
    tmp_dir = os.path.dirname(path)
    tmp = os.path.join(tmp_dir, '__inbox_tmp.md')
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(
        io.open(path, encoding='utf-8').read()
    )
    reflow_mod.reflow(tmp, write=True)
    text = io.open(tmp, encoding='utf-8').read()
    first, _, rest = text.partition('\n')
    if first.startswith('# ') and first[2:].strip() != title:
        text = '# ' + title + '\n' + rest
    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
    os.remove(tmp)


def check_style(path):
    proc = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, 'check_style.py'), path],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    out = (proc.stdout or '') + (proc.stderr or '')
    bad = [l.strip() for l in out.split('\n') if 'FAIL' in l]
    return bad


def looks_like_item(name):
    if not name.lower().endswith(('.md', '.txt')):
        return False
    if name.startswith('_'):
        return False
    if name.lower() in ('readme.md', 'readme.txt'):
        return False
    return True


def process_one(path, dry_run=False):
    raw = io.open(path, encoding='utf-8', errors='replace').read()
    meta, body = parse_directives(raw)
    fallback = os.path.splitext(os.path.basename(path))[0]
    title, body = split_title(body, meta.get('title') or fallback)
    title = meta.get('title') or title
    body = normalize_heads(body.strip('\n'))
    toc = build_toc(body)
    text = '# ' + title + '\n\n'
    if toc:
        text += '\n'.join(toc) + '\n\n'
    text += body.strip('\n') + '\n'

    folder, name = target_path(meta.get('folder', DEFAULT_FOLDER), title)
    dest = os.path.join(folder, name + '.md')
    print('  标题 %s' % title)
    print('  写入 %s' % os.path.relpath(dest, ROOT))
    if dry_run:
        return None

    if not os.path.isdir(folder):
        os.makedirs(folder)
    if os.path.exists(dest):
        stamp = datetime.datetime.now().strftime('%H%M%S')
        dest = os.path.join(folder, '%s %s.md' % (name, stamp))
        print('  已有同名文件, 改存 %s' % os.path.relpath(dest, ROOT))
    io.open(dest, 'w', encoding='utf-8', newline='\n').write(text)
    reflow_file(dest, title)

    for problem in check_style(dest):
        print('  [格式] ' + problem)
    return dest


def git(*args):
    return subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace')


def commit_and_push(written, push=True):
    git('add', '-A')
    now = datetime.datetime.now()
    stamp = '%d/%d/%d %d:%02d' % (now.year % 100, now.month, now.day, now.hour, now.minute)
    names = ' '.join(os.path.splitext(os.path.basename(p))[0] for p in written)
    if len(names) > 40:
        names = names[:40] + '...'
    msg = '[%s] 新增 %s' % (stamp, names)
    r = git('-c', 'user.name=nomad71214', '-c', 'user.email=1767546165@qq.com',
            'commit', '-m', msg)
    if r.returncode != 0:
        print('  提交跳过: ' + (r.stdout + r.stderr).strip().split('\n')[-1])
        return
    print('  已提交: ' + msg)
    if not push:
        print('  未推送, 在 GitHub Desktop 点 Push origin 即可')
        return
    r = git('push', 'origin', 'main')
    if r.returncode == 0:
        print('  已推送, 一两分钟后站点自动更新')
    else:
        print('  推送失败, 打开 GitHub Desktop 点 Push origin 即可')
        print('  ' + (r.stderr or r.stdout).strip().split('\n')[-1])


def archive(path):
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    folder = os.path.join(ARCHIVE, day)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    shutil.move(path, os.path.join(folder, os.path.basename(path)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-push', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.isdir(INBOX):
        os.makedirs(INBOX)
    items = sorted(
        os.path.join(INBOX, n) for n in os.listdir(INBOX)
        if looks_like_item(n) and os.path.isfile(os.path.join(INBOX, n))
    )
    if not items:
        print('Inbox 里没有待处理的内容')
        print('把 AI 的回答另存为 .md 放进 %s, 或者在这个对话里直接说' % INBOX)
        if not args.dry_run:
            os.startfile(INBOX)
        return

    written = []
    for path in items:
        print('处理 %s' % os.path.basename(path))
        dest = process_one(path, dry_run=args.dry_run)
        if dest:
            written.append(dest)
            archive(path)

    if args.dry_run or not written:
        print('演练结束, 没有落盘')
        return
    commit_and_push(written, push=not args.no_push)


if __name__ == '__main__':
    main()