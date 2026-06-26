/* FIA FOX — kauzy.js
   Filter (chipy) + triedenie (sortbar) pre register kauz #303 foxprof.club
   Jazykovo nezávislý: číta výhradne data-* atribúty na <details class="case">.
   - chipy:   data-filter  (all | eu | de | sk | kartell | gdpr | strafrecht)
   - karty:   data-cat (jurisdikcia: eu/de/sk) + data-area (oblasť: kartell/gdpr/strafrecht)
              data-date (ISO YYYY-MM-DD) · data-az · data-ourref
   - sortbar: .sortbtn[data-sort]  (date | az | ourref | area)
   - smer:    #kdir  data-dir (desc = najnovšie hore, asc = najstaršie hore)
   Prázdne hodnoty (data-az="", data-ourref="") idú vždy na koniec.
*/
(function () {
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

    function applyFilter() {
      cases.forEach(function (c) {
        var f = state.filter;
        var show = f === 'all'
                || attr(c, 'cat')  === f
                || attr(c, 'area') === f;
        c.classList.toggle('hide', !show);
      });
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
        var tn = dirBtn.firstChild;                 // textový uzol s ikonou "⬇ " / "⬆ "
        if (tn && tn.nodeType === 3) {
          tn.nodeValue = (state.dir === 'desc' ? '\u2b07 ' : '\u2b06 ');
        }
        applySort();
      });
    }

    applyFilter();
    applySort();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
