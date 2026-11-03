(function () {
  var root = window.NOMAD_ROOT || '';
  var doc = document.documentElement;

  // 主题
  var saved = null;
  try { saved = localStorage.getItem('nomad-theme'); } catch (e) {}
  if (saved === 'light' || saved === 'dark') doc.dataset.theme = saved;

  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = doc.dataset.theme === 'dark' ? 'light' : 'dark';
      doc.dataset.theme = next;
      try { localStorage.setItem('nomad-theme', next); } catch (e) {}
    });
  }

  // 窄屏目录
  var menuBtn = document.getElementById('menuBtn');
  if (menuBtn) {
    menuBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      document.body.classList.toggle('nav-open');
    });
    document.addEventListener('click', function (e) {
      if (!document.body.classList.contains('nav-open')) return;
      var sb = document.getElementById('sidebar');
      if (sb && sb.contains(e.target)) return;
      document.body.classList.remove('nav-open');
    });
  }

  // 搜索
  var mask = document.getElementById('searchMask');
  var input = document.getElementById('searchInput');
  var list = document.getElementById('searchResults');
  var data = null;
  var sel = 0;
  var hits = [];

  function load(done) {
    if (data) return done();
    fetch(root + 'assets/search.json')
      .then(function (r) { return r.json(); })
      .then(function (j) { data = j; done(); })
      .catch(function () { data = []; done(); });
  }

  function score(item, q) {
    var t = item.t.toLowerCase();
    var p = item.p.toLowerCase();
    var h = (item.h || '').toLowerCase();
    if (t === q) return 100;
    if (t.indexOf(q) === 0) return 80;
    if (t.indexOf(q) >= 0) return 60;
    if (p.indexOf(q) >= 0) return 30;
    if (h.indexOf(q) >= 0) return 15;
    return 0;
  }

  function render() {
    var q = input.value.trim().toLowerCase();
    if (!q) {
      hits = [];
      list.innerHTML = '<div class="result-empty">输入关键词, 搜标题、课程或正文</div>';
      return;
    }
    hits = data
      .map(function (it) { return { it: it, s: score(it, q) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) { return b.s - a.s; })
      .slice(0, 20)
      .map(function (x) { return x.it; });
    if (!hits.length) {
      list.innerHTML = '<div class="result-empty">没有找到, 换个词试试</div>';
      return;
    }
    sel = 0;
    list.innerHTML = hits
      .map(function (it, i) {
        return '<a class="result' + (i === 0 ? ' sel' : '') + '" href="' + root + it.u + '">' +
          '<div class="result-title">' + it.t + '</div>' +
          '<div class="result-path">' + it.p + '</div></a>';
      })
      .join('');
  }

  function open() {
    load(function () {
      if (!mask) return;
      mask.hidden = false;
      input.value = '';
      render();
      input.focus();
    });
  }

  function close() {
    if (mask) mask.hidden = true;
  }

  function move(step) {
    if (!hits.length) return;
    sel = (sel + step + hits.length) % hits.length;
    Array.prototype.forEach.call(list.children, function (el, i) {
      el.classList.toggle('sel', i === sel);
    });
    var cur = list.children[sel];
    if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: 'nearest' });
  }

  var trigger = document.getElementById('searchTrigger');
  if (trigger) trigger.addEventListener('click', open);

  if (mask) {
    mask.addEventListener('click', function (e) { if (e.target === mask) close(); });
    input.addEventListener('input', render);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Enter' && hits[sel]) { window.location.href = root + hits[sel].u; }
      else if (e.key === 'Escape') { close(); }
    });
  }

  document.addEventListener('keydown', function (e) {
    var k = e.key.toLowerCase();
    if ((e.ctrlKey || e.metaKey) && k === 'k') {
      e.preventDefault();
      if (mask && !mask.hidden) close(); else open();
    } else if (k === 'escape' && mask && !mask.hidden) {
      close();
    }
  });

  // 公式
  function math() {
    if (!window.renderMathInElement) return;
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false,
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option']
    });
  }

  if (document.readyState !== 'loading') math();
  else document.addEventListener('DOMContentLoaded', math);

  // 代码高亮
  function highlight() {
    if (window.Prism) window.Prism.highlightAll();
  }
  if (document.readyState !== 'loading') highlight();
  else document.addEventListener('DOMContentLoaded', highlight);
})();