(function(){
  var LANGS=['de','en','sk','hr','pl','es','it','fr','sv'];
  var HOME={de:'\u2190 Zur Startseite',en:'\u2190 Back to homepage',sk:'\u2190 Na domovsk\u00fa str\u00e1nku',hr:'\u2190 Na po\u010detnu stranicu',pl:'\u2190 Strona g\u0142\u00f3wna',es:'\u2190 A la p\u00e1gina principal',it:'\u2190 Alla home',fr:'\u2190 Retour \u00e0 l\u2019accueil',sv:'\u2190 Till startsidan'};
  function root(){return document.getElementById('fia-teilen');}
  function getStored(){try{return localStorage.getItem('fiaLang');}catch(e){return null;}}
  function setStored(l){try{localStorage.setItem('fiaLang',l);}catch(e){}}
  function curLang(){var s=getStored();return (s&&LANGS.indexOf(s)>=0)?s:'de';}
  function apply(lang){
    var r=root();if(!r)return;
    if(LANGS.indexOf(lang)<0)lang='de';
    LANGS.forEach(function(l){var inp=document.getElementById('lng-'+l);if(inp)inp.checked=(l===lang);});
    r.querySelectorAll('.tl').forEach(function(e){e.style.display='none';});
    r.querySelectorAll('.tl.'+lang).forEach(function(e){e.style.display='';});
    r.querySelectorAll('.posttext').forEach(function(e){e.style.display='none';});
    r.querySelectorAll('.posttext.'+lang).forEach(function(e){e.style.display='block';});
    r.querySelectorAll('label.flag').forEach(function(f){f.style.borderColor=(f.getAttribute('data-lang')===lang)?'#1F3864':'transparent';});
    var hb=r.querySelector('.homebtn');if(hb&&HOME[lang])hb.textContent=HOME[lang];
    setStored(lang);
  }
  function sortCards(key){
    var r=root();if(!r)return;
    var wrap=r.querySelector('.cards');if(!wrap)return;
    var cards=Array.prototype.slice.call(wrap.querySelectorAll('.post-card'));
    cards.sort(function(a,b){
      var x=(a.getAttribute('data-'+key)||'').toLowerCase();
      var y=(b.getAttribute('data-'+key)||'').toLowerCase();
      if(key==='date'){return y<x?-1:(y>x?1:0);} /* d\u00e1tum: najnov\u0161ie hore */
      if(x<y)return -1;if(x>y)return 1;return 0;
    });
    cards.forEach(function(c){wrap.appendChild(c);});
  }
  function activeText(card,lang){var t=card.querySelector('.posttext.'+lang)||card.querySelector('.posttext.de');return t?t.innerText.trim():'';}
  function fallbackCopy(txt){var ta=document.createElement('textarea');ta.value=txt;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(ta);}
  function copyText(txt,btn){var done=function(){var old=btn.getAttribute('data-old')||btn.textContent;btn.setAttribute('data-old',old);btn.textContent='\u2713';setTimeout(function(){btn.textContent=old;},1500);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){fallbackCopy(txt);done();});}else{fallbackCopy(txt);done();}}
  document.addEventListener('click',function(e){
    var r=root();if(!r||!r.contains(e.target))return;
    var flag=e.target.closest('label.flag');
    if(flag){e.preventDefault();apply(flag.getAttribute('data-lang'));return;}
    var card=e.target.closest('.post-card');
    var cp=e.target.closest('.btn.copy');
    if(cp&&card){e.preventDefault();copyText(activeText(card,curLang()),cp);return;}
  },false);
  document.addEventListener('change',function(e){
    var r=root();if(!r||!r.contains(e.target))return;
    var sel=e.target.closest('.sortsel');
    if(sel){sortCards(sel.value);}
  },false);
  function init(){apply(curLang());var sel=document.querySelector('#fia-teilen .sortsel');if(sel)sortCards(sel.value);}
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init);}else{init();}
})();
