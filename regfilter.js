/* FIA FOX — regfilter.js  (#303)
   Filtrovanie spodnych kariet podla klikuteho register-tlacidla (.rbtn v #fia-reg).
   Spaja DVA kontajnery kariet:
     - realne karty: #fia-kauzy .cases > details.case   (id = case-m10815 / case-dgcomp / case-telekom ...)
     - testovacie:   #fia-testcases > details.case       (id = case-test-* / case-mstest)
   Zdroj prislusnosti tlacidla ku kartam:
     - data-ids   na .rbtn  (medzerou oddelene id kariet; napr. "case-m10815 case-dgcomp case-telekom")
     - data-spis  na .rbtn  -> MAP na jednu testovaciu kartu (fallback, ak data-ids prazdne)
   Spravanie:
     - na starte: VSETKY karty viditelne
     - klik na .rbtn: zobraz LEN karty daneho tlacidla, ostatne skry
     - klik na uz aktivne tlacidlo (alebo ked nic nie je aktivne): RESET = ukaz vsetko
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

    function showAll() {
      allCards().forEach(function (c) { c.style.display = ""; });
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
          // druhy klik na aktivne = reset
          activeBtn = null;
          showAll();
          return;
        }
        activeBtn = b;
        showOnly(idsFor(b));
      });
    });

    // start: vsetko viditelne
    showAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
