#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vytiahne z exportu #303 vsetky data do strojovo citatelneho suboru fia_data.json."""
import json, re, html, sys

LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"]
h = open('303.html', encoding='utf-8').read()

def gtl(seg):
    """z useku HTML vytiahne prvu sadu 9 jazykovych spanov"""
    out = {}
    for L, t in re.findall(r'<span class="gtl (\w\w)">(.*?)</span>', seg, re.S):
        if L in LANGS and L not in out:
            out[L] = re.sub(r'<[^>]+>', '', t).strip()
        if len(out) == 9:
            break
    return out

# ─────────── KARTY ───────────
karty = []
for m in re.finditer(r'<details class="case"([^>]*)>(.*?)<div class="case-body">', h, re.S):
    at, head = m.group(1), m.group(2)
    def a(n):
        r = re.search(n + r'="([^"]*)"', at)
        return r.group(1) if r else ""
    tit = re.search(r'<div class="case-title">(.*?)</div>', head, re.S)
    crt = re.search(r'<div class="court">(.*?)</div>', head, re.S)
    pill = re.search(r'<span class="pill[^"]*">(.*?)</span>', head, re.S)
    dat = re.search(r'<span class="case-date">([^<]*)</span>', head)
    karty.append(dict(
        id=a("id"), jur=a("data-cat").split(), date=a("data-date"), az=a("data-az"),
        ourref=a("data-ourref"), area=a("data-area").split(), pin=a("data-pin"),
        datum_txt=(dat.group(1).replace("📅", "").strip() if dat else ""),
        nazov=gtl(tit.group(1)) if tit else {},
        organ=gtl(crt.group(1)) if crt else {},
        stav=gtl(pill.group(1)) if pill else {},
    ))

# ─────────── POLOZKY ───────────
bloky = re.split(r'(?=<div class="item[^"]*"[^>]{0,60}?data-snap=)', h)
polozky = []
for b in bloky[1:]:
    ms = re.match(r"<div class=\"item[^\"]*\"[^>]{0,60}?data-snap='(.*?)'>", b, re.S)
    if not ms:
        continue
    try:
        snap = json.loads(html.unescape(ms.group(1)))
    except Exception:
        continue
    telo = b[:60000]
    subj = re.search(r'<div class="subj">(.*?)</div>', telo, re.S)
    sm = re.search(r'href="#(summod-[^"]+)"', telo)
    links = {}
    for L, u in re.findall(r'<span class="gtl (\w\w)"><a class="open" href="([^"]+)"', telo):
        links.setdefault(L, html.unescape(u))
    polozky.append(dict(
        kauza=snap.get("kauzaKey", ""), kauza_nazov=snap.get("kauza", ""),
        dir=snap.get("dir", ""), date=snap.get("date", ""), stav=snap.get("stav", ""),
        access=snap.get("access", ""), az=snap.get("az", ""), ourref=snap.get("ourref", ""),
        court=snap.get("court", ""), cmtid=snap.get("cmtid", ""),
        summodId=snap.get("summodId") or (sm.group(1) if sm else ""),
        fname=snap.get("fname", ""), fpath=snap.get("fpath", ""),
        cats=snap.get("cats", {}), mode=snap.get("mode", ""),
        subj_snap=snap.get("subj", ""), summary_snap=snap.get("summary", ""),
        subj=gtl(subj.group(1)) if subj else {},
        urls=snap.get("urls", {}) or links,
    ))

# ─────────── SUHRNY (modaly) ───────────
suhrny = {}
for m in re.finditer(r'<div id="(summod-[^"]+)" class="kmodal summod">(.*?)(?=<div id="|<div class="item"|</details>)', h, re.S):
    mid, body = m.group(1), m.group(2)
    d = {}
    for L, t in re.findall(r'<div class="gtl-b (\w\w)">(.*?)</div>(?=<div class="gtl-b|\s*</div>)', body, re.S):
        if L in LANGS:
            d[L] = t.strip()
    if d:
        suhrny[mid] = d

# ─────────── KAUZY ───────────
kauzy = {}
for p in polozky:
    k = p["kauza"] or "?"
    z = kauzy.setdefault(k, dict(kod=k, nazov=p["kauza_nazov"], n=0, jur=set(), karty=set()))
    z["n"] += 1
    ju = (p.get("cats") or {}).get("jur", "")
    for j in (ju.split() if isinstance(ju, str) else (ju or [])):
        z["jur"].add(j)
for z in kauzy.values():
    z["jur"] = sorted(z["jur"]); z["karty"] = sorted(z["karty"])

data = dict(karty=karty, polozky=polozky, suhrny=suhrny, kauzy=list(kauzy.values()))
json.dump(data, open('fia_data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print(f"KARTY:    {len(karty)}")
print(f"POLOZKY:  {len(polozky)}   (odoslane {sum(1 for p in polozky if p['dir']=='sent')} / "
      f"dosle {sum(1 for p in polozky if p['dir']=='recv')})")
print(f"SUHRNY:   {len(suhrny)} modalov, "
      f"{sum(len(v) for v in suhrny.values())} jazykovych verzii")
print(f"KAUZY:    {len(kauzy)}")
for z in sorted(kauzy.values(), key=lambda x: -x["n"]):
    print(f"   {z['kod']:<10} {z['n']:>2} poloziek  {z['jur']}  {z['nazov'][:52]}")
n9 = sum(1 for p in polozky if len(p['subj']) == 9)
u9 = sum(1 for p in polozky if len(p.get('urls') or {}) == 9)
print(f"\nkontrola: {n9}/{len(polozky)} poloziek ma predmet v 9 jazykoch, "
      f"{u9}/{len(polozky)} ma odkazy v 9 jazykoch")
print("subor fia_data.json:", __import__('os').path.getsize('fia_data.json'), "B")
