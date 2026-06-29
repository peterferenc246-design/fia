/* FIA FOX — regfilter.js  (#303)
   Filtrovanie spodnych kariet podla klikuteho register-tlacidla (.rbtn v #fia-reg).
   Spaja DVA kontajnery kariet:
     - realne karty: #fia-kauzy .cases > details.case   (id = case-m10815 / case-dgcomp / case-telekom ...)
     - testovacie:   #fia-testcases > details.case       (id = case-test-* / case-mstest)
   Zdroj prislusnosti tlacidla ku kartam:
     - data-ids   na .rbtn  (medzerou oddelene id kariet; napr. "case-m10815 case-dgcomp case-telekom")
     - data-spis  na .rbtn  -> MAP na jednu testovaciu kartu (fallback, ak data-ids prazdne)
   Spravanie:
     - na starte: ZIADNE karty viditelne (kym sa neklikne register-tlacidlo)
     - klik na .rbtn: zobraz LEN karty daneho tlacidla, ostatne skry
     - klik na uz aktivne tlacidlo: RESET = skry vsetko
   Externy subor cez jsDelivr — obchadza WP.com entity-enkodovanie inline <script>.
   Bez logickeho operatora v kode (drzime pravidlo: WP.com ho v inline scripte meni na entity a rozbije ho). */
(function () {
  var MAP = {
    "TCFIA-2026-FON-008": ["case-test-fon"],
    "LRA-2026-BG-000":    ["case-test-lra"],
    "PER-DE-2026-INS-005":["case-test-ins"],
    "PR-2026-EXS-026":    ["case-test-exs"],
    "PR-2026-VsZ-006":    ["case-test-vszp"],
    "PIF-EU-2026-MBS-004":["case-mstest"],
    "PER-DE-2026-DAK-":   ["case-test-dak"]
  };

  function init() {
    var reg = document.getElementById("fia-reg");
    if (!reg) { return; }
    var kauzy = document.getElementById("fia-kauzy");
    var tc    = document.getElementById("fia-testcases");

    // PRESUN: testovacie karty pod riadok ZORADIŤ — vlož #fia-testcases do #fia-kauzy
    // hneď ZA .cases, aby sa konania VŠETKÝCH kaúz zobrazovali na rovnakom mieste
    // (pod sortbarom) ako reálne karty. Mimo .cases => kauzy.js triedenie sa ich nedotkne.
    if (tc) { if (kauzy) {
      var casesBox = kauzy.querySelector(".cases");
      if (casesBox) { if (casesBox.parentNode) {
        casesBox.parentNode.insertBefore(tc, casesBox.nextSibling);
      } }
    } }

    // --- MULTIJAZYK TESTKARIET ---
    // Titul sa klonuje priamo z register-tlacidla (.rbtn .rt .gtl) — vzdy v sulade s registrom.
    // Meta + poznamka zo zdielanej 9-jazycnej tabulky. Prepinanie: trieda .lang-XX na
    // #fia-testcases (rovnaky osvedceny vzor ako register.js pre #fia-reg) — bez :has.
    if (tc) {
      var L9 = ["de","en","sk","hr","pl","es","it","fr","sv"];
      var ML_META = ["Testkarte · Verdrahtungstest","Test card · wiring check","Testovacia karta · kontrola napojenia","Testna kartica · provjera povezivanja","Karta testowa · test podłączenia","Tarjeta de prueba · verificación de conexión","Scheda di test · verifica collegamento","Carte de test · vérification du câblage","Testkort · kopplingstest"];
      var ML_NOTE = ["Vorübergehende Testkarte. Die tatsächlichen Verfahren werden über das x5-Formular ergänzt.","Temporary test card. The actual proceedings will be added via the x5 form.","Dočasná testovacia karta. Skutočné konania sa doplnia cez formulár x5.","Privremena testna kartica. Stvarni postupci dodat će se putem obrasca x5.","Tymczasowa karta testowa. Rzeczywiste postępowania zostaną dodane przez formularz x5.","Tarjeta de prueba temporal. Los procedimientos reales se añadirán mediante el formulario x5.","Scheda di test temporanea. I procedimenti effettivi saranno aggiunti tramite il modulo x5.","Carte de test temporaire. Les procédures réelles seront ajoutées via le formulaire x5.","Tillfälligt testkort. De faktiska förfarandena läggs till via x5-formuläret."];
      function wrap9(arr) {
        var out = "";
        for (var i = 0; i < L9.length; i++) { out += '<span class="gtl ' + L9[i] + '">' + arr[i] + '</span>'; }
        return out;
      }
      // jazykove CSS cez triedu .lang-XX na #fia-testcases (rovnaky vzor ako register.js)
      var st = document.createElement("style");
      var css = "#fia-testcases .gtl{display:none}";
      L9.forEach(function (x) { css += "#fia-testcases.lang-" + x + " .gtl." + x + "{display:inline}"; });
      st.textContent = css;
      document.head.appendChild(st);
      // naplnenie kazdej testkarty podla prislusneho register-tlacidla
      [].slice.call(reg.querySelectorAll(".rbtn")).forEach(function (b) {
        var ids = [];
        var di = (b.getAttribute("data-ids") || "").split(/\s+/);
        di.forEach(function (x) { if (x) { ids.push(x); } });
        if (ids.length === 0) {
          var sp0 = b.getAttribute("data-spis") || "";
          if (MAP[sp0]) { MAP[sp0].forEach(function (x) { ids.push(x); }); }
        }
        ids.forEach(function (id) {
          var card = tc.querySelector("#" + id);
          if (!card) { return; }
          var rt = b.querySelector(".rt");
          var titleEl = card.querySelector(".tc-title");
          var metaEl  = card.querySelector(".tc-meta");
          var noteEl  = card.querySelector(".tc-note");
          if (titleEl) {
            if (rt) {
              var ts = "";
              [].slice.call(rt.querySelectorAll(".gtl")).forEach(function (g) { ts += g.outerHTML; });
              titleEl.innerHTML = "🧪 " + ts;
            }
          }
          var sp = b.getAttribute("data-spis") || "";
          if (metaEl) { metaEl.innerHTML = wrap9(ML_META) + " · spis " + sp; }
          if (noteEl) { noteEl.innerHTML = wrap9(ML_NOTE); }
        });
      });
      // prepinanie jazyka testkariet: trieda .lang-XX podla zaskrtnuteho klng radia
      function curLang9() { for (var i = 0; i < L9.length; i++) { var r = document.getElementById("klng-" + L9[i]); if (r) { if (r.checked) { return L9[i]; } } } return "de"; }
      function setTC() { var c = curLang9(); L9.forEach(function (x) { tc.classList.toggle("lang-" + x, x === c); }); }
      L9.forEach(function (x) { var r = document.getElementById("klng-" + x); if (r) { r.addEventListener("change", setTC); } });
      var lbar = document.getElementById("fia-langbar");
      if (lbar) { [].slice.call(lbar.querySelectorAll(".lbf")).forEach(function (fb) { fb.addEventListener("click", function () { setTimeout(setTC, 0); }); }); }
      setTC();
    }

    function allCards() {
      var out = [];
      if (kauzy) {
        var w = kauzy.querySelector(".cases");
        if (w) { [].slice.call(w.querySelectorAll("details.case")).forEach(function (c) { out.push(c); }); }
      }
      if (tc) {
        [].slice.call(tc.querySelectorAll("details.case")).forEach(function (c) { out.push(c); });
      }
      return out;
    }

    function idsFor(btn) {
      var ids = [];
      var di = (btn.getAttribute("data-ids") || "").split(/\s+/);
      di.forEach(function (x) { if (x) { ids.push(x); } });
      if (ids.length === 0) {
        var sp = btn.getAttribute("data-spis") || "";
        if (MAP[sp]) { MAP[sp].forEach(function (x) { ids.push(x); }); }
      }
      return ids;
    }

    function showOnly(ids) {
      var set = {};
      ids.forEach(function (x) { set[x] = true; });
      allCards().forEach(function (c) {
        if (set[c.id]) { c.style.display = ""; }
        else { c.style.display = "none"; }
      });
    }

    var rbtns = [].slice.call(reg.querySelectorAll(".rbtn"));
    var activeBtn = null;

    rbtns.forEach(function (b) {
      b.addEventListener("click", function () {
        if (activeBtn === b) {
          // druhy klik na aktivne = reset (skry vsetko)
          activeBtn = null;
          showOnly([]);
          return;
        }
        activeBtn = b;
        showOnly(idsFor(b));
      });
    });

    // start: nic viditelne, kym sa neklikne kauza v registri
    showOnly([]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
