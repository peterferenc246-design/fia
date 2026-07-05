/* FIA FOX — x5-clipboard-bridge.js
   Rieši cross-origin clipboard problém iframe x5 (rawcdn.githack.com).
   iframe pošle postMessage {type:'fiafox-copy', text:'...'} do parent (foxprof.club).
   Tento skript beží na parent (same-origin) — má plný clipboard prístup.
   Bez zásahu do kauzy.js, cardedit.js, register.js — nezávislý, single-purpose. */
(function () {
  window.addEventListener("message", function (ev) {
    try {
      var d = ev.data;
      if (!d || d.type !== "fiafox-copy" || typeof d.text !== "string") return;
      var text = d.text;
      // Odpoveď späť do iframe (aby x5 vedel, či sa podarilo)
      function reply(ok, why) {
        try {
          if (ev.source && ev.source.postMessage) {
            ev.source.postMessage({ type: "fiafox-copy-result", ok: !!ok, why: why || "", len: text.length }, "*");
          }
        } catch (e) {}
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { reply(true, ""); },
          function (e) { reply(false, (e && e.name) || "writeText rejected"); });
      } else {
        // Fallback: dočasný textarea + execCommand (starší prehliadače)
        try {
          var ta = document.createElement("textarea");
          ta.value = text;
          ta.style.position = "fixed"; ta.style.top = "-9999px"; ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.focus(); ta.select();
          var ok = document.execCommand("copy");
          document.body.removeChild(ta);
          reply(ok, ok ? "" : "execCommand copy=false");
        } catch (e2) { reply(false, (e2 && e2.name) || "fallback error"); }
      }
    } catch (e) {}
  });
})();
