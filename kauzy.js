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
