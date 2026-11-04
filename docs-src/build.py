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

DARK = "--bg:#0a0a0e;--subtle:#111117;--text:#ededf2;--muted:#9b9bab;--line:#24242e;--link:#ff7a59;--code:#1c1c25;--noteb:#5b9bff;--notebg:rgba(91,155,255,.1);--hover:#1b1b24;--glow:rgba(255,77,61,.2)"
CSS = """
:root{--bg:#fff;--subtle:#f6f6f9;--text:#18181f;--muted:#62626f;--line:#e2e2ea;--link:#d92d20;--code:#eeeef3;--noteb:#2563eb;--notebg:rgba(37,99,235,.08);--hover:#ececf2;--brand:#ff4d3d;--brand2:#ff8a2b;--glow:rgba(255,77,61,.12);color-scheme:light dark}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){@@DARK@@}}
:root[data-theme="dark"]{@@DARK@@}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + 84px);scroll-behavior:smooth}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.7 Inter,-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
::selection{background:var(--brand);color:#fff}
.prog{position:fixed;top:0;left:0;height:3px;width:0;background:linear-gradient(90deg,var(--brand),var(--brand2));z-index:60}
header{position:sticky;top:0;z-index:20;display:flex;gap:14px;align-items:center;padding:calc(10px + env(safe-area-inset-top,0px)) 24px 10px;background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--text);white-space:nowrap}.logo:hover{text-decoration:none}
.logo img{height:28px;width:auto;display:block}.logo span{color:var(--brand);font-weight:700;letter-spacing:.02em}
.hl{display:flex;gap:2px;font-size:14px;margin-left:8px}.hl a{color:var(--muted);padding:6px 11px;border-radius:8px;font-weight:500}.hl a:hover{background:var(--hover);color:var(--text);text-decoration:none}
.pill{font-size:12px;font-weight:600;border-radius:999px;padding:2px 10px;color:#fff;background:linear-gradient(90deg,var(--brand),var(--brand2))}.pill:hover{text-decoration:none;filter:brightness(1.08)}
#q{flex:1;max-width:320px;margin-left:auto;min-width:0;padding:8px 14px;border:1px solid var(--line);border-radius:10px;background:var(--subtle);color:var(--text);font:inherit;font-size:14px;transition:border-color .15s,box-shadow .15s}
#q:focus{outline:0;border-color:var(--brand);box-shadow:0 0 0 3px var(--glow)}
button{font:inherit;font-size:14px;border:1px solid var(--line);background:var(--subtle);color:var(--text);border-radius:10px;padding:6px 11px;cursor:pointer;transition:background .15s,border-color .15s}button:hover{background:var(--hover);border-color:var(--brand)}
#menu{display:none}
.wrap{display:grid;grid-template-columns:272px minmax(0,1fr) 210px;gap:44px;max-width:1420px;margin:0 auto;padding:28px 24px 40px}
nav{position:sticky;top:84px;align-self:start;max-height:calc(100vh - 104px);overflow:auto;font-size:14px;padding-right:6px}
nav a{display:block;padding:7px 12px;color:var(--muted);border-radius:8px;font-weight:500;transition:background .12s,color .12s}nav a:hover{background:var(--hover);color:var(--text);text-decoration:none}
nav a.on{background:linear-gradient(90deg,var(--glow),transparent);color:var(--text);font-weight:600;box-shadow:inset 3px 0 0 var(--brand)}
nav b{display:block;margin:20px 12px 6px;font-size:11px;font-weight:700;color:var(--text);text-transform:uppercase;letter-spacing:.09em;opacity:.55}nav b:first-child{margin-top:0}
#nores{padding:8px 12px;color:var(--muted)}
aside{position:sticky;top:84px;align-self:start;font-size:13px;border-left:1px solid var(--line);padding-left:16px}
aside b{display:block;margin-bottom:8px;font-size:11px;text-transform:uppercase;letter-spacing:.09em;opacity:.55}
aside a,aside span{display:block;padding:4px 0 4px 10px;margin-left:-11px;border-left:2px solid transparent;color:var(--muted);cursor:pointer}aside a:hover,aside span:hover{color:var(--text);text-decoration:none}
aside .cur{color:var(--link);border-left-color:var(--brand);font-weight:600}
main{min-width:0;max-width:820px}
.crumb{font-size:13px;color:var(--muted);margin-bottom:10px}
h1{font-size:2.4rem;font-weight:800;letter-spacing:-.02em;line-height:1.2;margin:0 0 .6em}
h2{font-size:1.5rem;font-weight:700;letter-spacing:-.01em;margin:2em 0 .7em;padding-bottom:.35em;border-bottom:1px solid var(--line)}
h3{font-size:1.15rem;font-weight:700;margin:1.6em 0 .4em}
.headerlink{margin-left:8px;color:var(--brand);opacity:0;font-weight:400;text-decoration:none}h2:hover .headerlink,h3:hover .headerlink{opacity:1}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
main p,main li{color:color-mix(in srgb,var(--text) 90%,var(--muted))}
code{background:var(--code);border-radius:6px;padding:.18em .42em;font:85% ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace}
pre{position:relative;margin:1.2em 0;padding:18px 18px;overflow-x:auto;background:#0f0f14;color:#e8e8ee;border:1px solid #2a2a35;border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.12);font:13.5px/1.6 ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace}
pre code{padding:0;background:none;color:inherit;font:inherit}
pre button{position:absolute;top:10px;right:10px;font-size:12px;padding:3px 10px;background:#1c1c25;color:#cfcfd8;border-color:#33333f;opacity:.8}
kbd{border:1px solid var(--line);border-bottom-width:3px;border-radius:7px;padding:1px 7px;background:var(--subtle);font:12px ui-monospace,Consolas,monospace}
blockquote{margin:1.2em 0;background:var(--notebg);border:1px solid color-mix(in srgb,var(--noteb) 28%,transparent);border-left:4px solid var(--noteb);padding:4px 18px;border-radius:10px}
blockquote.warn{--noteb:#d97706;--notebg:rgba(217,119,6,.1)}blockquote.tip{--noteb:#16a34a;--notebg:rgba(22,163,74,.1)}
table{border-collapse:separate;border-spacing:0;width:100%;display:block;overflow-x:auto;margin:1.2em 0;border:1px solid var(--line);border-radius:12px}
th,td{padding:10px 16px;text-align:left;border-bottom:1px solid var(--line)}tr:last-child td{border-bottom:0}th{background:var(--subtle);font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
li{margin:.3em 0}img{max-width:100%}
.hero{position:relative;overflow:hidden;display:flex;gap:28px;align-items:center;padding:36px;border:1px solid var(--line);border-radius:22px;margin-bottom:14px;background:radial-gradient(520px 260px at 0 0,var(--glow),transparent 70%),radial-gradient(460px 240px at 100% 100%,rgba(255,138,43,.14),transparent 70%),var(--subtle)}
.hero img{width:112px;height:112px;border-radius:26px;box-shadow:0 10px 40px rgba(255,77,61,.4);flex:none}
.hero h1{margin:0 0 .25em;font-size:2.6rem;background:linear-gradient(90deg,var(--brand),var(--brand2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.hero p{margin:.2em 0 .6em;color:var(--muted);font-size:1.08rem}
.btn{display:inline-block;margin:8px 10px 0 0;background:linear-gradient(90deg,var(--brand),var(--brand2));color:#fff;padding:9px 20px;border-radius:10px;font-weight:700;font-size:14px;box-shadow:0 6px 18px rgba(255,77,61,.3);transition:transform .15s}.btn:hover{text-decoration:none;transform:translateY(-2px)}
.btn.ghost{background:var(--bg);color:var(--text);border:1px solid var(--line);box-shadow:none}.btn.ghost:hover{border-color:var(--brand)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:1.2em 0}
.card{display:block;border:1px solid var(--line);border-radius:14px;padding:16px 18px;color:var(--text);background:var(--subtle);transition:transform .18s,border-color .18s,box-shadow .18s}
.card:hover{text-decoration:none;border-color:var(--brand);transform:translateY(-3px);box-shadow:0 10px 28px var(--glow)}
.card b{display:block;color:var(--text);margin-bottom:4px;font-size:15px}.card b::after{content:" \\2192";color:var(--brand)}.card span{font-size:14px;color:var(--muted);line-height:1.5}
.pn{display:flex;justify-content:space-between;gap:14px;margin-top:48px}
.pn span{flex:1}.pn span:last-child{text-align:right}
.pn a{display:block;padding:14px 18px;border:1px solid var(--line);border-radius:12px;font-weight:600;color:var(--text);background:var(--subtle);transition:border-color .15s,transform .15s}.pn a:hover{text-decoration:none;border-color:var(--brand);transform:translateY(-2px)}
footer{max-width:1420px;margin:0 auto;padding:28px 24px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
@media (max-width:1100px){.wrap{grid-template-columns:260px minmax(0,1fr)}aside{display:none}}
@media (max-width:860px){
#menu{display:inline-flex}.hl{display:none}.wrap{grid-template-columns:1fr;padding:18px 16px 32px}
nav{position:fixed;top:0;left:0;bottom:0;width:min(86vw,320px);max-height:none;transform:translateX(-104%);transition:transform .22s;background:var(--bg);z-index:40;padding:76px 12px 24px;border-right:1px solid var(--line)}
body.menu nav{transform:none}body.menu::after{content:"";position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:30}
header{padding-left:14px;padding-right:14px;gap:10px;z-index:50}#q{max-width:none}
.hero{flex-direction:column;align-items:flex-start;padding:24px}.hero h1,h1{font-size:2rem}.pn{flex-direction:column}.pn span:last-child{text-align:left}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
""".replace("@@DARK@@", DARK)

JS = """
(function(){
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
var q=$('#q'),nav=$('nav'),root=document.documentElement,body=document.body;
try{var st=localStorage.getItem('fc-theme');if(st)root.setAttribute('data-theme',st)}catch(e){}
$('#theme').addEventListener('click',function(){var d=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches),n=d?'light':'dark';root.setAttribute('data-theme',n);try{localStorage.setItem('fc-theme',n)}catch(e){}});
var mb=$('#menu');if(mb)mb.addEventListener('click',function(){body.classList.toggle('menu')});
document.addEventListener('click',function(e){if(body.classList.contains('menu')&&!e.target.closest('nav')&&!e.target.closest('#menu'))body.classList.remove('menu');if(e.target.closest&&e.target.closest('nav a'))body.classList.remove('menu')});
var none=document.createElement('div');none.id='nores';none.textContent='No matching pages';none.hidden=true;nav.appendChild(none);
q.addEventListener('input',function(){var v=q.value.toLowerCase().trim(),hit=0,grp=null,gv=0;
$$('nav b,nav a').forEach(function(el){if(el.tagName==='B'){if(grp)grp.style.display=gv?'':'none';grp=el;gv=0}else{var ok=!v||el.textContent.toLowerCase().indexOf(v)>-1;el.style.display=ok?'':'none';if(ok){hit++;gv++}}});
if(grp)grp.style.display=gv?'':'none';none.hidden=hit>0;if(v)body.classList.add('menu')});
q.addEventListener('keydown',function(e){if(e.key==='Enter'){var a=$$('nav a').filter(function(x){return x.style.display!=='none'})[0];if(a)a.click()}if(e.key==='Escape'){q.value='';q.dispatchEvent(new Event('input'));q.blur()}});
document.addEventListener('keydown',function(e){var t=e.target.tagName;if((e.key==='/'&&t!=='INPUT'&&t!=='TEXTAREA')||((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')){e.preventDefault();q.focus();q.select()}});
$$('pre').forEach(function(p){var b=document.createElement('button');b.textContent='Copy';b.addEventListener('click',function(){var t=p.querySelector('code').innerText;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Copied \\u2713';setTimeout(function(){b.textContent='Copy'},1600)},function(){b.textContent='Press Ctrl+C';setTimeout(function(){b.textContent='Copy'},1600)})});p.appendChild(b)});
var bar=document.createElement('div');bar.className='prog';body.appendChild(bar);
function spy(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?h.scrollTop/max*100:0)+'%';
var cur=null;$$('main h2[id]').forEach(function(x){if(x.offsetParent!==null&&x.getBoundingClientRect().top<140)cur=x.id});
$$('aside a,aside span').forEach(function(a){var k=a.getAttribute('data-id')||(a.getAttribute('href')||'').slice(1);a.classList.toggle('cur',k===cur)})}
addEventListener('scroll',spy,{passive:true});addEventListener('resize',spy);spy();
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
    return ('<header><button id="menu" aria-label="Menu">\u2630</button><a class="logo" href="%s"><img src="%s" alt="FireClient logo" height="26"><span>Docs</span></a>'
            '<div class="hl"><a href="%s">Download</a><a href="%s">Release notes</a><a href="%s">GitHub</a></div>'
            '<a class="pill" href="%s">%s</a>'
            '<input id="q" type="search" placeholder="Search docs  (press /)" aria-label="Search docs"><button id="theme" aria-label="Toggle theme">◐</button></header>'
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
open(out + "/CNAME", "w").write(BASE.split("//")[1] + "\n")
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
print(len(pages), "pages;", len(pv) // 1024, "KB preview")
