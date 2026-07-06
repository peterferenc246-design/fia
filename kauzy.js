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
    var tcBox    = document.getElementById('fia-testcases');
    var allCases = tcBox ? cases.concat([].slice.call(tcBox.querySelectorAll('details.case'))) : cases;
    (function(){ var s=document.createElement('style'); s.textContent='details.case.hide{display:none!important}'; document.head.appendChild(s); })();
    // --- INJEKCIA: area-chip „Zasahovanie do majetkových práv občana" (data-filter=majetok) ---
    // Klon strafrecht chipu (zachová štruktúru + .gtl jazyky), vloženie hneď zaň. Bez zásahu do bloku 3.
    (function(){
      var strf = root.querySelector('.chip[data-filter=strafrecht]');
      if (strf && !root.querySelector('.chip[data-filter=majetok]')) {
        var c = strf.cloneNode(true);
        c.setAttribute('data-filter','majetok');
        c.classList.remove('active','lit');
        c.style.boxShadow=''; c.style.borderColor='';
        var L={de:"Eingriff in Eigentumsrechte",en:"Interference with property rights",sk:"Zasahovanie do majetkových práv občana",hr:"Zadiranje u imovinska prava",pl:"Naruszenie praw majątkowych",es:"Injerencia en derechos patrimoniales",it:"Ingerenza nei diritti patrimoniali",fr:"Atteinte aux droits patrimoniaux",sv:"Intrång i egendomsrätt"};
        Object.keys(L).forEach(function(l){ var sp=c.querySelector('.gtl.'+l); if(sp) sp.textContent=L[l]; });
        strf.parentNode.insertBefore(c, strf.nextSibling);
      }
    })();
    var chips    = [].slice.call(root.querySelectorAll('.chip[data-filter]'));
    var sortbtns = [].slice.call(root.querySelectorAll('.sortbtn[data-sort]'));
    var dirBtn   = root.querySelector('#kdir');

    var state = { sort: 'date', dir: 'desc' };
    var selected = {};   // multi-select kategórií (prázdne = zobraz všetko)

    function attr(el, key) { return el.getAttribute('data-' + key) || ''; }

    // Rozsvieti chipy podľa kategórií práve otvorených (a filtrom neskrytých) kaúz.
    function relight() {
      var lit = {};
      allCases.forEach(function (c) {
        if (!c.open || c.classList.contains('hide')) return;
        (attr(c, 'cat') + ' ' + attr(c, 'area')).split(/\s+/).forEach(function (x) { if (x) lit[x] = true; });
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
      var keys = Object.keys(selected);
      var noFilter = keys.length === 0;
      allCases.forEach(function (c) {
        var vals = (attr(c, 'cat') + ' ' + attr(c, 'area')).split(/\s+/);
        var show = noFilter || keys.some(function (k) { return vals.indexOf(k) >= 0; });
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

    function clearCats() {
      selected = {};
      chips.forEach(function (x) { x.classList.remove('active'); });
      applyFilter();
    }
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var f = attr(chip, 'filter');
        if (!f || f === 'all') { clearCats(); return; }
        if (selected[f]) { delete selected[f]; chip.classList.remove('active'); }
        else { selected[f] = true; chip.classList.add('active'); }
        applyFilter();
      });
    });
    var regAll = document.querySelector('#fia-reg .rbtn[data-regall]');
    if (regAll) { regAll.addEventListener('click', clearCats); }

    // Svietenie kategórií pri otvorení/zatvorení ktorejkoľvek kauzy.
    allCases.forEach(function (c) {
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

/* ===== FIA FOX — komentárový modul (B1, natívne WP komentáre) ===== */
(function(){
  var REST = location.origin + '/wp-json/wp/v2';
  var POST_EP = location.origin + '/wp-comments-post.php';
  var S = {
    title:{de:'Öffentliche Kommentare',en:'Public comments',sk:'Verejné komentáre',hr:'Javni komentari',pl:'Komentarze publiczne',es:'Comentarios públicos',it:'Commenti pubblici',fr:'Commentaires publics',sv:'Offentliga kommentarer'},
    mod:{de:'moderiert – Freigabe durch Admin',en:'moderated – admin approval',sk:'moderované – schvaľuje admin',hr:'moderirano – odobrava admin',pl:'moderowane – zatwierdza admin',es:'moderado – aprueba admin',it:'moderato – approva admin',fr:'modéré – validation admin',sv:'modererat – admin godkänner'},
    name:{de:'Name / Pseudonym',en:'Name / pseudonym',sk:'Meno / prezývka',hr:'Ime / nadimak',pl:'Imię / pseudonim',es:'Nombre / seudónimo',it:'Nome / pseudonimo',fr:'Nom / pseudo',sv:'Namn / pseudonym'},
    email:{de:'E-Mail (nicht öffentlich)',en:'Email (not public)',sk:'E-mail (nezverejní sa)',hr:'E-pošta (nije javno)',pl:'E-mail (niepubliczny)',es:'Correo (no público)',it:'Email (non pubblica)',fr:'E-mail (non public)',sv:'E-post (ej offentlig)'},
    body:{de:'Ihr Kommentar …',en:'Your comment …',sk:'Váš komentár …',hr:'Vaš komentar …',pl:'Twój komentarz …',es:'Su comentario …',it:'Il tuo commento …',fr:'Votre commentaire …',sv:'Din kommentar …'},
    send:{de:'Kommentar absenden',en:'Send comment',sk:'Odoslať komentár',hr:'Pošalji komentar',pl:'Wyślij komentarz',es:'Enviar comentario',it:'Invia commento',fr:'Envoyer',sv:'Skicka kommentar'},
    sent:{de:'Danke. Ihr Kommentar erscheint nach Freigabe durch den Administrator.',en:'Thanks. Your comment will appear after admin approval.',sk:'Ďakujeme. Komentár sa zobrazí po schválení administrátorom.',hr:'Hvala. Komentar će se prikazati nakon odobrenja administratora.',pl:'Dziękujemy. Komentarz pojawi się po zatwierdzeniu przez administratora.',es:'Gracias. Su comentario aparecerá tras la aprobación del administrador.',it:'Grazie. Il commento apparirà dopo l’approvazione dell’amministratore.',fr:'Merci. Votre commentaire apparaîtra après validation de l’administrateur.',sv:'Tack. Din kommentar visas efter administratörens godkännande.'},
    empty:{de:'Noch keine freigegebenen Kommentare. Seien Sie der Erste.',en:'No approved comments yet. Be the first.',sk:'Zatiaľ žiadne schválené komentáre. Buďte prvý.',hr:'Još nema odobrenih komentara. Budite prvi.',pl:'Brak zatwierdzonych komentarzy. Bądź pierwszy.',es:'Aún no hay comentarios aprobados. Sé el primero.',it:'Ancora nessun commento approvato. Sii il primo.',fr:'Pas encore de commentaires approuvés. Soyez le premier.',sv:'Inga godkända kommentarer ännu. Bli först.'},
    tip:{de:'Kommentare sind öffentlich, werden jedoch erst nach Freigabe durch den Administrator angezeigt. Grund: Schutz vor verleumderischen Kommentaren der Gegenseite über fiktive/Fake-Konten.',en:'Comments are public but appear only after administrator approval. Reason: protection against defamatory comments by the opposing party via fake accounts.',sk:'Komentáre sú verejné, no zobrazia sa až po schválení administrátorom. Dôvod: ochrana pred hanlivými komentármi protistrany z fiktívnych/falošných účtov.',hr:'Komentari su javni, ali se prikazuju tek nakon odobrenja administratora. Razlog: zaštita od klevetničkih komentara protivne strane putem lažnih računa.',pl:'Komentarze są publiczne, ale pojawiają się dopiero po zatwierdzeniu przez administratora. Powód: ochrona przed zniesławiającymi komentarzami strony przeciwnej z fałszywych kont.',es:'Los comentarios son públicos pero aparecen solo tras la aprobación del administrador. Motivo: protección frente a comentarios difamatorios de la parte contraria mediante cuentas falsas.',it:'I commenti sono pubblici ma appaiono solo dopo l’approvazione dell’amministratore. Motivo: protezione da commenti diffamatori della controparte tramite account falsi.',fr:'Les commentaires sont publics mais n’apparaissent qu’après validation de l’administrateur. Raison : protection contre les commentaires diffamatoires de la partie adverse via de faux comptes.',sv:'Kommentarer är offentliga men visas först efter administratörens godkännande. Skäl: skydd mot ärekränkande kommentarer från motparten via falska konton.'}
  };
  function lang(){ var r=document.querySelector('input[id^="klng-"]:checked'); return (r&&r.id.slice(5))||'de'; }
  function t(k){ return (S[k]&&(S[k][lang()]||S[k].de))||''; }
  function esc(s){ return (s||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];}); }
  function all(sel,ctx){ return [].slice.call((ctx||document).querySelectorAll(sel)); }

  var OFFICIAL=['FIA FOX'];
  var idCache={};
  function resolveId(slug){
    if(idCache[slug]!==undefined) return Promise.resolve(idCache[slug]);
    return fetch(REST+'/posts?slug='+encodeURIComponent(slug)+'&_fields=id')
      .then(function(r){return r.json();})
      .then(function(j){ var id=(j&&j[0]&&j[0].id)||null; idCache[slug]=id; return id; })
      .catch(function(){ idCache[slug]=null; return null; });
  }
  function fetchComments(id){
    return fetch(REST+'/comments?post='+id+'&per_page=100&order=asc&_fields=id,author,author_name,date,content,author_avatar_urls')
      .then(function(r){return r.json();}).catch(function(){return [];});
  }
  function fmtDate(s){ try{ return new Date(s).toLocaleDateString(lang()); }catch(e){ return ''; } }
  function setCount(slug,n){ all('.ccount[data-doc="'+slug+'"]').forEach(function(el){ el.textContent=n; }); }

  function renderList(box,comments){
    if(!comments||!comments.length){ box.innerHTML='<div class="cmt-empty">'+esc(t('empty'))+'</div>'; return; }
    box.innerHTML=comments.map(function(c){
      var body=(c.content&&c.content.rendered)||'';
      var au=c.author_avatar_urls||{};
      var av=au['96']||au['48']||au['24']||'';
      var avh=av?'<img class="cmt-av" src="'+esc(av)+'" alt="" width="36" height="36" loading="lazy" referrerpolicy="no-referrer">':'<span class="cmt-av"></span>';
      var off=(c.author&&c.author>0)||OFFICIAL.indexOf((c.author_name||'').trim())>-1;
      return '<div class="cmt-i">'+avh+'<div class="cmt-c"><div class="cmt-h"><b class="cmt-name'+(off?' cmt-off':'')+'">'+esc(c.author_name||'Anonym')+'</b> · '+esc(fmtDate(c.date))+'</div><div class="cmt-b">'+body+'</div></div></div>';
    }).join('');
  }

  function buildPanel(slug){
    var p=document.createElement('div'); p.className='cmt-panel';
    p.innerHTML=
      '<div class="cmt-head">💬 <span class="cmt-ttl"></span> <span class="cmt-mod"></span></div>'+
      '<div class="cmt-list">…</div>'+
      '<div class="cmt-flash" style="display:none"></div>'+
      '<form class="cmt-form" novalidate>'+
        '<div class="cmt-row">'+
          '<input class="cmt-name" type="text" autocomplete="off">'+
          '<input class="cmt-mail" type="email" autocomplete="off">'+
        '</div>'+
        '<textarea class="cmt-body" rows="3"></textarea>'+
        '<input class="cmt-hp" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">'+
        '<div class="cmt-act"><button type="submit" class="cmt-send"></button></div>'+
      '</form>';
    function relabel(){
      p.querySelector('.cmt-ttl').textContent=t('title');
      p.querySelector('.cmt-mod').textContent='🔒 '+t('mod');
      p.querySelector('.cmt-name').placeholder=t('name');
      p.querySelector('.cmt-mail').placeholder=t('email');
      p.querySelector('.cmt-body').placeholder=t('body');
      p.querySelector('.cmt-send').textContent=t('send');
    }
    relabel(); p._relabel=relabel;
    var listEl=p.querySelector('.cmt-list'), flash=p.querySelector('.cmt-flash');
    resolveId(slug).then(function(id){
      if(!id){ listEl.innerHTML='<div class="cmt-empty">—</div>'; return; }
      p._pid=id;
      fetchComments(id).then(function(cs){ renderList(listEl,cs); setCount(slug,cs.length); });
    });
    p.querySelector('.cmt-form').addEventListener('submit',function(e){
      e.preventDefault();
      if(p.querySelector('.cmt-hp').value){ return; }            /* honeypot */
      var name=p.querySelector('.cmt-name').value.trim()||'Anonym';
      var mail=p.querySelector('.cmt-mail').value.trim();
      var body=p.querySelector('.cmt-body').value.trim();
      if(!body||!p._pid){ return; }
      var fd=new FormData();
      fd.append('comment_post_ID',p._pid);
      fd.append('author',name);
      fd.append('email',mail||'anonym@foxprof.club');
      fd.append('comment',body);
      var btn=p.querySelector('.cmt-send'); btn.disabled=true;
      fetch(POST_EP,{method:'POST',body:fd,credentials:'same-origin'})
        .then(function(){})
        .catch(function(){})
        .then(function(){
          p.querySelector('.cmt-body').value='';
          flash.textContent='✅ '+t('sent'); flash.style.display='block';
          setTimeout(function(){ flash.style.display='none'; },9000);
          btn.disabled=false;
        });
    });
    return p;
  }

  function wire(a){
    var slug=a.getAttribute('data-doc'); if(!slug) return;
    var wrap=document.querySelector('.cmt-wrap[data-doc="'+slug+'"]'); if(!wrap) return;
    a.addEventListener('click',function(e){
      e.preventDefault();
      if(wrap._panel){ wrap._panel.style.display=(wrap._panel.style.display==='none'?'block':'none'); return; }
      var p=buildPanel(slug); p.style.display='block'; wrap.appendChild(p); wrap._panel=p;
    });
    if(!a._tipEl){
      var tp=document.createElement('span'); tp.className='ktip'; tp.textContent=t('tip');
      a.parentNode.insertBefore(tp,a.nextSibling); a._tipEl=tp;
    }
  }

  function relangAll(){
    all('.kcmt').forEach(function(a){ if(a._tipEl) a._tipEl.textContent=t('tip'); });
    all('.cmt-wrap').forEach(function(w){ if(w._panel&&w._panel._relabel) w._panel._relabel(); });
  }

  function injectPilot(){
    if(document.querySelector('.kcmt[data-doc="cmt-pilot-m10815"]')) return; /* už je v markupe */
    var item=document.querySelector('#case-m10815 .comm .col .item');
    if(!item) return;
    var ph=document.createElement('div');
    ph.style.marginTop='8px';
    ph.innerHTML='<a class="kcmt" data-doc="cmt-pilot-m10815" href="#">'+
      '<span class="gtl de">💬 Kommentieren</span><span class="gtl en">💬 Comment</span><span class="gtl sk">💬 Komentovať</span><span class="gtl hr">💬 Komentiraj</span><span class="gtl pl">💬 Skomentuj</span><span class="gtl es">💬 Comentar</span><span class="gtl it">💬 Commenta</span><span class="gtl fr">💬 Commenter</span><span class="gtl sv">💬 Kommentera</span>'+
      ' (<span class="ccount" data-doc="cmt-pilot-m10815">0</span>)</a>'+
      '<div class="cmt-wrap" data-doc="cmt-pilot-m10815"></div>';
    item.appendChild(ph);
  }

  function init(){
    injectPilot();
    all('.kcmt[data-doc]').forEach(wire);
    var wraps=all('.cmt-wrap[data-doc]');
    (function next(){
      var w=wraps.shift(); if(!w) return;
      var slug=w.getAttribute('data-doc');
      resolveId(slug).then(function(id){
        if(id){ fetchComments(id).then(function(cs){ setCount(slug,cs.length); next(); }); }
        else next();
      });
    })();
    all('input[id^="klng-"]').forEach(function(r){ r.addEventListener('change',relangAll); });
  }
  if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',init); } else { init(); }
})();

/* ===== FIA FOX — kauzy.js · ČASŤ 4: jazykový langbar (#fia-langbar) =====
   Samostatný sticky pruh PRED #fia-kauzy: vľavo tlačidlo Domov (9 jazykov),
   vpravo 9 vlajok. Keďže langbar je iný blok než #fia-kauzy, CSS selektor
   #klng-XX:checked ~ ... naň nedosiahne — preto sa rieši týmto JS:
   - klik vlajky .lbf[data-lang] → nastaví zdieľané #klng-XX (checked) + dispatch 'change'
     (to prepne legacy karty v #fia-kauzy aj register #fia-reg cez ich vlastné listenery),
     rozsvieti aktívnu vlajku a prepne triedu #fia-langbar.lang-XX (zobrazí text Domov v danom jazyku).
   - počúva 'change' na #klng-XX (zmena cez register alebo legacy vlajky) a drží langbar v sync.
*/
(function () {
  var LANGS = ['de','en','sk','hr','pl','es','it','fr','sv'];

  function init() {
    var bar = document.getElementById('fia-langbar');
    if (!bar) return;
    var btns = [].slice.call(bar.querySelectorAll('.lbf[data-lang]'));

    function curChecked() {
      for (var i = 0; i < LANGS.length; i++) {
        var r = document.getElementById('klng-' + LANGS[i]);
        if (r && r.checked) return LANGS[i];
      }
      return 'de';
    }
    function setActive(L) {
      btns.forEach(function (b) { b.classList.toggle('active', b.getAttribute('data-lang') === L); });
      LANGS.forEach(function (x) { bar.classList.toggle('lang-' + x, x === L); });
    }

    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var L = b.getAttribute('data-lang');
        var r = document.getElementById('klng-' + L);
        if (r) { r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true })); }
        setActive(L);
      });
    });

    LANGS.forEach(function (x) {
      var r = document.getElementById('klng-' + x);
      if (r) r.addEventListener('change', function () { setActive(curChecked()); });
    });

    setActive(curChecked());
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* fia-thread-highlight — zvyraznenie vlakna odpovede (klik/hover na .thr alebo .replyto) */
(function(){
  function items(t){ return document.querySelectorAll('#fia-kauzy .item[data-thread="'+t+'"]'); }
  function setHl(t,on){ [].forEach.call(items(t),function(e){ e.classList.toggle('thr-hl',on); }); }
  function tOf(el){
    var it = el.closest ? el.closest('.item[data-thread]') : null;
    return it ? it.getAttribute('data-thread') : null;
  }
  document.addEventListener('mouseover', function(ev){
    var h = ev.target.closest ? ev.target.closest('#fia-kauzy .thr, #fia-kauzy .replyto') : null;
    if(!h) return; var t=tOf(h); if(t) setHl(t,true);
  });
  document.addEventListener('mouseout', function(ev){
    var h = ev.target.closest ? ev.target.closest('#fia-kauzy .thr, #fia-kauzy .replyto') : null;
    if(!h) return; var t=tOf(h); if(t) setHl(t,false);
  });
  document.addEventListener('click', function(ev){
    var h = ev.target.closest ? ev.target.closest('#fia-kauzy .thr, #fia-kauzy .replyto') : null;
    if(!h) return; var t=tOf(h); if(!t) return;
    ev.preventDefault();
    var all=items(t); if(!all.length) return;
    [].forEach.call(all,function(e){ e.classList.add('thr-hl'); });
    var self=h.closest('.item'); var partner=null;
    [].forEach.call(all,function(e){ if(e!==self) partner=e; });
    if(partner){ partner.scrollIntoView({behavior:'smooth',block:'center'}); }
    setTimeout(function(){ [].forEach.call(all,function(e){ e.classList.remove('thr-hl'); }); }, 2600);
  });
})();
