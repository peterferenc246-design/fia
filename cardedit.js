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
      subj = clone.textContent.trim();
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
    var cats = { jur: [], area: [] }; var az = "", ourref = "";
    if (caseEl){
      var c = (caseEl.getAttribute("data-cat")||"").trim();
      if (c){ cats.jur = c.split(/\s+/); }
      var ar = (caseEl.getAttribute("data-area")||"").trim();
      if (ar){ cats.area = ar.split(/\s+/); }
      az = caseEl.getAttribute("data-az")||"";
      ourref = caseEl.getAttribute("data-ourref")||"";
    }
    return { v:1, kauza:kauza, subj:subj, dir:dir, mode:"item", date:date,
      access:access, important:important, fname:fname, fallback:fallback,
      urls:urls, cats:cats, az:az, ourref:ourref };
  }
  function snapFor(item){
    var raw = item.getAttribute("data-snap");
    if (raw){ try { return JSON.parse(raw); } catch(e){} }
    return buildSnapFromDom(item);
  }
  function init(){
    if (!document.body.classList.contains("logged-in")){ return; }
    var frame = document.getElementById("fia-formx5-frame");
    if (!frame){ return; }
    var st = document.createElement("style");
    st.textContent = "#fia-kauzy .item{position:relative}.fx-edit{position:absolute;top:8px;right:10px;border:1px solid #C9A100;background:#FFF8E6;border-radius:8px;padding:2px 9px;font-size:13px;line-height:1.5;cursor:pointer;z-index:3;font-family:'Segoe UI',Calibri,Arial,sans-serif;color:#7a5a06}.fx-edit:hover{background:#FFEFC2}";
    document.head.appendChild(st);
    function addBtns(){
      var items = document.querySelectorAll("#fia-kauzy .item");
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
          frame.contentWindow.postMessage({ type:"fiafox-edit", snap:snap }, "https://rawcdn.githack.com");
          var wrap = document.getElementById("fia-formx5-wrap");
          if (wrap){ wrap.scrollIntoView({ behavior:"smooth", block:"start" }); }
        };
        it.appendChild(b);
      });
    }
    addBtns();
    document.addEventListener("click", function(){ setTimeout(addBtns, 60); }, true);
  }
  if (document.readyState === "loading"){ document.addEventListener("DOMContentLoaded", init); }
  else { init(); }
})();
