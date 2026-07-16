/* FIA FOX — cardedit.js
   ✏️ tlačidlá na položkách registra #303 (LEN prihlásený admin). */
(function () {
  var LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"];
  function txt(el){ return el ? el.textContent.trim() : ""; }
  function buildSnapFromDom(item){
    var caseEl = item.closest("details.case");
    var titleDe = caseEl ? caseEl.querySelector(".case-title .gtl.de") : null;
    var kauza = titleDe ? titleDe.textContent.trim() : (caseEl ? (caseEl.id||"") : "");
    var dir = "sent";
    var col = item.closest(".col");
    if (col && col.parentNode){
      var cols = col.parentNode.querySelectorAll(":scope > .col");
      if (cols.length>1 && cols[1]===col){ dir="recv"; }
    }
    var subj = "";
    var subjEl = item.querySelector(".subj");
    if (subjEl){
      var clone = subjEl.cloneNode(true);
      var imp = clone.querySelector(".impx");
      if (imp){ imp.parentNode.removeChild(imp); }
      var _sk = subjEl.querySelector(".gtl.sk") || subjEl.querySelector(".gtl"); subj = _sk ? _sk.textContent.trim() : clone.textContent.trim();
    }
    var date = txt(item.querySelector(".date")) || "—";
    var access = item.querySelector(".acc-pwd") ? "pwd" : "pub";
    var important = item.classList.contains("imp");
    var fname = "";
    var fnameEl = item.querySelector(".admin-fname");
    if (fnameEl){ fname = fnameEl.textContent.replace(/^\s*🛈\s*/, "").trim(); }
    var urls = {}; var fallback = ""; var anyPer = false;
    LANGS.forEach(function(l){
      var a = item.querySelector("span.gtl."+l+" > a.open");
      if (a){ urls[l] = a.getAttribute("href"); anyPer = true; }
    });
    if (!anyPer){
      var single = item.querySelector("a.open[href]");
      if (single){ fallback = single.getAttribute("href"); }
    }
    var cats = { jur: [], area: [] }; var az = "", ourref = "", cardsubj = "", stav = "", court = "", begleit = "", rspis = "";
    if (caseEl){
      var c = (caseEl.getAttribute("data-cat")||"").trim();
      if (c){ cats.jur = c.split(/\s+/); }
      var ar = (caseEl.getAttribute("data-area")||"").trim();
      if (ar){ cats.area = ar.split(/\s+/); }
      az = caseEl.getAttribute("data-az")||"";
      ourref = caseEl.getAttribute("data-ourref")||"";
      var csEl = caseEl.querySelector(".court-subj .gtl.sk") || caseEl.querySelector(".court-subj .gtl.de");
      if (csEl){ cardsubj = csEl.textContent.trim(); }
      var pillEl = caseEl.querySelector(".pill");
      if (pillEl){ stav = pillEl.classList.contains("p-amber") ? "eingereicht" : (pillEl.classList.contains("p-green") ? "abgeschlossen" : "laeuft"); }
      var _sks = caseEl.querySelectorAll(".gtl.sk");
      for (var _mi=0; _mi<_sks.length; _mi++){
        var _mt = _sks[_mi].textContent || "";
        if (_mt.indexOf("\u2696")>=0 && _mt.indexOf(":")>=0){ court = _mt.slice(_mt.indexOf(":")+1).split(" \u00b7 ")[0].trim(); break; }
      }
      if (!court){ court = caseEl.getAttribute("data-court")||""; }
      if (caseEl.id){
        var _modal = document.getElementById(caseEl.id + "-modal");
        if (_modal){
          var _skb = _modal.querySelector(".gtl-b.sk") || _modal.querySelector(".gtl-b.de");
          if (_skb){
            var _ps = _skb.querySelectorAll("p"), _arr = [];
            for (var _pi=0; _pi<_ps.length; _pi++){ var _pt=(_ps[_pi].textContent||"").trim(); if(_pt){ _arr.push(_pt); } }
            begleit = _arr.join("\n\n");
          }
        }
        var _tile = document.querySelector('#fia-reg .rbtn[data-ids~="'+caseEl.id+'"]');
        if (_tile){ rspis = _tile.getAttribute("data-spis")||""; }
      }
    }
    var comments = !!(item.querySelector(".kcmt") || item.querySelector(".cmt-wrap"));
    var thread = item.getAttribute("data-thread") || "";
    var kcEl = item.querySelector(".kcmt"); var cmtid = kcEl ? (kcEl.getAttribute("data-doc")||"") : "";
    return { v:1, kauza:kauza, caseId:(caseEl?(caseEl.id||""):""), subj:subj, dir:dir, mode:"item", date:date,
      access:access, important:important, fname:fname, fallback:fallback,
      urls:urls, cats:cats, az:az, ourref:ourref, comments:comments, thread:thread, cmtid:cmtid,
      cardsubj:cardsubj, stav:stav, court:court, begleit:begleit, rspis:rspis };
  }
  function isRecv(item){
    var col = item.closest(".col");
    if (!col || !col.parentNode){ return false; }
    var cols = col.parentNode.querySelectorAll(":scope > .col");
    return (cols.length>1 && cols[1]===col);
  }
  function snapFor(item){
    // Reálny stav položky z DOM (nikdy neklame — číta priamo z karty na #303).
    var dom = buildSnapFromDom(item);
    var raw = item.getAttribute("data-snap");
    if (raw){
      try {
        var snap = JSON.parse(raw);
        var ce = item.closest("details.case");
        if (ce && ce.id){ snap.caseId = ce.id; }
        // data-snap je bohatý základ (kauzaKey, urls, az…), ALE stavové polia,
        // ktoré sa na karte menia po vzniku snapu, prepíšeme aktuálnou pravdou z DOM.
        snap.comments  = dom.comments;   // ← prítomnosť .kcmt/.cmt-wrap na karte
        snap.important = dom.important;  // ← trieda .imp
        snap.access    = dom.access;     // ← acc-pwd vs acc-pub
        snap.thread    = dom.thread;     // ← živé data-thread z karty (ID reťaze vlákna)
        snap.cmtid     = dom.cmtid;      // ← živý komentárový slug (.kcmt data-doc)
        // zobrazované polia karty/položky VŽDY prepíšeme aktuálnou pravdou z DOM,
        // aby sa každá oprava na karte prejavila v ✏️ Upraviť okamžite:
        if (dom.subj)     snap.subj     = dom.subj;      // Predmet dokumentu (položka)
        if (dom.cardsubj) snap.cardsubj = dom.cardsubj;  // Predmet konania (riadok 2 karty)
        if (dom.stav)     snap.stav     = dom.stav;      // Stav (pill)
        if (dom.court)    snap.court    = dom.court;     // Orgán/súd (data-court, ak je na karte)
        if (dom.begleit)  snap.begleit  = dom.begleit;   // Sprievodný text (naživo z modálu karty)
        if (dom.rspis)    snap.rspis    = dom.rspis;      // spis. zn. dlaždice (naživo z #fia-reg)
        snap.date   = dom.date;                          // Dátum
        snap.cats   = dom.cats;                          // jurisdikcia + oblasť práva
        snap.az     = dom.az;                            // Az. súdu
        snap.ourref = dom.ourref;                        // Naša spis. zn.
        if (dom.fname != null) snap.fname = dom.fname;   // Názov súboru (admin)
        if (dom.urls && Object.keys(dom.urls).length) snap.urls = dom.urls; // 9 jazykových odkazov
        if (snap.dir == null) snap.dir = dom.dir;
        return snap;
      } catch(e){}
    }
    return dom;
  }
  /* ===== ŽIVÝ REGISTER = ZDROJ PRAVDY: harvest VŠETKÝCH položiek (reálne + testcases) do formulára ===== */
  function harvestInventory(){
    var out = [];
    var items = document.querySelectorAll("#fia-kauzy .item, #fia-testcases .item");
    [].slice.call(items).forEach(function(it){
      if (!it.querySelector(".subj")){ return; }
      try { var s = snapFor(it); if (s && s.subj){ out.push(s); } } catch(e){}
    });
    return out;
  }
  function sendInventory(frame){
    if (!frame){ return; }
    try { frame.contentWindow.postMessage({ type:"fiafox-inventory", items: harvestInventory() }, new URL(frame.src).origin); } catch(e){}
  }
  function init(){
    if (!document.body.classList.contains("logged-in")){ return; }
    var frame = document.getElementById("fia-formx5-frame");
    if (!frame){ return; }
    var st = document.createElement("style");
    st.textContent = "#fia-kauzy .item .top{display:flex;flex-wrap:wrap;align-items:center;gap:6px;row-gap:4px}.fx-edit,.fx-reply{position:static;border-radius:8px;padding:2px 9px;font-size:13px;line-height:1.5;cursor:pointer;font-family:'Segoe UI',Calibri,Arial,sans-serif;white-space:nowrap}.fx-edit{border:1px solid #C9A100;background:#FFF8E6;color:#7a5a06;margin-left:auto}.fx-edit:hover{background:#FFEFC2}.fx-reply{border:1px solid #7FA8D9;background:#EAF2FB;color:#0C447C;margin-left:auto}.fx-reply~.fx-edit,#fia-kauzy .item .top .fx-reply+.fx-edit{margin-left:0}";
    document.head.appendChild(st);
    function addBtns(){
      var items = document.querySelectorAll("#fia-kauzy .item, #fia-testcases .item");
      [].slice.call(items).forEach(function(it){
        if (!it.querySelector(".subj")){ return; }
        if (it.querySelector(".fx-edit")){ return; }
        var b = document.createElement("button");
        b.type = "button"; b.className = "fx-edit";
        b.textContent = "✏️ Upraviť";
        b.title = "Upraviť toto podanie vo formulári x5";
        b.onclick = function(ev){
          ev.preventDefault(); ev.stopPropagation();
          var snap = snapFor(it);
          frame.contentWindow.postMessage({ type:"fiafox-edit", snap:snap }, new URL(frame.src).origin);
          var wrap = document.getElementById("fia-formx5-wrap");
          if (wrap){ wrap.scrollIntoView({ behavior:"smooth", block:"start" }); }
        };
        var top = it.querySelector(".top") || it;
        if (isRecv(it) && !it.querySelector(".fx-reply")){
          var r = document.createElement("button");
          r.type = "button"; r.className = "fx-reply";
          r.textContent = "\u21a9 Odpoveda\u0165";
          r.title = "Vytvori\u0165 odpove\u010f na toto podanie vo formul\u00e1ri x5 (opa\u010dn\u00fd smer + v\u00e4zba vl\u00e1kna)";
          r.onclick = function(ev){
            ev.preventDefault(); ev.stopPropagation();
            var snap = snapFor(it);
            frame.contentWindow.postMessage({ type:"fiafox-reply", snap:snap }, new URL(frame.src).origin);
            var wrap = document.getElementById("fia-formx5-wrap");
            if (wrap){ wrap.scrollIntoView({ behavior:"smooth", block:"start" }); }
          };
          top.appendChild(r);
        }
        top.appendChild(b);
      });
    }
    addBtns();
    // Živý inventár do formulára (zdroj pravdy = register): pošli po načítaní + na vyžiadanie z iframe + po zmene DOM
    setTimeout(function(){ sendInventory(frame); }, 400);
    setTimeout(function(){ sendInventory(frame); }, 1500);
    window.addEventListener("message", function(ev){
      if (ev.source !== frame.contentWindow){ return; }
      var d = ev.data;
      if (d && d.type === "fiafox-inv-req"){ sendInventory(frame); }
    });
    document.addEventListener("click", function(){ setTimeout(addBtns, 60); }, true);
    document.addEventListener("click", function(ev){
      var sum = ev.target.closest ? ev.target.closest("#fia-kauzy details.case > summary") : null;
      if (!sum){ return; }
      var caseEl = sum.parentNode;
      setTimeout(function(){
        if (caseEl.open && caseEl.id){
          frame.contentWindow.postMessage({ type:"fiafox-focus", caseId:caseEl.id }, new URL(frame.src).origin);
        }
      }, 40);
    }, true);
  }
  if (document.readyState === "loading"){ document.addEventListener("DOMContentLoaded", init); }
  else { init(); }
})();
