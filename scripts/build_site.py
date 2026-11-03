import os
import re
import shutil
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, '.site')
REPO_NAME = 'nomad'

ROOT_PAGES = ['AGENTS.md', 'README.md', 'STYLES.md']
SKIP_DIRS = {'.git', '.github', '.dsh', '.vitepress', '.site', 'node_modules',
             'Annex', 'Paper', 'Skill', 'scripts'}
SKIP_FILES = {'package.json', 'package-lock.json'}


def safe_seg(seg):
    return seg.replace('[', '').replace(']', '')


def safe_rel(rel):
    parts = rel.split(os.sep)
    return os.sep.join(safe_seg(p) for p in parts)


def collect():
    items = []
    for name in ROOT_PAGES:
        if os.path.isfile(os.path.join(ROOT, name)):
            items.append((name, name))
    base = os.path.join(ROOT, 'Coursera')
    if not os.path.isdir(base):
        return items
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if not fn.lower().endswith('.md'):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            items.append((rel, safe_rel(rel)))
    return items


IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]*)\)')
CODE_RE = re.compile(r'`[^`\n]*`')


def fix_line(line):
    def code_sub(m):
        s = m.group(0)
        if '{{' in s or '}}' in s:
            return '<code v-pre>' + s[1:-1] + '</code>'
        return s
    line = CODE_RE.sub(code_sub, line)
    line = line.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
    return line


def transform(text, src_dir):
    out = []
    fence = False
    for line in text.split('\n'):
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = not fence
            out.append(line)
            continue
        if fence:
            out.append(line)
            continue

        def img_sub(m):
            alt, path = m.group(1), m.group(2)
            if not path:
                return m.group(0)
            target = os.path.normpath(os.path.join(src_dir, path))
            if os.path.isfile(target):
                return m.group(0)
            return '图 (原图未上传): ' + path

        line = IMG_RE.sub(img_sub, line)
        out.append(fix_line(line))
    return '\n'.join(out)


def title_of(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^#\s+(.+?)\s*$', line)
            if m:
                return m.group(1)
    return os.path.splitext(os.path.basename(path))[0]



def pretty(name):
    s = re.sub(r'^\d+', '', name).strip()
    s = re.sub(r'^\(\d+\)', '', s).strip()
    return s or name

def link(rel):
    rel = rel.replace(os.sep, '/')
    if ' ' in rel or '(' in rel or ')' in rel:
        return '<' + rel.replace(' ', '%20') + '>'
    return rel


def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, '.vitepress'))

    items = collect()
    links = []
    for src_rel, dst_rel in items:
        src = os.path.join(ROOT, src_rel)
        dst = os.path.join(SITE, dst_rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, encoding='utf-8') as f:
            text = f.read()
        with open(dst, 'w', encoding='utf-8', newline='\n') as f:
            f.write(transform(text, os.path.dirname(src)))
        label = dst_rel.replace('.md', '')
        links.append((label, title_of(src), dst_rel))

    sidebar = [{'text': '讲义', 'items': [
        {'text': t, 'link': '/' + l.replace('.md', '').replace(os.sep, '/')}
        for _, t, l in links
    ]}]

    cfg = """export default {
  title: 'Nomad',
  description: '课程讲义',
  lang: 'zh-CN',
  srcDir: '.',
  base: '/%s/',
  cleanUrls: true,
  ignoreDeadLinks: true,
  markdown: { math: true },
  themeConfig: {
    nav: [{ text: '首页', link: '/' }],
    sidebar: %s,
    outline: { level: [2, 3], label: '本页目录' },
    search: { provider: 'local' },
    docFooter: { prev: '上一篇', next: '下一篇' },
  },
}
""" % (REPO_NAME, sidebar)

    with open(os.path.join(SITE, '.vitepress', 'config.mts'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(cfg)

    groups = {}
    for _, title, rel in links:
        parts = rel[:-3].split(os.sep)
        if len(parts) >= 4:
            g, sub = parts[1], parts[2]
        elif len(parts) == 3:
            g, sub = parts[1], ''
        else:
            g, sub = '仓库说明', ''
        groups.setdefault(g, {}).setdefault(sub, []).append((title, rel))

    lines = ['# Nomad', '', '本站收录讲义笔记, 以下按学科分组。', '']
    for g in sorted(groups):
        lines += ['## %s' % pretty(g), '']
        for sub in sorted(groups[g]):
            if sub:
                lines += ['### %s' % pretty(sub), '']
            for title, rel in groups[g][sub]:
                lines.append('- [%s](%s)' % (title, link(rel)))
            lines.append('')
    with open(os.path.join(SITE, 'index.md'), 'w', encoding='utf-8',
              newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

    pkg = """{
  "name": "nomad-site",
  "private": true,
  "type": "module",
  "scripts": {
    "docs:build": "vitepress build",
    "docs:dev": "vitepress dev"
  },
  "devDependencies": {
    "markdown-it-mathjax3": "^4.3.2",
    "vitepress": "next"
  }
}
"""
    with open(os.path.join(SITE, 'package.json'), 'w', encoding='utf-8',
              newline='\n') as f:
        f.write(pkg)

    print('pages:', len(links))


if __name__ == '__main__':
    main()
