/* FIA FOX — langpersist.js — jazykova perzistencia registra #303 (foxprof.club)
   Doplnok k WPCode kauzy.js: NEDUPLIKUJE filter/sort/share/komentare.
   Riesi len:
   - pri nacitani rozpozna jazyk: ?lang=XX -> jazyk odkazujucej stranky (Polylang prefix
     /sk/ /en/ ...; bez prefixu = DE; reload tej istej stranky sa ignoruje) -> localStorage 'fiaLang' -> DE
   - pocuva zmenu #klng (klik vlajky) -> ulozi volbu a prepise odkaz Domov (.lbhome) na jazykovu URL
   Bezi az po dobehnuti footer skriptov (male oneskorenie), aby prebilo default DE.
*/
(function () {
  var LANGS = ['de','en','sk','hr','pl','es','it','fr','sv'];
  var HOME = {
    de:'https://foxprof.club/',
    en:'https://foxprof.club/en/welcome/',
    sk:'https://foxprof.club/sk/164-2/',
    hr:'https://foxprof.club/hr/dobrodosli/',
    pl:'https://foxprof.club/pl/witamy/',
    es:'https://foxprof.club/es/bienvenidos/',
    it:'https://foxprof.club/it/benvenuti/',
    fr:'https://foxprof.club/fr/bienvenue/',
    sv:'https://foxprof.club/sv/209-2/'
  };
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
  function paint(L){
    var bar = document.getElementById('fia-langbar');
    if (!bar) return;
    LANGS.forEach(function (x) { bar.classList.toggle('lang-' + x, x === L); });
    [].forEach.call(bar.querySelectorAll('.lbf'), function (b) { b.classList.toggle('active', b.getAttribute('data-lang') === L); });
    var h = bar.querySelector('.lbhome'); if (h && HOME[L]) h.setAttribute('href', HOME[L]);
  }
  function apply(L){
    if (!ok(L)) L = 'de';
    var r = document.getElementById('klng-' + L);
    if (r && !r.checked) { r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true })); }
    paint(L); store(L);
  }
  function bind(){
    LANGS.forEach(function (x) {
      var r = document.getElementById('klng-' + x);
      if (r) r.addEventListener('change', function () { var c = cur(); paint(c); store(c); });
    });
    apply(detect());
  }
  function boot(){ setTimeout(bind, 90); }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', boot); } else { boot(); }
})();
