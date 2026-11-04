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
var bar=document.createElement('div');bar.className='prog';body.appendChild(bar);
function spy(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?h.scrollTop/max*100:0)+'%';
var cur=null;$$('main h2[id]').forEach(function(x){if(x.offsetParent!==null&&x.getBoundingClientRect().top<140)cur=x.id});
$$('aside a,aside span').forEach(function(a){var k=a.getAttribute('data-id')||(a.getAttribute('href')||'').slice(1);a.classList.toggle('cur',k===cur)})}
addEventListener('scroll',spy,{passive:true});addEventListener('resize',spy);spy();
})();