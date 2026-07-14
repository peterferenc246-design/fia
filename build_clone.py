#!/usr/bin/env python3
# VLAJKA-VIEWER clone builder — Antrag auf Erlass einer einstweiligen Verfuegung
# Usage: python3 build_clone.py <LANG> lang_src/<lang>.blocks.tsv out.pdf
# Renders one language clone matching the approved FR_1zu1 layout (Carlito 12pt).
import sys, html, os
from weasyprint import HTML

FLAGS = {
 "FR": '<svg viewBox="0 0 3 2"><rect width="1" height="2" x="0" fill="#0055A4"/><rect width="1" height="2" x="1" fill="#fff"/><rect width="1" height="2" x="2" fill="#EF4135"/></svg>',
 "HR": '<svg viewBox="0 0 3 2"><rect width="3" height="0.667" y="0" fill="#FF0000"/><rect width="3" height="0.667" y="0.667" fill="#fff"/><rect width="3" height="0.667" y="1.334" fill="#171796"/><rect x="1.25" y="0.55" width="0.5" height="0.9" fill="#fff" stroke="#171796" stroke-width="0.03"/><rect x="1.25" y="0.55" width="0.166" height="0.3" fill="#FF0000"/><rect x="1.584" y="0.55" width="0.166" height="0.3" fill="#FF0000"/><rect x="1.416" y="0.85" width="0.168" height="0.3" fill="#FF0000"/><rect x="1.25" y="1.15" width="0.166" height="0.3" fill="#FF0000"/><rect x="1.584" y="1.15" width="0.166" height="0.3" fill="#FF0000"/></svg>',
 "PL": '<svg viewBox="0 0 3 2"><rect width="3" height="1" y="0" fill="#fff"/><rect width="3" height="1" y="1" fill="#DC143C"/></svg>',
 "IT": '<svg viewBox="0 0 3 2"><rect width="1" height="2" x="0" fill="#009246"/><rect width="1" height="2" x="1" fill="#fff"/><rect width="1" height="2" x="2" fill="#CE2B37"/></svg>',
 "ES": '<svg viewBox="0 0 3 2"><rect width="3" height="2" fill="#AA151B"/><rect width="3" height="1" y="0.5" fill="#F1BF00"/></svg>',
 "SV": '<svg viewBox="0 0 16 10"><rect width="16" height="10" fill="#005293"/><rect x="5" width="2" height="10" fill="#FECB00"/><rect y="4" width="16" height="2" fill="#FECB00"/></svg>',
}
NAME = {"FR":"FRANÇAIS","HR":"HRVATSKI","PL":"POLSKI","IT":"ITALIANO","ES":"ESPAÑOL","SV":"SVENSKA"}
COUNTRY = {"FR":"Allemagne","HR":"Njemačka","PL":"Niemcy","IT":"Germania","ES":"Alemania","SV":"Tyskland"}
ADDR_LBL = {"FR":"« Requérant »","HR":"„Podnositelj zahtjeva“","PL":"„Wnioskodawca“","IT":"«Richiedente»","ES":"«Solicitante»","SV":"”Sökande”"}
DATELINE = {"FR":"à Kumhausen, le 10 décembre 2024","HR":"u Kumhausenu, 10. prosinca 2024.","PL":"Kumhausen, 10 grudnia 2024 r.","IT":"Kumhausen, 10 dicembre 2024","ES":"Kumhausen, 10 de diciembre de 2024","SV":"Kumhausen, den 10 december 2024"}
TITLE = {"FR":"DEMANDE DE DÉLIVRANCE D'UNE ORDONNANCE JUDICIAIRE","HR":"ZAHTJEV ZA DONOŠENJE PRIVREMENE MJERE","PL":"WNIOSEK O WYDANIE ZARZĄDZENIA TYMCZASOWEGO","IT":"RICHIESTA DI PROVVEDIMENTO CAUTELARE D'URGENZA","ES":"SOLICITUD DE ADOPCIÓN DE UNA MEDIDA CAUTELAR","SV":"BEGÄRAN OM UTFÄRDANDE AV ETT INTERIMISTISKT FÖRORDNANDE"}
SUBTITLE = {"FR":"Requête en référé (einstweilige Verfügung) — 10.12.2024","HR":"Zahtjev za privremenu mjeru (einstweilige Verfügung) — 10.12.2024","PL":"Wniosek o zabezpieczenie (einstweilige Verfügung) — 10.12.2024","IT":"Ricorso cautelare (einstweilige Verfügung) — 10.12.2024","ES":"Solicitud de medida cautelar (einstweilige Verfügung) — 10.12.2024","SV":"Interimistisk ansökan (einstweilige Verfügung) — 10.12.2024"}
CLOSING = {"FR":"Respectueusement,","HR":"S poštovanjem,","PL":"Z poważaniem,","IT":"Con osservanza,","ES":"Atentamente,","SV":"Högaktningsfullt,"}
ROLE = {"FR":"citoyen de l'Union européenne","HR":"građanin Europske unije","PL":"obywatel Unii Europejskiej","IT":"cittadino dell'Unione europea","ES":"ciudadano de la Unión Europea","SV":"medborgare i Europeiska unionen"}

CSS = """
@page { size: A4; margin: 2cm 2cm 1.6cm 2cm; }
* { box-sizing: border-box; }
body { font-family:'Carlito','Calibri','DejaVu Sans',sans-serif; font-size:12pt; color:#000; line-height:1.32; }
.topwrap { position:relative; min-height:118px; }
.banner { position:absolute; right:0; top:0; border:2px solid #E4002B; border-radius:9px; padding:6px 12px 6px 8px; display:flex; align-items:center; }
.banner svg { width:64px; height:42px; border:1px solid #999; display:block; margin-right:11px; }
.banner .bn { font-weight:bold; font-size:19pt; line-height:1.0; color:#111; letter-spacing:.5px; }
.banner .bv { font-size:8.5pt; color:#333; letter-spacing:1px; margin-top:2px; }
.lbl { font-weight:bold; }
.contact { }
.court { margin-top:14px; }
.court b { font-weight:bold; }
.dateline { text-align:right; margin-top:6px; }
h1.title { text-align:center; color:#1F3864; font-weight:bold; font-size:18pt; margin:22px 0 2px 0; }
.subtitle { text-align:center; font-style:italic; color:#6B7280; font-size:11pt; margin:0 0 14px 0; }
p.body { text-align:justify; margin:8px 0; }
h2.h1 { color:#1F3864; font-weight:bold; font-size:15pt; margin:18px 0 4px 0; }
h3.h2 { color:#1F3864; font-weight:bold; font-size:14pt; margin:14px 0 3px 0; }
ul { margin:6px 0 6px 0; padding-left:22px; }
li { text-align:justify; margin:3px 0; }
table.sig { width:100%; margin-top:26px; border-collapse:collapse; page-break-inside:avoid; }
table.sig td { vertical-align:bottom; border:none; }
td.sigL { width:45%; }
td.sigR { width:55%; text-align:center; }
td.sigR img { width:232px; height:auto; display:block; margin:0 auto; }
.role { font-style:italic; }
"""

def esc(s): return html.escape(s)

def build(lang, tsv, out):
    lines = [l.rstrip("\n") for l in open(tsv, encoding="utf-8") if l.strip()]
    body_html = []
    bullets = []
    def flush():
        if bullets:
            body_html.append("<ul>"+"".join(f"<li>{esc(b)}</li>" for b in bullets)+"</ul>")
            bullets.clear()
    for ln in lines:
        typ, _, txt = ln.partition("\t")
        if typ == "bullet":
            bullets.append(txt); continue
        flush()
        if typ == "h1": body_html.append(f'<h2 class="h1">{esc(txt)}</h2>')
        elif typ == "h2": body_html.append(f'<h3 class="h2">{esc(txt)}</h3>')
        else: body_html.append(f'<p class="body">{esc(txt)}</p>')
    flush()
    doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="topwrap">
  <div class="banner"><span class="fl">{FLAGS[lang]}</span><span><span class="bn">{esc(NAME[lang])}</span><br><span class="bv">VLAJKA-VIEWER · {lang}</span></span></div>
  <div class="contact"><div class="lbl">{esc(ADDR_LBL[lang])}</div>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen<br>{esc(COUNTRY[lang])}<br>info@foxprof.club<br>+49 157 317 33332</div>
</div>
<div class="court"><b>Landgericht Landshut</b><br>Maximilianstraße 22<br>84028 Landshut<br>{esc(COUNTRY[lang])}</div>
<div class="dateline">{esc(DATELINE[lang])}</div>
<h1 class="title">{esc(TITLE[lang])}</h1>
<div class="subtitle">{esc(SUBTITLE[lang])}</div>
{''.join(body_html)}
<table class="sig"><tr>
<td class="sigL">{esc(CLOSING[lang])}<br><br>{esc(DATELINE[lang])}</td>
<td class="sigR"><img src="sig.png"><br><span class="role">{esc(ROLE[lang])}</span></td>
</tr></table>
</body></html>"""
    HTML(string=doc, base_url=os.path.dirname(os.path.abspath(__file__))).write_pdf(out)
    print("built", out, lang)

# fix banner svg wrapper (flag span needs the svg to size)
FLAGS = {k:v.replace("<svg ", '<svg preserveAspectRatio="xMidYMid meet" ') for k,v in FLAGS.items()}

if __name__ == "__main__":
    lang, tsv, out = sys.argv[1], sys.argv[2], sys.argv[3]
    build(lang, tsv, out)
