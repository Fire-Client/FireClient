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
$$('pre').forEach(function(p){var b=document.createElement('button');b.textContent='Copy';b.addEventListener('click',function(){var t=p.querySelector('code').innerText;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Copied \u2713';setTimeout(function(){b.textContent='Copy'},1600)},function(){b.textContent='Press Ctrl+C';setTimeout(function(){b.textContent='Copy'},1600)})});p.appendChild(b)});
var REPO='untitledinfo/verifed-fireclient',KEY='fc-rel-v1';
function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function fd(x){try{return new Date(x).toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'})}catch(e){return ''}}
function sz(n){return n>1048576?(n/1048576).toFixed(1)+' MB':Math.round(n/1024)+' KB'}
function apply(r){var tag=r.tag_name,by={},as=r.assets||[];as.forEach(function(a){by[a.name]=a});
$$('[data-latest]').forEach(function(e){e.textContent=tag});$$('[data-latest-date]').forEach(function(e){e.textContent=fd(r.published_at)});
$$('a[href*="releases/latest/download/"]').forEach(function(a){var n=decodeURIComponent(a.getAttribute('href').split('/').pop()),m=by[n];if(m)a.href=m.browser_download_url;else if(as.length){a.classList.add('na');a.title='Not included in '+tag}});
var box=$('#rel');if(box){var h='<div class="rel-top"><span class="rel-tag">'+esc(tag)+'</span><span>Released '+esc(fd(r.published_at))+'</span><a href="'+esc(r.html_url)+'">Release notes on GitHub</a></div>';
if(as.length)h+='<div class="rel-files">'+as.filter(function(a){return !/[.](sha256|sig|asc)$/i.test(a.name)}).map(function(a){return '<a class="rel-f" href="'+esc(a.browser_download_url)+'"><b>'+esc(a.name)+'</b><span>'+sz(a.size)+' | '+(a.download_count||0)+' downloads'+(a.digest?' | '+esc(a.digest.slice(0,19))+'...':'')+'</span></a>'}).join('')+'</div>';
box.innerHTML=h}}
var cr=null;try{cr=JSON.parse(sessionStorage.getItem(KEY))}catch(e){}
if(cr&&Date.now()-cr.t<600000)apply(cr.r);else if(window.fetch)fetch('https://api.github.com/repos/'+REPO+'/releases/latest',{headers:{Accept:'application/vnd.github+json'}}).then(function(x){return x.ok?x.json():Promise.reject()}).then(function(r){if(r&&r.tag_name){try{sessionStorage.setItem(KEY,JSON.stringify({t:Date.now(),r:r}))}catch(e){}apply(r)}}).catch(function(){});
var bar=document.createElement('div');bar.className='prog';body.appendChild(bar);
function spy(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?h.scrollTop/max*100:0)+'%';
var cur=null;$$('main h2[id]').forEach(function(x){if(x.offsetParent!==null&&x.getBoundingClientRect().top<140)cur=x.id});
$$('aside a,aside span').forEach(function(a){var k=a.getAttribute('data-id')||(a.getAttribute('href')||'').slice(1);a.classList.toggle('cur',k===cur)})}
addEventListener('scroll',spy,{passive:true});addEventListener('resize',spy);spy();
})();