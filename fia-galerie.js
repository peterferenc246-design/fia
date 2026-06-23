/* FIA FOX — Galerie  (fia-galerie.js)
   Prepínanie jazyka (vlajky), zobrazenie mriežka/zoznam, triedenie, filtre, lightbox.
   Všetko v rámci #fia-galerie. Žiadne externé závislosti. */
(function () {
  function init() {
    var root = document.getElementById('fia-galerie');
    if (!root) return;

    /* ---------- JAZYK ---------- */
    var LS = 'fiaLang';
    function curLang() {
      var s = '';
      try { s = localStorage.getItem(LS) || ''; } catch (e) {}
      if (!s) {
        var r = root.querySelector('.glngradio:checked');
        s = r ? r.id.replace('glng-', '') : 'de';
      }
      return s;
    }
    // preklady volieb triedenia (option nemoze mat .gtl spany)
    var SORT_I18N = {
      date:  {de:'Datum',en:'Date',sk:'Dátum',hr:'Datum',pl:'Data',es:'Fecha',it:'Data',fr:'Date',sv:'Datum'},
      title: {de:'Titel',en:'Title',sk:'Názov',hr:'Naslov',pl:'Tytuł',es:'Título',it:'Titolo',fr:'Titre',sv:'Titel'},
      cat:   {de:'Kategorie',en:'Category',sk:'Kategória',hr:'Kategorija',pl:'Kategoria',es:'Categoría',it:'Categoria',fr:'Catégorie',sv:'Kategori'}
    };
    function applyLang(lang) {
      // prepni radio
      var inp = root.querySelector('#glng-' + lang);
      if (inp) inp.checked = true;
      // .gtl spany
      root.querySelectorAll('.gtl').forEach(function (e) { e.style.display = 'none'; });
      root.querySelectorAll('.gtl.' + lang).forEach(function (e) { e.style.display = ''; });
      // rozbalovacka triedenia
      root.querySelectorAll('.gsortsel option').forEach(function (op) {
        var key = op.value, map = SORT_I18N[key];
        if (map && map[lang]) op.textContent = map[lang];
      });
      try { localStorage.setItem(LS, lang); } catch (e) {}
    }
    root.querySelectorAll('label.gflag').forEach(function (lab) {
      lab.addEventListener('click', function () {
        applyLang(lab.getAttribute('data-lang'));
      });
    });

    /* ---------- ZOBRAZENIE mriežka/zoznam ---------- */
    var grid = root.querySelector('.gitems');
    root.querySelectorAll('.gview-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute('data-view');
        root.querySelectorAll('.gview-btn').forEach(function (x) { x.classList.remove('active'); });
        b.classList.add('active');
        if (grid) { grid.classList.toggle('list', v === 'list'); grid.classList.toggle('grid', v === 'grid'); }
      });
    });

    /* ---------- FILTRE ---------- */
    root.querySelectorAll('.gchip').forEach(function (c) {
      c.addEventListener('click', function () {
        var cat = c.getAttribute('data-cat');
        root.querySelectorAll('.gchip').forEach(function (x) { x.classList.remove('active'); });
        c.classList.add('active');
        root.querySelectorAll('.gcard').forEach(function (card) {
          var show = (cat === 'all') || (card.getAttribute('data-cat') === cat);
          card.style.display = show ? '' : 'none';
        });
      });
    });

    /* ---------- TRIEDENIE ---------- */
    var sortSel = root.querySelector('.gsortsel');
    if (sortSel && grid) {
      sortSel.addEventListener('change', function () {
        var mode = sortSel.value;
        var cards = Array.prototype.slice.call(grid.querySelectorAll('.gcard'));
        cards.sort(function (a, b) {
          if (mode === 'title') return (a.getAttribute('data-title') || '').localeCompare(b.getAttribute('data-title') || '');
          if (mode === 'cat') return (a.getAttribute('data-cat') || '').localeCompare(b.getAttribute('data-cat') || '');
          // date (default) — najnovšie hore
          return (b.getAttribute('data-date') || '').localeCompare(a.getAttribute('data-date') || '');
        });
        cards.forEach(function (c) { grid.appendChild(c); });
      });
    }

    /* ---------- LIGHTBOX ---------- */
    var lb = root.querySelector('.glightbox');
    var lbImg = root.querySelector('.glightbox img');
    if (lb && lbImg) {
      root.querySelectorAll('.gcard .gthumb').forEach(function (th) {
        th.addEventListener('click', function () {
          var src = th.getAttribute('data-full') || th.getAttribute('src');
          lbImg.src = src;
          lb.classList.add('open');
        });
      });
      lb.addEventListener('click', function () { lb.classList.remove('open'); lbImg.src = ''; });
    }

    /* ---------- KOPÍROVANIE odkazu obrázka ---------- */
    root.querySelectorAll('.gcopy').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var url = btn.getAttribute('data-url') || '';
        if (navigator.clipboard && url) {
          navigator.clipboard.writeText(url).then(function () {
            var old = btn.textContent;
            btn.textContent = '✓';
            setTimeout(function () { btn.textContent = old; }, 1200);
          });
        }
      });
    });

    applyLang(curLang());
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
