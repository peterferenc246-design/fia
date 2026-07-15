/* FIA FOX — langpersist.js — jazykova perzistencia REGISTRA #303 (foxprof.club)
   Doplnok k WPCode kauzy.js: NEDUPLIKUJE filter/sort/share/komentare.
   Dopredny smer: register pri nacitani prevezme jazyk podla stranky, z ktorej sa prislo
   (Polylang prefix /sk/ /en/ ...). Poradie: ?lang=XX -> referrer -> localStorage 'fiaLang' -> DE.
   Klik na vlajku v registri si volbu zapamata.
   DOLEZITE: odkaz "Domov" (.lbhome) sa UMYSELNE NEPREPISUJE — vzdy vedie na DE domovsku
   stranku (kampan je primarne DE), aby home nenaskakoval v inom jazyku.
*/
(function () {
  var LANGS = ['de','en','sk','hr','pl','es','it','fr','sv'];
  function ok(L){ return L && LANGS.indexOf(L) >= 0; }
  function store(L){ try { localStorage.setItem('fiaLang', L); } catch (e) {} }
  function stored(){ try { var v = localStorage.getItem('fiaLang'); return ok(v) ? v : null; } catch (e) { return null; } }
  function fromQuery(){
    var m = (location.search + location.hash).match(/[?&#]lang=([A-Za-z]{2})/);
    var L = m && m[1].toLowerCase();
    return ok(L) ? L : null;
  }
  function fromReferrer(){
    try {
      if (!document.referrer) return null;
      var u = new URL(document.referrer);
      if (u.hostname !== location.hostname) return null;
      if (u.pathname === location.pathname) return null;
      var seg = (u.pathname.split('/').filter(Boolean)[0] || '').toLowerCase();
      if (ok(seg) && seg !== 'de') return seg;
      return 'de';
    } catch (e) { return null; }
  }
  function detect(){ return fromQuery() || fromReferrer() || stored() || 'de'; }
  function cur(){
    for (var i = 0; i < LANGS.length; i++) { var r = document.getElementById('klng-' + LANGS[i]); if (r && r.checked) return LANGS[i]; }
    return 'de';
  }
  function paintBar(L){
    var bar = document.getElementById('fia-langbar');
    if (!bar) return;
    LANGS.forEach(function (x) { bar.classList.toggle('lang-' + x, x === L); });
    [].forEach.call(bar.querySelectorAll('.lbf'), function (b) { b.classList.toggle('active', b.getAttribute('data-lang') === L); });
    /* .lbhome href sa zamerne NEMENI — Domov vzdy DE */
  }
  function apply(L){
    if (!ok(L)) L = 'de';
    var r = document.getElementById('klng-' + L);
    if (r && !r.checked) { r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true })); }
    paintBar(L); store(L);
  }
  function bind(){
    LANGS.forEach(function (x) {
      var r = document.getElementById('klng-' + x);
      if (r) r.addEventListener('change', function () { var c = cur(); paintBar(c); store(c); });
    });
    apply(detect());
  }
  function boot(){ setTimeout(bind, 90); }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', boot); } else { boot(); }
})();
