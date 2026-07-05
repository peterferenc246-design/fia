/* FIA FOX — register.js  (#303 #fia-reg)
   Jazyk (titul/tlačidlá) + jurisdikčný filter vlajok DE/SK/EU.
   Externý súbor cez jsDelivr — obchádza WP.com entity-enkódovanie inline <script> (&& -> &#038;).
   Karty zobrazuje samostatný fia-testcases skript cez data-spis; tu sa kartami nezaoberáme. */
(function () {
  function init() {
    var reg = document.getElementById('fia-reg');
    if (!reg) { return; }
    var LANGS = ['de','en','sk','hr','pl','es','it','fr','sv'];

    function curLang() {
      for (var i = 0; i < LANGS.length; i++) {
        var r = document.getElementById('klng-' + LANGS[i]);
        if (r) { if (r.checked) { return LANGS[i]; } }
      }
      return 'de';
    }
    function setLang() {
      var L = curLang();
      LANGS.forEach(function (x) { reg.classList.toggle('lang-' + x, x === L); });
    }
    LANGS.forEach(function (x) {
      var r = document.getElementById('klng-' + x);
      if (r) { r.addEventListener('change', setLang); }
    });
    setLang();

    var jbtns = reg.querySelectorAll('.jbtn');
    var jall  = reg.querySelector('.jall');
    var rbtns = reg.querySelectorAll('.rbtn');
    var curJur = '__all__';

    function jurMatch(el) {
      if (curJur === '__all__') { return true; }
      var js = (el.getAttribute('data-jur') || '').split(/\s+/).filter(Boolean);
      return js.indexOf(curJur) !== -1;
    }
    function syncJur() {
      jbtns.forEach(function (b) { b.classList.toggle('active', curJur === b.getAttribute('data-jur')); });
      if (jall) { jall.classList.toggle('active', curJur === '__all__'); }
      rbtns.forEach(function (b) { b.classList.toggle('hide', !jurMatch(b)); });
    }

    jbtns.forEach(function (b) {
      b.addEventListener('click', function () { curJur = b.getAttribute('data-jur'); syncJur(); });
    });
    if (jall) {
      jall.addEventListener('click', function () { curJur = '__all__'; syncJur(); });
    }
    rbtns.forEach(function (b) {
      b.addEventListener('click', function () {
        rbtns.forEach(function (x) { x.classList.toggle('active', x === b); });
        // NOVÉ: informuj všetky iframe (x5 formular) o kliku na dlaždicu — spis rieši mapovanie
        var sp = b.getAttribute('data-spis');
        if (sp) {
          var frames = document.querySelectorAll('iframe');
          for (var i = 0; i < frames.length; i++) {
            try { frames[i].contentWindow.postMessage({type:'fiafox-registerclick', spis:sp}, '*'); } catch (e) {}
          }
        }
      });
    });

    syncJur();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
