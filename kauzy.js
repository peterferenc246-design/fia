/* FIA FOX — kauzy.js
   Filter (chipy) + triedenie (sortbar) + svietenie kategórií pre register kauz #303 foxprof.club
   Jazykovo nezávislý: číta výhradne data-* atribúty na <details class="case">.
   - chipy:   data-filter  (all | eu | de | sk | kartell | gdpr | strafrecht)
   - karty:   data-cat (jurisdikcia: eu/de/sk) + data-area (oblasť: kartell/gdpr/strafrecht)
              data-date (ISO YYYY-MM-DD) · data-az · data-ourref
   - sortbar: .sortbtn[data-sort]  (date | az | ourref | area)
   - smer:    #kdir  data-dir (desc = najnovšie hore, asc = najstaršie hore)
   Prázdne hodnoty (data-az="", data-ourref="") idú vždy na koniec.

   SVIETENIE: keď je kauza otvorená (details[open]) a nie je skrytá filtrom,
   rozsvietia sa zlato VŠETKY chipy, do ktorých patrí (jurisdikcia data-cat + oblasť data-area).
   Viac otvorených kaúz = zjednotenie. Po zatvorení zhasnú.
   Svietenie (trieda .lit + zlatý glow, inline style) je oddelené od filter-.active (navy),
   takže obe môžu byť na chipe naraz bez kolízie.
*/
(function () {
  var LIT_SHADOW = '0 0 0 2px rgba(255,203,62,.90), 0 3px 12px rgba(255,203,62,.55)';
  var LIT_BORDER = '#FFCB3E';

  function init() {
    var root = document.getElementById('fia-kauzy');
    if (!root) return;
    var wrap = root.querySelector('.cases');
    if (!wrap) return;

    var cases    = [].slice.call(wrap.querySelectorAll('details.case'));
    var chips    = [].slice.call(root.querySelectorAll('.chip[data-filter]'));
    var sortbtns = [].slice.call(root.querySelectorAll('.sortbtn[data-sort]'));
    var dirBtn   = root.querySelector('#kdir');

    var state = { filter: 'all', sort: 'date', dir: 'desc' };

    function attr(el, key) { return el.getAttribute('data-' + key) || ''; }

    // Rozsvieti chipy podľa kategórií práve otvorených (a filtrom neskrytých) kaúz.
    function relight() {
      var lit = {};
      cases.forEach(function (c) {
        if (!c.open || c.classList.contains('hide')) return;
        var cat = attr(c, 'cat'), area = attr(c, 'area');
        if (cat)  lit[cat]  = true;
        if (area) lit[area] = true;
      });
      chips.forEach(function (chip) {
        var f = attr(chip, 'filter');
        var on = f && f !== 'all' && lit[f];
        if (on) {
          chip.classList.add('lit');
          chip.style.boxShadow   = LIT_SHADOW;
          chip.style.borderColor = LIT_BORDER;
        } else {
          chip.classList.remove('lit');
          chip.style.boxShadow   = '';
          chip.style.borderColor = '';
        }
      });
    }

    function applyFilter() {
      cases.forEach(function (c) {
        var f = state.filter;
        var show = f === 'all'
                || attr(c, 'cat')  === f
                || attr(c, 'area') === f;
        c.classList.toggle('hide', !show);
      });
      relight();
    }

    function applySort() {
      var key = state.sort;
      var dir = state.dir === 'asc' ? 1 : -1;
      cases.slice().sort(function (a, b) {
        var va = attr(a, key), vb = attr(b, key);
        var ea = va === '', eb = vb === '';
        if (ea && eb) return 0;
        if (ea) return 1;        // prázdne vždy dole
        if (eb) return -1;
        if (va < vb) return -1 * dir;
        if (va > vb) return  1 * dir;
        return 0;
      }).forEach(function (c) { wrap.appendChild(c); });
    }

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (x) { x.classList.remove('active'); });
        chip.classList.add('active');
        state.filter = attr(chip, 'filter') || 'all';
        applyFilter();
      });
    });

    // Svietenie kategórií pri otvorení/zatvorení ktorejkoľvek kauzy.
    cases.forEach(function (c) {
      c.addEventListener('toggle', relight);
    });

    sortbtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        sortbtns.forEach(function (x) { x.classList.remove('active'); });
        btn.classList.add('active');
        state.sort = attr(btn, 'sort') || 'date';
        applySort();
      });
    });

    if (dirBtn) {
      dirBtn.addEventListener('click', function () {
        state.dir = state.dir === 'desc' ? 'asc' : 'desc';
        dirBtn.setAttribute('data-dir', state.dir);
        dirBtn.classList.toggle('active', state.dir === 'asc');
        var tn = dirBtn.firstChild;                 // textový uzol s ikonou "\u2b07 " / "\u2b06 "
        if (tn && tn.nodeType === 3) {
          tn.nodeValue = (state.dir === 'desc' ? '\u2b07 ' : '\u2b06 ');
        }
        applySort();
      });
    }

    applyFilter();
    applySort();
    relight();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* FIA FOX — kauzy.js · ČASŤ 2: zdieľacie menu (Teilen/Share) pre karty #303
   Generuje sa klientsky, aby blok stránky zostal ľahký. Číta kontext karty:
   - URL na zdieľanie = location.origin + pathname + '#' + id karty (.case[id])
   - 9 jazykov titulu z .case-title .gtl.<lang> (per-vlajka text pre WhatsApp/X/Telegram/E-mail)
   FB/Messenger/LinkedIn ťahajú og:title (text z URL neberú). Copy = navigator.clipboard.
   Poradie: WhatsApp · Facebook · Messenger · Telegram · X · LinkedIn · E-mail · Kopírovať odkaz.
*/
(function () {
  var L = ["de","en","sk","hr","pl","es","it","fr","sv"];
  var TAG = "FIA FOX – Fair Internet Initiative";
  var ICON = {
    wa:  ["#25D366","M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.247-.694.247-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"],
    fb:  ["#1877F2","M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"],
    msgr:["#0084FF","M12 0C5.24 0 0 4.95 0 11.64c0 3.5 1.44 6.53 3.78 8.62.2.18.32.43.32.7l.07 2.14c.02.68.72 1.13 1.35.85l2.39-1.05c.2-.09.43-.11.64-.05 1.09.3 2.26.46 3.45.46 6.76 0 12-4.95 12-11.64C24 4.95 18.76 0 12 0zm7.2 8.94l-3.52 5.6c-.56.9-1.76 1.13-2.6.5l-2.8-2.1c-.26-.2-.6-.2-.87 0l-3.79 2.87c-.5.38-1.17-.22-.82-.75l3.52-5.6c.56-.9 1.76-1.13 2.6-.5l2.8 2.1c.26.2.6.2.87 0l3.79-2.87c.5-.39 1.17.22.82.75z"],
    tg:  ["#229ED9","M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.022c.242-.213-.054-.334-.373-.121l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.538-.196 1.006.128.83.941z"],
    x:   ["#000000","M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932 6.064-6.933zm-1.29 19.5h2.039L6.486 3.24H4.298l13.314 17.413z"],
    li:  ["#0A66C2","M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"],
    mail:["#1F3864","M22 4H2C.9 4 0 4.9 0 6v12c0 1.1.9 2 2 2h20c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-10 5L2 8V6l10 5 10-5v2z"],
    copy:["#1F3864","M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"]
  };
  var SHARE = {de:"↗ Teilen",en:"↗ Share",sk:"↗ Zdieľať",hr:"↗ Podijeli",pl:"↗ Udostępnij",es:"↗ Compartir",it:"↗ Condividi",fr:"↗ Partager",sv:"↗ Dela"};
  var COPY  = {de:"Link kopieren",en:"Copy link",sk:"Kopírovať odkaz",hr:"Kopiraj poveznicu",pl:"Kopiuj link",es:"Copiar enlace",it:"Copia link",fr:"Copier le lien",sv:"Kopiera länk"};
  var COPIED= {de:"Link kopiert",en:"Link copied",sk:"Odkaz skopírovaný",hr:"Poveznica kopirana",pl:"Skopiowano link",es:"Enlace copiado",it:"Link copiato",fr:"Lien copié",sv:"Länk kopierad"};
  var MTIP  = {de:"Funktioniert nur in der mobilen Messenger-App",en:"Works only in the Messenger mobile app",sk:"Funguje len v mobilnej aplikácii Messenger",hr:"Radi samo u mobilnoj aplikaciji Messenger",pl:"Działa tylko w aplikacji mobilnej Messenger",es:"Funciona solo en la app móvil de Messenger",it:"Funziona solo nell'app mobile di Messenger",fr:"Fonctionne uniquement dans l'application mobile Messenger",sv:"Fungerar bara i Messenger-mobilappen"};

  function esc(s){return (s==null?"":String(s)).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
  function svg(k){var a=ICON[k];return '<svg class="shr-ic" viewBox="0 0 24 24" width="16" height="16" fill="'+a[0]+'" aria-hidden="true"><path d="'+a[1]+'"/></svg>';}
  function gtl(map){return L.map(function(l){return '<span class="gtl '+l+'">'+esc(map[l])+'</span>';}).join("");}

  function build(menuEl){
    var caseEl = menuEl.closest('.case'); if(!caseEl) return;
    var id = caseEl.id || "";
    var url = location.origin + location.pathname + (id ? "#"+id : "");
    var u = encodeURIComponent(url);
    var T = {};
    L.forEach(function(l){ var s=caseEl.querySelector('.case-title .gtl.'+l); T[l]= s ? s.textContent.trim() : ""; });
    var fb  = '<a class="shr-i" href="https://www.facebook.com/sharer/sharer.php?u='+u+'" target="_blank" rel="noopener">'+svg("fb")+'<span>Facebook</span></a>';
    var li  = '<a class="shr-i" href="https://www.linkedin.com/sharing/share-offsite/?url='+u+'" target="_blank" rel="noopener">'+svg("li")+'<span>LinkedIn</span></a>';
    var msgr= '<span class="shr-i shr-msgr"><a class="shr-msgr-a" href="fb-messenger://share/?link='+u+'">'+svg("msgr")+'<span>Messenger</span></a><span class="shr-mt">'+gtl(MTIP)+'</span></span>';
    var wa="",x="",tg="",mail="";
    L.forEach(function(l){
      var text=(T[l]||"")+" | "+TAG; var t=encodeURIComponent(text);
      wa  += '<a class="shr-i gtl '+l+'" href="https://wa.me/?text='+encodeURIComponent(text+"\n"+url)+'" target="_blank" rel="noopener">'+svg("wa")+'<span>WhatsApp</span></a>';
      x   += '<a class="shr-i gtl '+l+'" href="https://twitter.com/intent/tweet?url='+u+'&text='+t+'" target="_blank" rel="noopener">'+svg("x")+'<span>X</span></a>';
      tg  += '<a class="shr-i gtl '+l+'" href="https://t.me/share/url?url='+u+'&text='+t+'" target="_blank" rel="noopener">'+svg("tg")+'<span>Telegram</span></a>';
      mail+= '<a class="shr-i gtl '+l+'" href="mailto:?subject='+encodeURIComponent(T[l]||"")+'&body='+encodeURIComponent(text+"\n"+url)+'">'+svg("mail")+'<span>E-mail</span></a>';
    });
    var copy='<button type="button" class="shr-i shr-copy" data-url="'+esc(url)+'">'+svg("copy")+'<span class="shr-cl">'+gtl(COPY)+'</span><span class="shr-toast">'+gtl(COPIED)+'</span></button>';
    menuEl.innerHTML = wa+fb+msgr+tg+x+li+mail+copy;
  }

  function initShare(){
    var root=document.getElementById('fia-kauzy'); if(!root) return;
    [].slice.call(root.querySelectorAll('details.shr .shr-menu')).forEach(build);
  }

  document.addEventListener('click', function(e){
    var b = e.target.closest ? e.target.closest('.shr-copy') : null;
    if(b){
      e.preventDefault();
      var u=b.getAttribute('data-url')||location.href;
      var ok=function(){ b.classList.add('copied'); setTimeout(function(){ b.classList.remove('copied'); },1600); };
      if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(u).then(ok,function(){}); }
      else{ var t=document.createElement('textarea'); t.value=u; document.body.appendChild(t); t.select(); try{document.execCommand('copy');ok();}catch(_){} document.body.removeChild(t); }
      return;
    }
    var open=document.querySelectorAll('details.shr[open]');
    if(open.length){ [].slice.call(open).forEach(function(d){ if(!d.contains(e.target)) d.removeAttribute('open'); }); }
  });

  if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded', initShare); } else { initShare(); }
})();
