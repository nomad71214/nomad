"""生成 NOMAD 笔记站点。

用法:
    python scripts/build_site.py

输出到仓库根目录的 dist/。
不依赖 npm, 只依赖 markdown-it-py 与 mdit-py-plugins。
"""

import html
import io
import json
import os
import re
import shutil
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
SITE_SRC = ROOT / 'site'
COURSERA = ROOT / 'Coursera'

DOCS = [
    ('README.md', '笔记目录', '仓库说明'),
    ('AGENTS.md', '仓库约定', '仓库说明'),
    ('STYLES.md', '格式约定', '仓库说明'),
]

NOTE_ROOTS = [
    ('Skill', '备忘录', '写给自己和 agent 的备忘', 'note'),
    ('Paper', '论文', '论文精读与推导', 'file'),
]

SUBJECT_DESC = {
    '数学': '分析、代数与证明的手稿',
    '电子': '从电路到 C 与 Python',
    '示例': '笔记格式的样板',
}

SUBJECT_ICON = {
    '数学': 'sigma',
    '电子': 'cpu',
    '示例': 'file',
}

ICONS = {
    'grid': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    'sigma': '<path d="M18 5H7l6 7-6 7h11"/>',
    'cpu': '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="10" y="10" width="4" height="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M6.5 2v2M17.5 2v2M6.5 20v2M17.5 20v2M2 6.5h2M2 17.5h2M20 6.5h2M20 17.5h2"/>',
    'file': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    'arrow': '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>',
    'moon': '<path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8z"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'note': '<path d="M4 20h4l10-10a2.8 2.8 0 0 0-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
}


def icon(name, cls='ic'):
    body = ICONS.get(name, '')
    return (
        '<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true">%s</svg>' % (cls, body)
    )


def order_key(name):
    m = re.match(r'^[\[(](\d+)[\])]', name)
    return (0, int(m.group(1))) if m else (1, name)


def pretty(name):
    n = re.sub(r'^\[\d+\]', '', name)
    n = re.sub(r'^\(\d+\)', '', n)
    n = re.sub(r'^\d+\s*', '', n)
    return n.strip() or name


def fs_name(name):
    return re.sub(r'[\[\]()]', '', name).strip()


def esc(s):
    return html.escape(s, quote=True)


class Note:
    def __init__(self, path, subject, course):
        self.path = path
        self.subject = subject
        self.course = course
        self.name = pretty(path.stem)
        self.rel = path.relative_to(ROOT)
        parts = [fs_name(p) for p in self.rel.parts[:-1]]
        if parts and parts[0] == 'Coursera':
            parts = parts[1:]
        self.url = '/'.join(parts + [fs_name(self.rel.stem)]) + '.html'
        self.depth = len(Path(self.url).parts) - 1
        self.title = self.name
        self.first = ''
        self.hours = []


def collect():
    matcher = MarkdownIt('commonmark')
    subjects = []
    if not COURSERA.exists():
        return subjects
    for sdir in sorted([d for d in COURSERA.iterdir() if d.is_dir()], key=lambda p: order_key(p.name)):
        courses = []
        for cdir in sorted([d for d in sdir.iterdir() if d.is_dir()], key=lambda p: order_key(p.name)):
            notes = []
            for f in sorted(cdir.glob('*.md'), key=lambda p: order_key(p.name)):
                n = Note(f, pretty(sdir.name), pretty(cdir.name))
                text = f.read_text(encoding='utf-8')
                for line in text.splitlines():
                    if line.startswith('# '):
                        n.title = line[2:].strip()
                        break
                notes.append(n)
            if notes:
                courses.append({'name': pretty(cdir.name), 'dir': cdir.name, 'notes': notes})
        if courses:
            subjects.append({
                'name': pretty(sdir.name),
                'dir': sdir.name,
                'courses': courses,
                'count': sum(len(c['notes']) for c in courses),
                'url': fs_name(sdir.name) + '/index.html',
                'desc': SUBJECT_DESC.get(pretty(sdir.name), '%d 门课程' % len(courses)),
                'icon': SUBJECT_ICON.get(pretty(sdir.name), 'file'),
            })
    for dirname, label, desc, ic in NOTE_ROOTS:
        root = ROOT / dirname
        if not root.exists():
            continue
        groups = {}
        for f in sorted(root.rglob('*.md')):
            rel = f.relative_to(root)
            if any(part.startswith(('.', '_')) for part in rel.parts):
                continue
            parent = rel.parent.as_posix()
            course = label if parent == '.' else parent.split('/')[-1]
            groups.setdefault(course, []).append(f)
        courses = []
        for course, files in groups.items():
            notes = []
            for f in files:
                n = Note(f, label, course)
                text = f.read_text(encoding='utf-8')
                for line in text.splitlines():
                    if line.startswith('# '):
                        n.title = line[2:].strip()
                        break
                notes.append(n)
            courses.append({'name': course, 'dir': course, 'notes': notes})
        if courses:
            subjects.append({
                'name': label,
                'dir': dirname,
                'courses': courses,
                'count': sum(len(c['notes']) for c in courses),
                'url': fs_name(dirname) + '/index.html',
                'desc': desc,
                'icon': ic,
            })
    return subjects


def math_render(content, opts):
    if opts.get('display_mode'):
        return '\\[%s\\]' % content
    return '\\(%s\\)' % content


def asset_url(src, env):
    """把笔记里的相对图片路径改成站点里的相对路径。"""
    if not env:
        return src
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', src) or src.startswith('/') or src.startswith('#'):
        return src
    base = env.get('src_dir')
    if base is None:
        return src
    target = (Path(base) / src).resolve()
    try:
        rel = target.relative_to(ROOT.resolve())
    except ValueError:
        return src
    return env.get('u', '') + rel.as_posix()


def make_md():
    md = MarkdownIt('commonmark', {'html': False, 'linkify': False, 'typographer': False})
    md.enable(['table', 'strikethrough'])
    md.use(dollarmath_plugin, allow_space=False, renderer=math_render)

    default_fence = md.renderer.rules.get('fence')

    def fence(tokens, idx, options, env):
        token = tokens[idx]
        info = (token.info or '').strip().split()[0] if token.info else ''
        if info == 'text':
            info = ''
        lang = ' class="language-%s"' % esc(info) if info else ''
        body = esc(token.content)
        return '<pre class="code"><code%s>%s</code></pre>\n' % (lang, body)

    md.renderer.rules['fence'] = fence

    def image(tokens, idx, options, env):
        token = tokens[idx]
        alt = token.content or ''
        src = token.attrGet('src') or ''
        if not src.strip():
            return '<span class="figure-ph">%s · 待补</span>' % esc(alt)
        src = asset_url(src, env)
        return '<img src="%s" alt="%s" loading="lazy">' % (esc(src), esc(alt))

    md.renderer.rules['image'] = image

    def code_inline(tokens, idx, options, env):
        return '<code>%s</code>' % esc(tokens[idx].content)

    md.renderer.rules['code_inline'] = code_inline
    return md


def heading_ids(body, used=None):
    used = used if used is not None else {}

    def repl(m):
        level, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner)
        text = html.unescape(text).strip()
        key = text
        if key in used:
            used[key] += 1
            key = '%s %d' % (text, used[key])
        else:
            used[text] = 1
        return '<h%s id="%s">%s</h%s>' % (level, esc(key), inner, level)

    return re.sub(r'<h([1-6])>(.*?)</h\1>', repl, body, flags=re.S)


def plain_text(path):
    text = path.read_text(encoding='utf-8')
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('- [') or s.startswith('|'):
            continue
        if s.startswith('```'):
            continue
        s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
        s = re.sub(r'`([^`]*)`', r'\1', s)
        s = re.sub(r'\$[^$]*\$', '', s)
        out.append(s)
        if sum(len(x) for x in out) > 160:
            break
    return ' '.join(out)[:150]


def up(depth):
    return '../' * depth


def page(title, depth, active, crumbs, content, extra_class=''):
    u = up(depth)
    nav = sidebar(depth, active)
    return TEMPLATE.format(
        title=esc(title),
        u=u,
        nav=nav,
        crumbs=crumbs,
        content=content,
        body_class=extra_class,
        brand_icon=icon('grid'),
        search_icon=icon('search'),
        moon=icon('moon', 'ic ic-moon'),
        sun=icon('sun', 'ic ic-sun'),
        menu=icon('menu'),
    )


def sidebar(depth, active):
    u = up(depth)
    items = []
    items.append(
        '<a class="tree-item%s" href="%sindex.html">%s<span class="tree-name">总览</span><span class="tree-count">%d</span></a>'
        % (' is-active' if active == 'home' else '', u, icon('grid'), TOTAL)
    )
    for s in SUBJECTS:
        items.append(
            '<a class="tree-item%s" href="%s%s">%s<span class="tree-name">%s</span><span class="tree-count">%d</span></a>'
            % (' is-active' if active == s['name'] else '', u, s['url'], icon(s['icon']), esc(s['name']), s['count'])
        )
    docs = []
    for f, label, _ in DOCS:
        docs.append('<a class="foot-link" href="%s%s.html">%s</a>' % (u, f[:-3], esc(label)))
    return SIDEBAR.format(
        u=u,
        items='\n'.join(items),
        docs=' · '.join(docs),
        search_icon=icon('search'),
        brand_icon=icon('grid'),
    )


def build_index():
    cards = []
    for i, s in enumerate(SUBJECTS, 1):
        cards.append(CARD.format(
            u='',
            url=s['url'],
            num='%02d' % i,
            icon=icon(s['icon'], 'card-icon'),
            name=esc(s['name']),
            desc=esc(s['desc']),
            count=s['count'],
        ))
    content = '''
<section class="hero">
  <p class="kicker">NOMAD · KNOWLEDGE GARDEN</p>
  <h1 class="hero-title">NOMAD 的知识库</h1>
  <p class="hero-sub">把学过的内容, 整理成可以回来的地方。</p>
  <p class="hero-meta">%d 篇笔记 · %d 个分区 · 持续整理</p>
</section>
<div class="section-head"><h2>知识分区</h2><span>从文件夹开始阅读</span></div>
<div class="cards">%s</div>
<div class="section-head"><h2>仓库说明</h2><span>写给人和 agent 的约定</span></div>
<div class="cards cards-doc">%s</div>
''' % (TOTAL, len(SUBJECTS), '\n'.join(cards), doc_cards(0))
    write('index.html', page('NOMAD 的知识库', 0, 'home', crumb(0, '知识库', '总览'), content))


def doc_cards(depth):
    u = up(depth)
    out = []
    for f, label, group in DOCS:
        out.append(
            '<a class="doc-card" href="%s%s.html"><span class="doc-name">%s</span>'
            '<span class="doc-file">%s</span></a>' % (u, f[:-3], esc(label), esc(f))
        )
    return '\n'.join(out)


def build_subject(s):
    u = up(1)
    blocks = []
    for c in s['courses']:
        rows = []
        for i, n in enumerate(c['notes'], 1):
            rows.append(
                '<a class="note-row" href="%s%s">'
                '<span class="note-num">%02d</span>'
                '<span class="note-name">%s</span>'
                '<span class="note-arrow">%s</span></a>'
                % (u, n.url, i, esc(n.title), icon('arrow'))
            )
        blocks.append(
            '<section class="course"><h2 class="course-title">%s<span>%d 篇</span></h2>'
            '<div class="note-list">%s</div></section>'
            % (esc(c['name']), len(c['notes']), '\n'.join(rows))
        )
    content = '''
<section class="hero hero-subject">
  <p class="kicker">SUBJECT · %s</p>
  <h1 class="hero-title">%s</h1>
  <p class="hero-sub">%s</p>
  <p class="hero-meta">%d 门课程 · %d 篇笔记</p>
</section>
%s
''' % (esc(s['name']), esc(s['name']), esc(s['desc']), len(s['courses']), s['count'], '\n'.join(blocks))
    write(s['url'], page(s['name'], 1, s['name'], crumb(1, '知识库', s['name']), content))


def crumb(depth, left, right):
    return '<a href="%sindex.html">%s</a>' % (up(depth), esc(left)) + \
        ' <span class="sep">/</span> ' + esc(right)


def build_note(n, prev_note, next_note, md):
    body = md.render(n.path.read_text(encoding='utf-8'),
                     {'src_dir': n.path.parent, 'u': up(n.depth)})
    body = heading_ids(body)
    body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    body = re.sub(r'<a href="([^"]+)\.md(#[^"]*)?">', lambda m: '<a href="%s.html%s">' % (m.group(1), m.group(2) or ''), body)
    nav = []
    if prev_note:
        nav.append('<a class="pager prev" href="%s%s"><span>上一篇</span>%s</a>' % (up(n.depth), prev_note.url, esc(prev_note.title)))
    if next_note:
        nav.append('<a class="pager next" href="%s%s"><span>下一篇</span>%s</a>' % (up(n.depth), next_note.url, esc(next_note.title)))
    content = '<article class="prose">%s</article><nav class="pager-row">%s</nav>' % (body, ''.join(nav))
    crumbs = '%s <span class="sep">/</span> %s <span class="sep">/</span> <span>%s</span>' % (
        '<a href="%sindex.html">知识库</a>' % up(n.depth),
        '<a href="%s%s">%s</a>' % (up(n.depth), n.subject_url(), esc(n.subject)),
        esc(n.title),
    )
    write(n.url, page(n.title, n.depth, n.subject, crumbs, content, 'is-note'))


def build_docs():
    md = make_md()
    for f, label, group in DOCS:
        p = ROOT / f
        if not p.exists():
            continue
        body = heading_ids(md.render(p.read_text(encoding='utf-8'),
                                     {'src_dir': p.parent, 'u': up(0)}))
        body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
        content = '<article class="prose">%s</article>' % body
        write(f[:-3] + '.html', page(label, 0, 'home', crumb(0, '知识库', label), content))


def write(rel, text):
    p = DIST / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def copy_assets():
    dst = DIST / 'assets'
    dst.mkdir(parents=True, exist_ok=True)
    for name in ('theme.css', 'app.js'):
        shutil.copyfile(SITE_SRC / name, dst / name)
    annex = ROOT / 'Annex'
    if annex.is_dir():
        shutil.copytree(annex, DIST / 'Annex', dirs_exist_ok=True)


def build_search():
    items = []
    for s in SUBJECTS:
        for c in s['courses']:
            for n in c['notes']:
                items.append({
                    't': n.title,
                    'p': '%s / %s' % (s['name'], c['name']),
                    'u': n.url,
                    'h': n.first,
                })
    for f, label, group in DOCS:
        p = ROOT / f
        if p.exists():
            items.append({'t': label, 'p': '仓库说明', 'u': f[:-3] + '.html', 'h': ''})
    with io.open(DIST / 'assets' / 'search.json', 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(items, fh, ensure_ascii=False)


Note.subject_url = lambda self, s=None: fs_name(self.subject) + '/index.html'


TEMPLATE = '''<!doctype html>
<html lang="zh-CN" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · NOMAD</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="{u}assets/theme.css">
</head>
<body class="{body_class}">
<button class="menu-btn" id="menuBtn" aria-label="目录">{menu}</button>
<aside class="sidebar" id="sidebar">
  <div class="sidebar-inner">
    <a class="brand" href="{u}index.html">
      <span class="brand-mark">{brand_icon}</span>
      <span class="brand-text"><strong>NOMAD</strong><small>个人知识库</small></span>
    </a>
    <button class="search-trigger" id="searchTrigger">
      {search_icon}<span>搜索笔记</span><kbd>Ctrl K</kbd>
    </button>
    <nav class="tree">
      <p class="tree-label">知识目录</p>
      {nav}
    </nav>
    <div class="sidebar-foot">
      <p class="foot-title">公开知识库</p>
      <p class="foot-desc">记录、整理、再次理解。</p>
    </div>
  </div>
</aside>
<main class="main">
  <header class="topbar">
    <div class="crumbs">{crumbs}</div>
    <div class="topbar-right">
      <span class="wordmark">NOMAD</span>
      <button class="theme-btn" id="themeBtn" aria-label="切换主题">{moon}{sun}</button>
    </div>
  </header>
  {content}
  <footer class="site-foot"><span>积累一点, 理解一点。</span><span class="dot">·</span><span>NOMAD</span></footer>
</main>
<div class="search-mask" id="searchMask" hidden>
  <div class="search-box">
    <input id="searchInput" type="text" autocomplete="off" placeholder="搜索标题, 课程或正文">
    <div class="search-hint">↑ ↓ 选择 · Enter 打开 · Esc 关闭</div>
    <div class="search-results" id="searchResults"></div>
  </div>
</div>
<script>window.NOMAD_ROOT = "{u}";</script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-c.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-python.min.js"></script>
<script src="{u}assets/app.js"></script>
</body>
</html>
'''

SIDEBAR = '''{items}
<div class="foot-links">{docs}</div>'''

CARD = '''<a class="card" href="{u}{url}">
  <div class="card-top">{icon}<span class="card-num">{num}</span></div>
  <h3 class="card-name">{name}<span class="card-arrow">↗</span></h3>
  <p class="card-desc">{desc}</p>
  <p class="card-count">{count} 篇笔记</p>
</a>'''

SUBJECTS = []
TOTAL = 0


def main():
    global SUBJECTS, TOTAL
    SUBJECTS = collect()
    TOTAL = sum(s['count'] for s in SUBJECTS)
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    copy_assets()
    build_index()
    for s in SUBJECTS:
        build_subject(s)
    md = make_md()
    for s in SUBJECTS:
        for c in s['courses']:
            flat = c['notes']
            for i, n in enumerate(flat):
                n.first = plain_text(n.path)
                n.subject = s['name']
                prev_n = flat[i - 1] if i > 0 else None
                next_n = flat[i + 1] if i + 1 < len(flat) else None
                build_note(n, prev_n, next_n, md)
    build_docs()
    build_search()
    print('pages: %d' % (1 + len(SUBJECTS) + TOTAL + len(DOCS)))


if __name__ == '__main__':
    main()