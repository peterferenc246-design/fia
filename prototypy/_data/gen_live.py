#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vygeneruje CELY register z fia_data.json — register.html + kartu pre kazde konanie.
   Ziadne rucne pisane data; vsetko pochadza z exportu #303."""
import json, os, re, html

LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"]
FLAG  = {"de":"de","en":"gb","sk":"sk","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
D = json.load(open('fia_data.json', encoding='utf-8'))
KARTY, POLOZKY, SUHRNY = D["karty"], D["polozky"], D["suhrny"]

def S(*v): return dict(zip(LANGS, v))
def g(d, b=False):
    c = "gtl-b" if b else "gtl"
    if not d: return ""
    fb = d.get("sk") or d.get("de") or next(iter(d.values()), "")
    return "".join(f'<span class="{c} {L}">{d.get(L, fb)}</span>' for L in LANGS)

UI = {
 "reg":  S("Fallregister","Case register","Register káuz","Registar predmeta","Rejestr spraw","Registro de casos","Registro dei casi","Registre des affaires","Ärenderegister"),
 "home": S("← Zur Startseite","← Home","← Späť na úvod","← Naslovnica","← Strona główna","← Inicio","← Home","← Accueil","← Startsidan"),
 "back": S("← Zum Register","← To the register","← Späť na register","← Na registar","← Do rejestru","← Al registro","← Al registro","← Au registre","← Till registret"),
 "all":  S("Alle","All","Všetko","Sve","Wszystko","Todo","Tutti","Tout","Alla"),
 "jde":  S("Deutschland","Germany","Nemecko","Njemačka","Niemcy","Alemania","Germania","Allemagne","Tyskland"),
 "jsk":  S("Slowakei","Slovakia","Slovensko","Slovačka","Słowacja","Eslovaquia","Slovacchia","Slovaquie","Slovakien"),
 "jeu":  S("EU","EU","EÚ","EU","UE","UE","UE","UE","EU"),
 "allv": S("Alle Verfahren anzeigen","Show all proceedings","Zobraziť všetky konania","Prikaži sve postupke","Pokaż wszystkie postępowania","Mostrar todos","Mostra tutti","Tout afficher","Visa alla"),
 "allk": S("★ Alle Fälle","★ All cases","★ Všetky kauzy","★ Svi predmeti","★ Wszystkie sprawy","★ Todos los casos","★ Tutti i casi","★ Toutes les affaires","★ Alla ärenden"),
 "verf": S("Verfahren","proceedings","konania","postupci","postępowania","procedimientos","procedimenti","procédures","förfaranden"),
 "docs": S("Dokumente","documents","dokumentov","dokumenata","dokumentów","documentos","documenti","documents","handlingar"),
 "sent": S("Gesendet","Sent","Odoslané","Poslano","Wysłane","Enviados","Inviati","Envoyés","Skickat"),
 "recv": S("Eingegangen","Received","Prijaté","Primljeno","Otrzymane","Recibidos","Ricevuti","Reçus","Mottaget"),
 "open": S("Akte öffnen →","Open →","Otvoriť kartu →","Otvori →","Otwórz →","Abrir →","Apri →","Ouvrir →","Öppna →"),
 "doc":  S("Dokument","Document","Dokument","Dokument","Dokument","Documento","Documento","Document","Handling"),
 "sum":  S("Zusammenfassung","Summary","Súhrn","Sažetak","Streszczenie","Resumen","Riepilogo","Résumé","Sammanfattning"),
 "sort": S("SORTIEREN","SORT","ZORADIŤ","SORTIRAJ","SORTUJ","ORDENAR","ORDINA","TRIER","SORTERA"),
 "s_d":  S("📅 Datum","📅 Date","📅 Dátum","📅 Datum","📅 Data","📅 Fecha","📅 Data","📅 Date","📅 Datum"),
 "s_a":  S("🏛 Az.","🏛 File ref.","🏛 Spis","🏛 Broj","🏛 Sygn.","🏛 Ref.","🏛 Rif.","🏛 Réf.","🏛 Nr"),
 "gen":  S("aus den Daten erzeugt","generated from data","vygenerované z dát","generirano iz podataka","wygenerowane z danych","generado a partir de datos","generato dai dati","généré à partir des données","genererat från data"),
}
STAV = {"laeuft": S("Läuft","Pending","Prebieha","U tijeku","W toku","En curso","In corso","En cours","Pågår"),
        "eingereicht": S("Eingereicht","Filed","Podané","Podneseno","Złożone","Presentado","Depositata","Déposée","Inlämnad"),
        "abgelehnt": S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag")}

def jflag(j):
    return '<span class="jf">🇪🇺</span>' if j == "eu" else f'<img class="jf" src="https://flagcdn.com/{FLAG.get(j,"de")}.svg" alt="{j}">'

CSS = """
:root{--navy:#1F3864;--red:#C00000;--soft:#D6E6F2;--bd:#c9d8e8}
*{box-sizing:border-box}
body{margin:0;color:#22303f;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
 background:linear-gradient(#8ec5ea 0%,#b9dcf3 34%,#dcecf8 64%,#f3e9d6 100%);background-attachment:fixed;min-height:100vh}
.top{text-align:center;padding:20px 16px 4px}
.top h1{margin:0;font-size:22px;color:var(--navy);font-weight:800}
.wrap{max-width:1000px;margin:0 auto;padding:0 16px 50px}
.navbar{background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(31,56,100,.10);padding:9px 14px;
 display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.hm{border:1px solid var(--bd);border-radius:6px;padding:5px 14px;text-decoration:none;color:var(--navy);font-size:13px}
.hm:hover{background:#f2f7fc}
.lang{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.lang .lb{font-size:10px;color:#8a97a6;letter-spacing:.12em;margin-right:3px}
.f{background:none;border:1px solid rgba(31,56,100,.3);border-radius:3px;padding:0;cursor:pointer;width:30px;height:20px;opacity:.5;overflow:hidden}
.f img{width:30px;height:20px;object-fit:cover;display:block}
.f.on{opacity:1;border-color:var(--navy);box-shadow:0 0 0 2px rgba(31,56,100,.25)}
.panel{background:#fff;border-radius:8px;box-shadow:0 2px 10px rgba(31,56,100,.10);padding:20px 22px;margin-bottom:14px}
.panel>h2{margin:0 0 14px;font-size:22px;color:var(--navy)}
.tabs{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
.tab{border:1px solid var(--bd);background:#fbfcfd;border-radius:6px;padding:5px 14px;font-size:13px;cursor:pointer;color:#3d4d5e;display:flex;align-items:center;gap:6px}
.tab.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.tab img{width:18px;height:12px;object-fit:cover;border-radius:2px}
.allrow{border:1px solid var(--bd);border-left:4px solid var(--navy);border-radius:6px;padding:11px 15px;margin-bottom:12px;cursor:pointer;background:#fbfcfd}
.allrow.on{background:#eef4fb}
.allrow .t{font-size:14px;color:var(--navy);font-weight:600}
.allrow .b{display:inline-block;margin-top:5px;font-size:11px;background:#fff3d6;color:#8a5a00;border:1px solid #f0c040;border-radius:999px;padding:1px 10px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:11px}
@media(max-width:880px){.grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.grid{grid-template-columns:1fr}}
.tile{text-align:left;background:#fbfcfd;border:1px solid var(--bd);border-left:4px solid var(--navy);border-radius:6px;padding:11px 13px;cursor:pointer;font:inherit;color:inherit}
.tile:hover{background:#f2f7fc}
.tile.on{background:#eef4fb;box-shadow:0 0 0 2px rgba(31,56,100,.28)}
.tf{display:flex;gap:4px;align-items:center;margin-bottom:5px;min-height:13px}
.jf{width:17px;height:12px;object-fit:cover;border-radius:2px;font-size:12px;line-height:1}
.tn{font-size:13px;font-weight:700;color:var(--navy);line-height:1.3}
.tk{font-size:10.5px;color:#8a97a6;letter-spacing:.04em;margin-top:3px}
.tc{display:inline-block;margin-top:7px;font-size:11px;color:#54637a;background:#eef2f7;border-radius:999px;padding:1px 9px}
.sortbar{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:center;margin:14px 0}
.sortbar .lb{font-size:10.5px;color:#5a6a7d;letter-spacing:.12em}
.sb{border:1px solid var(--bd);background:#fff;border-radius:6px;padding:4px 13px;font-size:12.5px;cursor:pointer;color:#3d4d5e}
.sb.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.kon{background:#fff;border-radius:7px;box-shadow:0 1px 6px rgba(31,56,100,.09);padding:12px 16px;margin-bottom:9px;
 display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.knaz{font-size:14.5px;color:var(--navy);font-weight:600}
.korg{font-size:12.5px;color:#7a8899;margin-top:2px}
.kside{display:flex;align-items:center;gap:10px}
.st{font-size:11px;border-radius:999px;padding:2px 10px;white-space:nowrap}
.st-laeuft,.st-eingereicht{background:#fff3d6;color:#8a5a00;border:1px solid #f0c040}
.st-abgelehnt{background:#fde8e8;color:#8a1c1c;border:1px solid #e8b4b4}
.go{font-size:12.5px;text-decoration:none;background:var(--navy);color:#fff;border-radius:4px;padding:5px 13px;white-space:nowrap}
.go:hover{background:#16294a}
.chead{background:#fff;border-radius:8px;border-top:4px solid var(--navy);box-shadow:0 2px 10px rgba(31,56,100,.10);padding:20px 24px;margin-bottom:16px}
.chead h2{margin:0 0 6px;font-size:21px;color:var(--navy);line-height:1.3}
.chead .org{font-size:13px;color:#5a6a7d}
.chead .meta{font-size:12.5px;color:#5a6a7d;border-top:1px solid var(--bd);margin-top:10px;padding-top:9px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:900px){.cols{grid-template-columns:1fr}}
.col h3{margin:0 0 9px;font-size:12px;text-transform:uppercase;letter-spacing:.09em;color:#7a8899}
.item{background:#fff;border-radius:7px;box-shadow:0 1px 6px rgba(31,56,100,.09);padding:12px 15px;margin-bottom:9px}
.itop{display:flex;justify-content:space-between;gap:10px;margin-bottom:4px}
.idate{font-size:12px;color:#7a8899;font-weight:700}
.isubj{font-size:14px;color:var(--navy);font-weight:600;line-height:1.35;margin-bottom:8px}
.ibtn{display:flex;gap:6px;flex-wrap:wrap}
.b{font-size:11.5px;text-decoration:none;border:1px solid var(--bd);border-radius:3px;padding:3px 9px;color:#3d4d5e;background:#fbfcfd;cursor:pointer}
.b:hover{border-color:var(--navy);color:var(--navy)}
.sumbox{margin-top:9px;border-top:1px dashed var(--bd);padding-top:9px;font-size:13px;line-height:1.6;color:#3d4d5e;display:none}
.sumbox.on{display:block}
.sumbox p{margin:0 0 8px}
.proto{background:#fff6d6;border:1px solid #f0c040;border-left:5px solid var(--red);padding:10px 14px;margin:10px 0 14px;border-radius:4px;font-size:12.5px}
.gtl,.gtl-b{display:none}
"""
SHOW = "".join(f'body[data-l="{L}"] .gtl.{L}{{display:inline}}body[data-l="{L}"] .gtl-b.{L}{{display:block}}' for L in LANGS)
FLAGS = "".join(f'<button class="f{" on" if L=="sk" else ""}" data-l="{L}"><img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in LANGS)
LSCRIPT = """
document.querySelectorAll('.f').forEach(function(b){b.addEventListener('click',function(){
 document.body.dataset.l=b.dataset.l;document.documentElement.lang=b.dataset.l;
 document.querySelectorAll('.f').forEach(function(x){x.classList.remove('on');});b.classList.add('on');});});
"""

def page(title, body, script=""):
    return f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{html.escape(title)} — FIA FOX</title>
<meta name="description" content="Verejný register právnych konaní iniciatívy FIA FOX — dokumenty, podania a odpovede inštitúcií v deviatich jazykoch.">
<style>{CSS}{SHOW}</style></head><body data-l="sk">
<div class="top"><h1>FIA FOX — Fair Internet Initiative</h1></div>
<div class="wrap">{body}</div>
<script>{LSCRIPT}{script}</script></body></html>"""

# ─────────── KARTY: doplnkove udaje ───────────
pol_karty = {}
for p in POLOZKY:
    pol_karty.setdefault(p["karta"], []).append(p)
karta_by_id = {k["id"]: k for k in KARTY}
kauza_karty = {}
for p in POLOZKY:
    if p["karta"]:
        kauza_karty.setdefault(p["kauza"] or "?", set()).add(p["karta"])

kauza_nazov = {}
for p in POLOZKY:
    if p["kauza"] and p["kauza_nazov"]:
        kauza_nazov.setdefault(p["kauza"], p["kauza_nazov"])

def jur_karty(cid):
    k = karta_by_id.get(cid)
    return k["jur"] if k and k["jur"] else ["de"]

# ─────────── REGISTER ───────────
tiles = ""
for kz in sorted(kauza_karty, key=lambda x: -len(kauza_karty[x])):
    cids = sorted(kauza_karty[kz])
    js = sorted({j for c in cids for j in jur_karty(c)})
    npol = sum(1 for p in POLOZKY if p["kauza"] == kz)
    tiles += (f'<button class="tile" data-k="{kz}" data-jur="{" ".join(js)}">'
              f'<div class="tf">{"".join(jflag(j) for j in js)}</div>'
              f'<div class="tn">{html.escape(kauza_nazov.get(kz, kz))[:70]}</div>'
              f'<div class="tk">{kz}</div>'
              f'<span class="tc">• {len(cids)} {g(UI["verf"])} · {npol} {g(UI["docs"])}</span></button>')

rows = ""
for cid, ps in sorted(pol_karty.items(), key=lambda x: -len(x[1])):
    k = karta_by_id.get(cid, {})
    kz = ps[0]["kauza"] or "?"
    st = ps[0]["stav"] or "laeuft"
    rows += (f'<div class="kon" data-k="{kz}" data-d="{k.get("date","")}" data-az="{html.escape(k.get("az","") or "")}">'
             f'<div><div class="knaz">{g(k.get("nazov")) or html.escape(cid)}</div>'
             f'<div class="korg">{g(k.get("organ"))} &nbsp;·&nbsp; <b>{html.escape(k.get("az","") or "—")}</b>'
             f' &nbsp;·&nbsp; {len(ps)} {g(UI["docs"])}</div></div>'
             f'<div class="kside"><span class="st st-{st}">{g(STAV.get(st, STAV["laeuft"]))}</span>'
             f'<a class="go" href="karta-{cid}.html">{g(UI["open"])}</a></div></div>')

reg_body = f"""
<div class="navbar"><a class="hm" href="index.html">{g(UI["home"])}</a>
 <div class="lang"><span class="lb">LANG</span>{FLAGS}</div></div>
<div class="panel"><h2>{g(UI["reg"])}</h2>
 <div class="tabs"><button class="tab on" data-j="all">{g(UI["all"])}</button>
  <button class="tab" data-j="de"><img src="https://flagcdn.com/de.svg" alt="DE">{g(UI["jde"])}</button>
  <button class="tab" data-j="sk"><img src="https://flagcdn.com/sk.svg" alt="SK">{g(UI["jsk"])}</button>
  <button class="tab" data-j="eu">🇪🇺 {g(UI["jeu"])}</button></div>
 <div class="allrow on" id="allrow"><div class="t">🌐 {g(UI["allv"])}</div><span class="b">{g(UI["allk"])}</span></div>
 <div class="grid">{tiles}</div></div>
<div class="sortbar"><span class="lb">{g(UI["sort"])}</span>
 <button class="sb on" data-s="d">{g(UI["s_d"])}</button><button class="sb" data-s="az">{g(UI["s_a"])}</button></div>
<div id="list">{rows}</div>
"""
REGJS = """
var SEL=null,JUR='all',SORT='d';
function apply(){
 document.querySelectorAll('.tile').forEach(function(t){
  t.style.display=(JUR==='all'||t.dataset.jur.split(' ').indexOf(JUR)>=0)?'':'none';
  t.classList.toggle('on',SEL===t.dataset.k);});
 document.getElementById('allrow').classList.toggle('on',SEL===null);
 var l=document.getElementById('list'),r=[].slice.call(l.querySelectorAll('.kon'));
 r.forEach(function(x){x.style.display=(SEL===null||x.dataset.k===SEL)?'':'none';});
 r.sort(function(a,b){return SORT==='d'?b.dataset.d.localeCompare(a.dataset.d):a.dataset.az.localeCompare(b.dataset.az);})
  .forEach(function(x){l.appendChild(x);});}
document.querySelectorAll('.tile').forEach(function(t){t.addEventListener('click',function(){SEL=(SEL===t.dataset.k)?null:t.dataset.k;apply();});});
document.getElementById('allrow').addEventListener('click',function(){SEL=null;apply();});
document.querySelectorAll('.tab').forEach(function(b){b.addEventListener('click',function(){JUR=b.dataset.j;SEL=null;
 document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on');});b.classList.add('on');apply();});});
document.querySelectorAll('.sb').forEach(function(b){b.addEventListener('click',function(){SORT=b.dataset.s;
 document.querySelectorAll('.sb').forEach(function(x){x.classList.remove('on');});b.classList.add('on');apply();});});
apply();
"""
open('register.html','w',encoding='utf-8').write(page("Fallregister", reg_body, REGJS))

# ─────────── KARTY KONANI ───────────
def item_html(p, n):
    url = (p.get("urls") or {})
    doc = "".join(f'<span class="gtl {L}"><a class="b" href="{html.escape(url.get(L,""))}" target="_blank" rel="noopener">📄 {UI["doc"][L]}</a></span>'
                  for L in LANGS if url.get(L))
    sm = ""
    if p["summodId"] and p["summodId"] in SUHRNY:
        s = SUHRNY[p["summodId"]]
        blocks = "".join(f'<div class="gtl-b {L}">{s[L]}</div>' for L in LANGS if L in s)
        sm = (f'<button class="b" onclick="document.getElementById(\'s{n}\').classList.toggle(\'on\')">📄 {g(UI["sum"])}</button>'
              f'<div class="sumbox" id="s{n}">{blocks}</div>')
    st = p["stav"] or "laeuft"
    return (f'<div class="item"><div class="itop"><span class="idate">{html.escape(p["date"])}</span>'
            f'<span class="st st-{st}">{g(STAV.get(st, STAV["laeuft"]))}</span></div>'
            f'<div class="isubj">{g(p["subj"])}</div><div class="ibtn">{doc}{sm}</div></div>')

n = 0
for cid, ps in pol_karty.items():
    if not cid: continue
    k = karta_by_id.get(cid, {})
    sent = [p for p in ps if p["dir"] == "sent"]
    recv = [p for p in ps if p["dir"] != "sent"]
    hs = ""
    for p in sent: n += 1; hs += item_html(p, n)
    hr = ""
    for p in recv: n += 1; hr += item_html(p, n)
    body = f"""
<div class="navbar"><a class="hm" href="register.html">{g(UI["back"])}</a>
 <div class="lang"><span class="lb">LANG</span>{FLAGS}</div></div>
<div class="chead"><h2>{g(k.get("nazov")) or html.escape(cid)}</h2>
 <div class="org">{g(k.get("organ"))}</div>
 <div class="meta"><b>{html.escape(k.get("az","") or "—")}</b> &nbsp;·&nbsp; {html.escape(k.get("ourref","") or "")}
  &nbsp;·&nbsp; {html.escape(k.get("datum_txt","") or k.get("date",""))} &nbsp;·&nbsp; {len(ps)} {g(UI["docs"])}</div></div>
<div class="cols">
 <div class="col"><h3>▲ {g(UI["sent"])} ({len(sent)})</h3>{hs}</div>
 <div class="col"><h3>▼ {g(UI["recv"])} ({len(recv)})</h3>{hr}</div>
</div>"""
    open(f'karta-{cid}.html', 'w', encoding='utf-8').write(page(k.get("nazov", {}).get("sk", cid), body))

print(f"register.html + {len([c for c in pol_karty if c])} kariet")
print(f"  kauzy (dlazdice): {len(kauza_karty)}")
print(f"  dokumentov:       {len(POLOZKY)}")
print(f"  suhrnov vlozenych: {sum(1 for p in POLOZKY if p['summodId'] in SUHRNY)}")
tot = sum(os.path.getsize(f) for f in os.listdir('.') if f.startswith(('register.html','karta-')))
print(f"  velkost spolu:    {tot//1024} kB")
