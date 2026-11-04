import glob, os, re, json, html, shutil, base64, yaml, markdown

BASE = os.environ.get("BASE", "https://docs.fireclient.net").rstrip("/")
TODAY = "2026-11-04"
LATEST = "v1.0.10"
OG = "https://www.fireclient.net/assets/og-image.png"
SITE = "FireClient Docs"
GH = "https://github.com/fire-client/fireclient"
REL = "https://github.com/untitledinfo/verifed-fireclient/releases"
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

CSS = """
:root{--bg:#fff;--subtle:#f6f8fa;--text:#1f2328;--muted:#59636e;--line:#d1d9e0;--link:#0969da;--code:#eff1f3;--noteb:#0969da;--notebg:#ddf4ff;--hover:#eaeef2;--brand:#e5322d}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--subtle:#151b23;--text:#f0f6fc;--muted:#9198a1;--line:#3d444d;--link:#4493f8;--code:#262c36;--noteb:#4493f8;--notebg:#10243e;--hover:#262c36;--brand:#ff5a4f}}
:root[data-theme="dark"]{--bg:#0d1117;--subtle:#151b23;--text:#f0f6fc;--muted:#9198a1;--line:#3d444d;--link:#4493f8;--code:#262c36;--noteb:#4493f8;--notebg:#10243e;--hover:#262c36;--brand:#ff5a4f}
:root{box-sizing:border-box;color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + 80px);scroll-behavior:smooth}
*,*::before,*::after{box-sizing:inherit}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);background:var(--subtle);z-index:10}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;display:flex;gap:18px;align-items:center;padding:10px 24px;background:var(--subtle);border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:10px;font-weight:600;color:var(--text);white-space:nowrap}.logo:hover{text-decoration:none}
.logo img{height:26px;width:auto;display:block}.logo span{color:var(--muted);font-weight:400}
.hl{display:flex;gap:4px;font-size:14px}.hl a{color:var(--text);padding:5px 10px;border-radius:6px}.hl a:hover{background:var(--hover);text-decoration:none}
.pill{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:1px 9px;color:var(--muted);background:var(--bg)}.pill:hover{text-decoration:none;color:var(--link)}
#q{flex:1;max-width:340px;margin-left:auto;min-width:0;padding:6px 12px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--text);font:inherit;font-size:14px}
button{font:inherit;font-size:14px;border:1px solid var(--line);background:var(--bg);color:var(--text);border-radius:6px;padding:5px 10px;cursor:pointer}
.wrap{display:grid;grid-template-columns:260px minmax(0,1fr) 200px;gap:40px;max-width:1360px;margin:0 auto;padding:24px}
nav{position:sticky;top:76px;align-self:start;max-height:calc(100vh - 96px);overflow:auto;font-size:14px}
nav a{display:block;padding:6px 12px;color:var(--text);border-radius:6px}nav a:hover{background:var(--hover);text-decoration:none}
nav a.on{background:var(--hover);font-weight:600;box-shadow:inset 3px 0 0 var(--brand)}
nav b{display:block;margin:18px 12px 4px;font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}nav b:first-child{margin-top:0}
aside{position:sticky;top:76px;align-self:start;font-size:13px;border-left:1px solid var(--line);padding-left:16px}
aside b{display:block;margin-bottom:6px}aside a{display:block;padding:3px 0;color:var(--muted)}aside a:hover{color:var(--link)}
main{min-width:0;max-width:800px}
.crumb{font-size:14px;color:var(--muted);margin-bottom:8px}
h1{font-size:2.1rem;font-weight:600;line-height:1.25;margin:0 0 .5em}
h2{font-size:1.5rem;font-weight:600;margin:1.6em 0 .6em;padding-bottom:.3em;border-bottom:1px solid var(--line)}
h3{font-size:1.15rem;font-weight:600;margin:1.4em 0 .4em}
.headerlink{margin-left:8px;color:var(--muted);opacity:0;font-weight:400;text-decoration:none}h2:hover .headerlink,h3:hover .headerlink{opacity:1}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
code,pre{background:var(--code);border-radius:6px;font:85% ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace}
code{padding:.2em .4em}pre{position:relative;padding:16px;overflow-x:auto;background:var(--subtle);border:1px solid var(--line)}pre code{padding:0;background:none}
pre button{position:absolute;top:8px;right:8px;font-size:12px;padding:2px 8px;opacity:.75}
kbd{border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:2px 6px;background:var(--subtle);font:12px ui-monospace,Consolas,monospace}
blockquote{margin:1em 0;background:var(--notebg);border-left:4px solid var(--noteb);padding:2px 16px;border-radius:0 6px 6px 0}
blockquote.warn{--noteb:#bf8700;--notebg:#fff8c5}blockquote.tip{--noteb:#1a7f37;--notebg:#dafbe1}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) blockquote.warn{--notebg:#2d2200}:root:not([data-theme="light"]) blockquote.tip{--notebg:#0f2d1a}}
:root[data-theme="dark"] blockquote.warn{--notebg:#2d2200}:root[data-theme="dark"] blockquote.tip{--notebg:#0f2d1a}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;margin:1em 0}th,td{border:1px solid var(--line);padding:8px 13px;text-align:left}th{background:var(--subtle)}tr:nth-child(2n) td{background:var(--subtle)}
li{margin:.25em 0}
.hero{display:flex;gap:24px;align-items:center;padding:8px 0 24px;border-bottom:1px solid var(--line);margin-bottom:8px}
.hero img{width:104px;height:104px;border-radius:24px;box-shadow:0 8px 30px rgba(229,50,45,.35)}
.hero h1{margin:0 0 .2em}.hero p{margin:.2em 0;color:var(--muted);font-size:1.05rem}
.btn{display:inline-block;margin:10px 8px 0 0;background:#1f883d;color:#fff;padding:7px 16px;border-radius:6px;font-weight:600;font-size:14px}.btn:hover{text-decoration:none;background:#1a7f37}
.btn.ghost{background:var(--subtle);color:var(--text);border:1px solid var(--line)}.btn.ghost:hover{background:var(--hover)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:1em 0}
.card{display:block;border:1px solid var(--line);border-radius:8px;padding:14px 16px;color:var(--text);background:var(--subtle)}
.card:hover{text-decoration:none;border-color:var(--brand)}.card b{display:block;color:var(--link);margin-bottom:4px}.card span{font-size:14px;color:var(--muted)}
.pn{display:flex;justify-content:space-between;gap:12px;margin-top:40px;padding-top:16px;border-top:1px solid var(--line);font-size:14px}
footer{max-width:1360px;margin:0 auto;padding:24px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
@media (max-width:1100px){.wrap{grid-template-columns:240px minmax(0,1fr)}aside{display:none}}
@media (max-width:800px){.wrap{grid-template-columns:1fr;padding:16px}nav{position:static;max-height:none;display:flex;flex-wrap:wrap;gap:4px}nav a{border:1px solid var(--line)}nav b{display:none}header{padding:10px 14px;gap:10px}.hl{display:none}.hero{flex-direction:column;align-items:flex-start}}
"""

JS = """
(function(){var q=document.getElementById('q'),n=[].slice.call(document.querySelectorAll('nav a'));
q.addEventListener('input',function(){var v=q.value.toLowerCase().trim();n.forEach(function(a){a.style.display=!v||a.textContent.toLowerCase().indexOf(v)>-1?'':'none'})});
document.getElementById('theme').addEventListener('click',function(){var r=document.documentElement,d=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);r.setAttribute('data-theme',d?'light':'dark')});
document.querySelectorAll('pre').forEach(function(p){var b=document.createElement('button');b.textContent='Copy';b.onclick=function(){var t=p.querySelector('code').innerText;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1500)},function(){})};p.appendChild(b)});
})();
"""


def data_uri(name):
    return "data:image/png;base64," + base64.b64encode(open("assets/" + name, "rb").read()).decode()


def asset(name, preview):
    return data_uri(name) if preview else "assets/" + name


pages = []
for f in glob.glob("content/*.md"):
    _, fm, body = open(f, encoding="utf-8").read().split("---", 2)
    m = yaml.safe_load(fm)
    m["slug"] = os.path.basename(f)[:-3]
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"],
                           extension_configs={"toc": {"permalink": "#", "permalink_class": "headerlink", "permalink_title": "Link to this section"}})
    h = md.convert(body.strip())
    h = re.sub(r"<blockquote>\s*<p><strong>Warning", '<blockquote class="warn"><p><strong>Warning', h)
    h = re.sub(r"<blockquote>\s*<p><strong>Tip", '<blockquote class="tip"><p><strong>Tip', h)
    m["html"] = h
    m["toc"] = [(t["id"], t["name"].rstrip("#").strip()) for t in md.toc_tokens if t["level"] == 2]
    pages.append(m)
pages.sort(key=lambda p: p["order"])


def file_of(p):
    return "index.html" if p["slug"] == "index" else p["slug"] + ".html"


def url_of(p):
    return BASE + "/" if p["slug"] == "index" else BASE + "/" + p["slug"] + ".html"


def links(body, preview):
    def r(m):
        slug, frag = m.group(1), m.group(2) or ""
        return 'href="#%s"' % slug if preview else 'href="%s.html%s"' % (slug, frag)
    return re.sub(r'href="([a-z0-9-]+)\.md(#[^"]*)?"', r, body)


def nav(preview, cur=None):
    out, last = [], None
    for p in pages:
        if p["group"] != last:
            out.append("<b>%s</b>" % html.escape(p["group"]))
            last = p["group"]
        href = "#" + p["slug"] if preview else file_of(p)
        out.append('<a href="%s"%s>%s</a>' % (href, ' class="on"' if p is cur else "", html.escape(p["title"])))
    return "\n".join(out)


def hero(preview):
    d = "#download" if preview else "download.html"
    i = "#installation" if preview else "installation.html"
    return ('<div class="hero"><img src="%s" alt="FireClient app icon" width="104" height="104"><div>'
            '<h1>FireClient documentation</h1><p>Minecraft, Your Way. Install, set up and get the most out of the FireClient launcher and in-game client.</p>'
            '<a class="btn" href="%s">Download %s</a><a class="btn ghost" href="%s">Install guide</a><a class="btn ghost" href="%s">GitHub</a></div></div>'
            ) % (asset("icon-256.png", preview), d, LATEST, i, GH)


def article(p, i, preview):
    prev_ = pages[i - 1] if i > 0 else None
    next_ = pages[i + 1] if i < len(pages) - 1 else None
    h = lambda q: ("#" + q["slug"]) if preview else file_of(q)
    pn = '<div class="pn"><span>%s</span><span>%s</span></div>' % (
        '<a href="%s">← %s</a>' % (h(prev_), html.escape(prev_["title"])) if prev_ else "",
        '<a href="%s">%s →</a>' % (h(next_), html.escape(next_["title"])) if next_ else "")
    crumb = "FireClient / Docs / %s%s" % (html.escape(p["group"]), "" if p["slug"] == "index" else " / " + html.escape(p["title"]))
    top = hero(preview) if p.get("hero") else '<div class="crumb">%s</div>\n<h1>%s</h1>' % (crumb, html.escape(p["title"]))
    return "%s\n%s\n%s" % (top, links(p["html"], preview), pn)


def toc(p):
    items = "".join('<a href="#%s">%s</a>' % (i, html.escape(n)) for i, n in p["toc"])
    return "<aside><b>On this page</b>%s</aside>" % items if items else "<aside></aside>"


def jsonld(p):
    u = url_of(p)
    crumbs = [("FireClient", "https://www.fireclient.net/"), ("Docs", BASE + "/")]
    if p["slug"] != "index":
        crumbs.append((p["title"], u))
    app = {"@type": "SoftwareApplication", "name": "FireClient", "alternateName": "Fire Client",
           "applicationCategory": "GameApplication", "operatingSystem": "Windows 10, Windows 11, macOS, Linux",
           "softwareVersion": LATEST.lstrip("v"), "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    if p["slug"] == "download":
        app["downloadUrl"] = REL + "/latest"
    g = [
        {"@type": "TechArticle", "headline": p["title"], "description": p["description"], "url": u,
         "inLanguage": "en", "dateModified": TODAY, "mainEntityOfPage": u,
         "image": OG,
         "author": [{"@type": "Person", "name": "FirePDX"}, {"@type": "Person", "name": "Sajjad Ahmed"}],
         "publisher": {"@type": "Organization", "name": "FireClient", "url": "https://www.fireclient.net/",
                       "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon-512.png"}},
         "about": app},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": link} for i, (n, link) in enumerate(crumbs)]}]
    if p["slug"] == "index":
        g.append({"@type": "WebSite", "name": SITE, "url": BASE + "/", "inLanguage": "en"})
    if p["slug"] == "faq":
        qa = re.findall(r"<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>", p["html"], re.S)
        strip = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).rstrip("#").strip()
        g.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qa]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def head(p):
    t = "FireClient Docs: Install, Download, HUD, Mods and Help" if p["slug"] == "index" else p["title"] + " | " + SITE
    d = html.escape(p["description"], quote=True)
    u = url_of(p)
    te = html.escape(t, quote=True)
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(t)}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{u}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="FirePDX, Sajjad Ahmed">
<meta name="theme-color" content="#0d1117">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{te}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{te}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{OG}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="assets/favicon-48.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{jsonld(p)}</script>"""


def header(preview):
    home = "#index" if preview else "index.html"
    rel = "#release-notes" if preview else "release-notes.html"
    dl = "#download" if preview else "download.html"
    return ('<header><a class="logo" href="%s"><img src="%s" alt="FireClient logo" height="26"><span>Docs</span></a>'
            '<div class="hl"><a href="%s">Download</a><a href="%s">Release notes</a><a href="%s">GitHub</a></div>'
            '<a class="pill" href="%s">%s</a>'
            '<input id="q" type="search" placeholder="Search docs" aria-label="Search docs"><button id="theme" aria-label="Toggle theme">◐</button></header>'
            ) % (home, asset("logo-mark.png", preview), dl, rel, GH, rel, LATEST)


FOOT = ('<footer>FireClient is not affiliated with Mojang or Microsoft. · <a href="https://www.fireclient.net/">fireclient.net</a> · '
        '<a href="%s">GitHub</a> · <a href="https://discord.gg/r23YNWWfrx">Discord</a> · Made by FirePDX and Sajjad Ahmed</footer>' % GH)

out = "site"
shutil.rmtree(out, ignore_errors=True)
os.makedirs(out)
shutil.copytree("assets", out + "/assets")
shutil.copy("assets/favicon.ico", out + "/favicon.ico")
open(out + "/style.css", "w").write(CSS.strip())
open(out + "/script.js", "w").write(JS.strip())


def full(p, i):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(p)}
</head>
<body>
{header(False)}
<div class="wrap">
<nav aria-label="Docs">
{nav(False, p)}
</nav>
<main>
{article(p, i, False)}
</main>
{toc(p)}
</div>
{FOOT}
<script src="script.js" defer></script>
</body>
</html>
"""


for i, p in enumerate(pages):
    open(os.path.join(out, file_of(p)), "w", encoding="utf-8").write(full(p, i))

nf = {"slug": "404", "title": "Page not found", "description": "This page does not exist.", "group": "Get started", "html": '<p>That page does not exist. Try the <a href="index.html">docs home</a> or the <a href="download.html">download page</a>.</p>', "toc": []}
open(out + "/404.html", "w", encoding="utf-8").write(
    full(nf, 0).replace('content="index, follow, max-image-preview:large, max-snippet:-1"', 'content="noindex"').replace(article(nf, 0, False), '<h1>Page not found</h1>' + nf["html"]))

urls = "\n".join(f"  <url><loc>{url_of(p)}</loc><lastmod>{TODAY}</lastmod><priority>{'1.0' if p['slug']=='index' else '0.8'}</priority></url>" for p in pages)
open(out + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
open(out + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

arts = "\n".join('<article id="p-%s" hidden>%s</article>' % (p["slug"], article(p, i, True)) for i, p in enumerate(pages))
data = json.dumps({p["slug"]: [p["title"], [list(t) for t in p["toc"]]] for p in pages}, ensure_ascii=False)
pv = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>FireClient Docs</title><link rel="icon" href="{data_uri('favicon-32.png')}"><style>{CSS}</style></head>
<body>{header(True)}
<div class="wrap"><nav aria-label="Docs">{nav(True)}</nav><main>{arts}</main><aside id="toc"></aside></div>{FOOT}
<script>{JS}
var D={data};
function show(){{var s=(location.hash||'#index').slice(1);if(!D[s])s='index';
document.querySelectorAll('article').forEach(function(a){{a.hidden=a.id!=='p-'+s}});
document.querySelectorAll('nav a').forEach(function(a){{a.classList.toggle('on',a.getAttribute('href')==='#'+s)}});
var t=document.getElementById('toc');t.innerHTML=D[s][1].length?'<b>On this page</b>'+D[s][1].map(function(x){{return '<span data-id="'+x[0]+'" style="display:block;padding:3px 0;color:var(--muted);cursor:pointer">'+x[1]+'</span>'}}).join(''):'';
document.title=(s==='index'?'':D[s][0]+' | ')+'FireClient Docs';scrollTo(0,0)}}
document.getElementById('toc').addEventListener('click',function(e){{var i=e.target.getAttribute('data-id');if(i){{var el=document.querySelector('article:not([hidden]) [id="'+i+'"]');if(el)el.scrollIntoView()}}}});
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a.headerlink');if(a){{e.preventDefault();var el=a.parentElement;if(el)el.scrollIntoView()}}}});
addEventListener('hashchange',show);show();</script></body></html>"""
os.makedirs("/mnt/user-data/outputs", exist_ok=True)
open("/mnt/user-data/outputs/fireclient-docs.html", "w", encoding="utf-8").write(pv)
print(len(pages), "pages;", len(pv) // 1024, "KB preview")
