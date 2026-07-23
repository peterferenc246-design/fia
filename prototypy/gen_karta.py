#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROTOTYP — karta konania DG COMP ako samostatna HTML stranka generovana z dat.
   Mimo WordPressu. Nezasahuje do #303 ani do ostrych materialov kauzy."""
import html

LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"]
FLAG  = {"de":"de","en":"gb","sk":"sk","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
SHA   = "8d1f0c501c922d66cf47ab2acfd795b4ab531abb"
REPO  = f"https://cdn.jsdelivr.net/gh/peterferenc246-design/fia@{SHA}/dg-comp-kartel-pristup-k-dokumentom/"
CORR  = "https://peterferenc246-design.github.io/fia/dg-comp-kartel-pristup-k-dokumentom/dgcomp-correspondence-full.html"
CELEX = "https://eur-lex.europa.eu/legal-content/{L}/TXT/?uri=CELEX:32001R1049"

# ═══════════════════ DÁTA KARTY — jediné miesto, kde sa niečo mení ═══════════════════

CARD = {
 "id":"case-dgcomp", "az":"EASE 2025/6534 · COMP/C5/LC/(2025)/6534", "ourref":"TFIA-2026-JV-009",
 "title":{"de":"Beschwerde wegen Kartellpraktiken — DG COMP","en":"Complaint about cartel practices — DG COMP",
   "sk":"Sťažnosť na kartelové praktiky — DG COMP","hr":"Pritužba zbog kartelnih praksi — DG COMP",
   "pl":"Skarga dotycząca praktyk kartelowych — DG COMP","es":"Denuncia por prácticas de cártel — DG COMP",
   "it":"Denuncia per pratiche di cartello — DG COMP","fr":"Plainte pour pratiques d'entente — DG COMP",
   "sv":"Klagomål om kartellpraxis — DG COMP"},
 "organ":{"de":"Europäische Kommission, GD Wettbewerb, Referat C.5 · Generalsekretariat, Referat Transparenz",
   "en":"European Commission, DG Competition, Unit C.5 · Secretariat-General, Transparency Unit",
   "sk":"Európska komisia, GR pre hospodársku súťaž, oddelenie C.5 · Generálny sekretariát, útvar Transparentnosť",
   "hr":"Europska komisija, Glavna uprava za tržišno natjecanje, odjel C.5 · Glavno tajništvo, Odjel za transparentnost",
   "pl":"Komisja Europejska, DG ds. Konkurencji, dział C.5 · Sekretariat Generalny, Dział Przejrzystości",
   "es":"Comisión Europea, DG Competencia, unidad C.5 · Secretaría General, Unidad de Transparencia",
   "it":"Commissione europea, DG Concorrenza, unità C.5 · Segretariato generale, Unità Trasparenza",
   "fr":"Commission européenne, DG Concurrence, unité C.5 · Secrétariat général, unité Transparence",
   "sv":"Europeiska kommissionen, GD Konkurrens, enhet C.5 · Generalsekretariatet, enheten för öppenhet"},
 "status":{"de":"Läuft","en":"Pending","sk":"Prebieha","hr":"U tijeku","pl":"W toku",
   "es":"En curso","it":"In corso","fr":"En cours","sv":"Pågår"},
}

def S(de,en,sk,hr,pl,es,it,fr,sv):
    return dict(zip(LANGS,[de,en,sk,hr,pl,es,it,fr,sv]))

ITEMS = [
 # ─────────────── ODOSLANÉ ───────────────
 dict(dir="odoslane", date="10.12.2025", msg=1, law=True,
   doc=REPO+"odoslane/01_Request_for_Access_to_Documents_M10815_KLON.pdf",
   qes=REPO+"odoslane/01_Request_for_Access_to_Documents_M10815_signed_with_QES.pdf",
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Erstantrag auf Dokumentenzugang — Fall M.10815",
          "Initial request for access to documents — Case M.10815",
          "Prvotná žiadosť o prístup k dokumentom — vec M.10815",
          "Prvi zahtjev za pristup dokumentima — predmet M.10815",
          "Pierwotny wniosek o dostęp do dokumentów — sprawa M.10815",
          "Solicitud inicial de acceso a documentos — asunto M.10815",
          "Domanda iniziale di accesso ai documenti — caso M.10815",
          "Demande initiale d'accès aux documents — affaire M.10815",
          "Ursprunglig ansökan om tillgång till handlingar — ärende M.10815")),
 dict(dir="odoslane", date="19.01.2026", msg=5, law=True,
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Antrag auf Fristverlängerung für den Zweitantrag",
          "Request for extension of the deadline for the confirmatory application",
          "Žiadosť o predĺženie lehoty na potvrdzovaciu žiadosť",
          "Zahtjev za produljenje roka za ponovni zahtjev",
          "Wniosek o przedłużenie terminu na wniosek potwierdzający",
          "Solicitud de prórroga del plazo para la solicitud confirmatoria",
          "Richiesta di proroga del termine per la domanda di conferma",
          "Demande de prorogation du délai pour la demande confirmative",
          "Begäran om förlängd frist för den bekräftande ansökan")),
 dict(dir="odoslane", date="30.01.2026", msg=7, law=True,
   doc=REPO+"odoslane/02_Confirmatory_Appeal_JV_Documents_signed_with_QES.pdf",
   qes=REPO+"odoslane/02_Confirmatory_Appeal_JV_Documents_signed_with_QES.pdf",
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Zweitantrag nach Art. 7 Abs. 2 VO 1049/2001",
          "Confirmatory application under Art. 7(2) of Reg. 1049/2001",
          "Potvrdzovacia žiadosť podľa čl. 7 ods. 2 nar. 1049/2001",
          "Ponovni zahtjev na temelju čl. 7. st. 2. Uredbe 1049/2001",
          "Wniosek potwierdzający na podstawie art. 7 ust. 2 rozp. 1049/2001",
          "Solicitud confirmatoria conforme al art. 7, apdo. 2, del Regl. 1049/2001",
          "Domanda di conferma ai sensi dell'art. 7, par. 2, del reg. 1049/2001",
          "Demande confirmative au titre de l'art. 7, par. 2, du règl. 1049/2001",
          "Bekräftande ansökan enligt art. 7.2 i förordning 1049/2001")),
 dict(dir="odoslane", date="08.02.2026", msg=10, law=True,
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Verfahrensrechtliche Klarstellung — Eingang am 26.01.2026",
          "Procedural clarification — filing of 26 January 2026",
          "Procesné objasnenie — podanie z 26.01.2026",
          "Postupovno pojašnjenje — podnesak od 26.01.2026.",
          "Wyjaśnienie proceduralne — złożenie z 26.01.2026",
          "Aclaración procedimental — presentación de 26.01.2026",
          "Chiarimento procedurale — deposito del 26.01.2026",
          "Clarification procédurale — dépôt du 26.01.2026",
          "Processuellt klargörande — ingivning den 26.01.2026")),
 dict(dir="odoslane", date="12.02.2026", msg=15,
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Strafanzeige — Art. 325 AEUV (Tracking 2428.022)",
          "Criminal complaint — Article 325 TFEU (Tracking 2428.022)",
          "Trestné oznámenie — čl. 325 ZFEÚ (Tracking 2428.022)",
          "Kaznena prijava — čl. 325. UFEU-a (Tracking 2428.022)",
          "Zawiadomienie o przestępstwie — art. 325 TFUE (Tracking 2428.022)",
          "Denuncia penal — art. 325 TFUE (Tracking 2428.022)",
          "Denuncia penale — art. 325 TFUE (Tracking 2428.022)",
          "Plainte pénale — art. 325 TFUE (Tracking 2428.022)",
          "Brottsanmälan — art. 325 FEUF (Tracking 2428.022)")),
 dict(dir="odoslane", date="19.07.2026", msg=17, law=True, hi=True,
   doc=REPO+"odoslane/12_Odpoved_DG-COMP_EASE-2025-6534_KLON_ALL.pdf",
   qes=REPO+"odoslane/12_Odpoved_DG-COMP_EASE-2025-6534_signed_with_QES.pdf",
   badge=S("Zugestellt","Delivered","Doručené","Dostavljeno","Doręczono","Entregado","Consegnato","Remis","Levererat"),
   subj=S("Antwort auf den Beschluss über die Zugangsverweigerung — TFIA-2026-JV-009",
          "Reply to the decision refusing access — TFIA-2026-JV-009",
          "Odpoveď na rozhodnutie o odmietnutí prístupu — TFIA-2026-JV-009",
          "Odgovor na odluku o odbijanju pristupa — TFIA-2026-JV-009",
          "Odpowiedź na decyzję o odmowie dostępu — TFIA-2026-JV-009",
          "Respuesta a la decisión de denegación de acceso — TFIA-2026-JV-009",
          "Risposta alla decisione di diniego di accesso — TFIA-2026-JV-009",
          "Réponse à la décision de refus d'accès — TFIA-2026-JV-009",
          "Svar på beslutet att neka tillgång — TFIA-2026-JV-009")),
 # ─────────────── PRIJATÉ ───────────────
 dict(dir="prijate", date="10.12.2025", msg=2,
   badge=S("Registriert","Registered","Zaevidované","Evidentirano","Zarejestrowano","Registrado","Registrato","Enregistré","Registrerat"),
   subj=S("Eingangsbestätigung — Aktenzeichen 2025/6534",
          "Acknowledgement of receipt — case number 2025/6534",
          "Potvrdenie o prijatí — číslo veci 2025/6534",
          "Potvrda primitka — broj predmeta 2025/6534",
          "Potwierdzenie wpływu — numer sprawy 2025/6534",
          "Acuse de recibo — número de asunto 2025/6534",
          "Conferma di ricezione — numero di pratica 2025/6534",
          "Accusé de réception — numéro de dossier 2025/6534",
          "Mottagningsbekräftelse — ärendenummer 2025/6534")),
 dict(dir="prijate", date="07.01.2026", msg=4, law=True, hi=True,
   doc=REPO+"prijate/11_EASE_2025-6534_KLON_ALL.pdf",
   orig=REPO+"prijate/11_EASE_2025-6534_DG-COMP_EN_ORIGINAL.pdf",
   badge=S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag"),
   subj=S("Ablehnung des Dokumentenzugangs — EASE 2025/6534, unterzeichnet vom Generaldirektor",
          "Refusal of access to documents — EASE 2025/6534, signed by the Director-General",
          "Zamietnutie prístupu k dokumentom — EASE 2025/6534, podpísané generálnym riaditeľom",
          "Odbijanje pristupa dokumentima — EASE 2025/6534, potpisao glavni direktor",
          "Odmowa dostępu do dokumentów — EASE 2025/6534, podpisana przez dyrektora generalnego",
          "Denegación de acceso a documentos — EASE 2025/6534, firmada por la Directora General",
          "Diniego di accesso ai documenti — EASE 2025/6534, firmato dal Direttore generale",
          "Refus d'accès aux documents — EASE 2025/6534, signé par la directrice générale",
          "Avslag på tillgång till handlingar — EASE 2025/6534, undertecknat av generaldirektören")),
 dict(dir="prijate", date="20.01.2026", msg=6, law=True,
   badge=S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag"),
   subj=S("Fristverlängerung nicht möglich — Art. 7 Abs. 2 steht nicht zur Disposition",
          "Extension not possible — Art. 7(2) not at the parties' disposal",
          "Predĺženie lehoty nie je možné — čl. 7 ods. 2 nie je k dispozícii stranám",
          "Produljenje roka nije moguće — čl. 7. st. 2. nije na raspolaganju strankama",
          "Przedłużenie niemożliwe — art. 7 ust. 2 nie pozostaje w dyspozycji stron",
          "Prórroga imposible — el art. 7, apdo. 2, no está a disposición de las partes",
          "Proroga non possibile — l'art. 7, par. 2, non è nella disponibilità delle parti",
          "Prorogation impossible — l'art. 7, par. 2, n'est pas à la disposition des parties",
          "Förlängning inte möjlig — art. 7.2 står inte till parternas förfogande")),
 dict(dir="prijate", date="03.02.2026", msg=8,
   badge=S("Weitergeleitet","Forwarded","Postúpené","Proslijeđeno","Przekazano","Remitido","Trasmesso","Transmis","Vidarebefordrat"),
   subj=S("COMP C-5 bestätigt Eingang und leitet an das Generalsekretariat weiter",
          "COMP C-5 acknowledges receipt and forwards to the Secretariat-General",
          "COMP C-5 potvrdzuje prijatie a postupuje Generálnemu sekretariátu",
          "COMP C-5 potvrđuje primitak i prosljeđuje Glavnom tajništvu",
          "COMP C-5 potwierdza wpływ i przekazuje Sekretariatowi Generalnemu",
          "COMP C-5 acusa recibo y remite a la Secretaría General",
          "COMP C-5 accusa ricevuta e trasmette al Segretariato generale",
          "COMP C-5 accuse réception et transmet au Secrétariat général",
          "COMP C-5 bekräftar mottagandet och vidarebefordrar till generalsekretariatet")),
 dict(dir="prijate", date="03.02.2026", msg=9, law=True, hi=True,
   badge=S("Als verspätet zurückgewiesen","Rejected as out of time","Zamietnuté ako oneskorené",
           "Odbačeno kao nepravodobno","Odrzucone jako spóźnione","Rechazado por extemporáneo",
           "Respinto perché tardivo","Rejeté comme tardif","Avvisad som för sent inkommen"),
   subj=S("Generalsekretariat weist den Zweitantrag als verspätet zurück — Ares(2026)1214166",
          "Secretariat-General rejects the confirmatory application as out of time — Ares(2026)1214166",
          "Generálny sekretariát zamieta potvrdzovaciu žiadosť ako oneskorenú — Ares(2026)1214166",
          "Glavno tajništvo odbacuje ponovni zahtjev kao nepravodoban — Ares(2026)1214166",
          "Sekretariat Generalny odrzuca wniosek potwierdzający jako spóźniony — Ares(2026)1214166",
          "La Secretaría General rechaza la solicitud confirmatoria por extemporánea — Ares(2026)1214166",
          "Il Segretariato generale respinge la domanda di conferma perché tardiva — Ares(2026)1214166",
          "Le Secrétariat général rejette la demande confirmative comme tardive — Ares(2026)1214166",
          "Generalsekretariatet avvisar den bekräftande ansökan som för sent inkommen — Ares(2026)1214166")),
 dict(dir="prijate", date="10.02.2026", msg=12,
   badge=S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag"),
   subj=S("Kommission verweist auf das offizielle Portal — keine Haftung für Websites Dritter",
          "Commission refers to the official portal — no liability for third-party websites",
          "Komisia odkazuje na oficiálny portál — za stránky tretích strán nezodpovedá",
          "Komisija upućuje na službeni portal — ne odgovara za stranice trećih osoba",
          "Komisja odsyła do oficjalnego portalu — nie odpowiada za strony podmiotów trzecich",
          "La Comisión remite al portal oficial — sin responsabilidad por sitios de terceros",
          "La Commissione rinvia al portale ufficiale — nessuna responsabilità per siti di terzi",
          "La Commission renvoie au portail officiel — aucune responsabilité pour les sites de tiers",
          "Kommissionen hänvisar till den officiella portalen — inget ansvar för tredje parters webbplatser")),
]

UI = {
 "sent":      S("Gesendet","Sent","Odoslané","Poslano","Wysłane","Enviados","Inviati","Envoyés","Skickat"),
 "received":  S("Eingegangen","Received","Prijaté","Primljeno","Otrzymane","Recibidos","Ricevuti","Reçus","Mottaget"),
 "doc":       S("Dokument","Document","Dokument","Dokument","Dokument","Documento","Documento","Document","Handling"),
 "qes":       S("Signiertes Original (QES)","Signed original (QES)","Podpísaný originál (QES)","Potpisani izvornik (QES)",
                "Podpisany oryginał (QES)","Original firmado (QES)","Originale firmato (QES)","Original signé (QES)","Signerat original (QES)"),
 "orig":      S("Original","Original","Originál","Izvornik","Oryginał","Original","Originale","Original","Original"),
 "text":      S("Wortlaut","Full text","Znenie","Tekst","Treść","Texto","Testo","Texte","Lydelse"),
 "law":       S("Vorschrift","Legal basis","Predpis","Propis","Przepis","Norma","Norma","Texte légal","Föreskrift"),
 "corr":      S("Vollständiger Schriftverkehr","Full correspondence","Celá komunikácia","Cjelovita korespondencija",
                "Pełna korespondencja","Correspondencia completa","Corrispondenza completa","Correspondance complète","Fullständig korrespondens"),
 "anal":      S("Worin die Kommission gefehlt hat","Where the Commission erred","Kde Komisia pochybila","U čemu je Komisija pogriješila",
                "W czym Komisja uchybiła","En qué erró la Comisión","In che cosa la Commissione ha errato","En quoi la Commission a failli","Var kommissionen har brustit"),
 "az":        S("Aktenzeichen","File ref.","Spisová značka","Poslovni broj","Sygnatura","Referencia","Riferimento","Référence","Ärendenummer"),
 "ourref":    S("Unser Zeichen","Our ref.","Naša značka","Naš broj","Nasza sygn.","Ntra. ref.","Ns. rif.","Notre réf.","Vårt nr"),
}

# ═══════════════════ ŠABLÓNA — obsah sa jej netýka ═══════════════════

def g(d, block=False):
    c = "gtl-b" if block else "gtl"
    return "".join(f'<span class="{c} {L}">{d[L]}</span>' for L in LANGS)

def item_html(it, n):
    b = []
    if it.get("doc"):
        b.append(f'<a class="b b-doc" href="{it["doc"]}" target="_blank" rel="noopener">📄 {g(UI["doc"])}</a>')
    if it.get("qes"):
        b.append(f'<a class="b b-qes" href="{it["qes"]}" target="_blank" rel="noopener">✍ {g(UI["qes"])}</a>')
    if it.get("orig"):
        b.append(f'<a class="b b-qes" href="{it["orig"]}" target="_blank" rel="noopener">📎 {g(UI["orig"])}</a>')
    b.append(f'<a class="b b-txt" href="{CORR}#msg-{it["msg"]}" target="_blank" rel="noopener">📑 {g(UI["text"])}</a>')
    if it.get("law"):
        b.append('<a class="b b-law" href="#" data-celex="1" '
                 + "".join(f'data-{L}="{CELEX.format(L=L.upper())}" ' for L in LANGS)
                 + f'target="_blank" rel="noopener">⚖ {g(UI["law"])}</a>')
    hi = " hi" if it.get("hi") else ""
    return (f'<div class="item{hi}"><div class="itop"><span class="idate">{it["date"]}</span>'
            f'<span class="ibadge">{g(it["badge"])}</span></div>'
            f'<div class="isubj">{g(it["subj"])}</div>'
            f'<div class="ibtns">{"".join(b)}</div></div>')

sent = "".join(item_html(i,n) for n,i in enumerate(x for x in ITEMS if x["dir"]=="odoslane"))
recv = "".join(item_html(i,n) for n,i in enumerate(x for x in ITEMS if x["dir"]=="prijate"))
flags = "".join(f'<button class="f{" on" if L=="sk" else ""}" data-l="{L}">'
                f'<img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in LANGS)

HTML = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>PROTOTYP — karta konania DG COMP</title>
<style>
:root{{--navy:#1F3864;--red:#C00000;--bg:#f4f6f9;--bd:#dfe5ec;--ink:#22303f}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 18px 60px}}
#bar{{position:sticky;top:0;z-index:20;background:var(--navy);color:#fff}}
#bar .in{{max-width:1180px;margin:0 auto;padding:9px 18px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
#bar .nm{{font-weight:700;letter-spacing:.02em}}
#bar a{{color:#fff;text-decoration:none;font-size:13px;border-bottom:1px solid rgba(255,255,255,.45)}}
#bar a:hover{{border-bottom-color:#fff}}
.f{{background:none;border:0;padding:0;cursor:pointer;width:26px;height:18px;opacity:.5;border-radius:2px;overflow:hidden}}
.f img{{width:26px;height:18px;object-fit:cover;display:block}}
.f.on{{opacity:1;outline:2px solid #ffd34d}}
.proto{{background:#fff4cc;border:1px solid #f0c040;border-left:5px solid var(--red);
 padding:12px 16px;margin:18px 0;border-radius:4px;font-size:13.5px}}
.head{{background:#fff;border:1px solid var(--bd);border-top:4px solid var(--navy);
 border-radius:5px;padding:22px 26px;margin-bottom:18px}}
.head h1{{margin:0 0 8px;font-size:23px;color:var(--navy);letter-spacing:-.01em;line-height:1.3}}
.head .org{{font-size:13.5px;color:#5a6a7d;margin-bottom:12px}}
.head .meta{{font-size:12.5px;color:#5a6a7d;border-top:1px solid var(--bd);padding-top:10px}}
.head .meta b{{color:var(--navy)}}
.pill{{display:inline-block;background:#fff3d6;color:#8a5a00;border:1px solid #f0c040;
 border-radius:999px;padding:2px 12px;font-size:12px;font-weight:700;margin-left:8px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
@media(max-width:860px){{.cols{{grid-template-columns:1fr}}}}
.col h2{{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:.09em;color:#7a8899}}
.item{{background:#fff;border:1px solid var(--bd);border-radius:5px;padding:13px 16px;margin-bottom:10px}}
.item.hi{{border-left:4px solid var(--red)}}
.itop{{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:5px}}
.idate{{font-size:12px;color:#7a8899;font-weight:700}}
.ibadge{{font-size:11px;background:#eef2f7;color:#54637a;border-radius:3px;padding:1px 8px;white-space:nowrap}}
.isubj{{font-size:14.5px;color:var(--navy);font-weight:600;margin-bottom:9px;line-height:1.4}}
.ibtns{{display:flex;flex-wrap:wrap;gap:6px}}
.b{{font-size:11.5px;text-decoration:none;border:1px solid var(--bd);border-radius:3px;
 padding:3px 9px;color:#3d4d5e;background:#fbfcfd;white-space:nowrap}}
.b:hover{{border-color:var(--navy);color:var(--navy)}}
.b-qes{{background:#fff8e6;border-color:#f0c040;color:#8a5a00}}
.b-txt{{background:#eef4ff;border-color:#c3d5f5;color:#1F3864}}
.foot{{margin-top:26px;padding-top:14px;border-top:1px solid var(--bd);font-size:12.5px;color:#7a8899}}
.gtl,.gtl-b{{display:none}}
{"".join(f'body[data-l="{L}"] .gtl.{L}{{display:inline}}body[data-l="{L}"] .gtl-b.{L}{{display:block}}' for L in LANGS)}
</style></head>
<body data-l="sk">

<div id="bar"><div class="in">
 <span class="nm">FIA FOX · PROTOTYP</span>
 {flags}
 <a href="{CORR}" target="_blank" rel="noopener">📑 {g(UI["corr"])}</a>
 <a href="{CORR}#anal" target="_blank" rel="noopener">⚖ {g(UI["anal"])}</a>
</div></div>

<div class="wrap">

<div class="proto"><b>PROTOTYP — mimo WordPressu.</b>
<span class="gtl-b sk">Toto je ukážka, ako by karta konania vyzerala, keby sa generovala z dát namiesto ručného písania do stránky #303. Ostrá karta na foxprof.club beží ďalej nezmenená; táto stránka do nej nijako nezasahuje. Obsahuje celý doložený tok konania — dvanásť položiek namiesto štyroch, ktoré sú dnes na karte.</span>
<span class="gtl-b de">Muster dafür, wie die Verfahrensakte aussähe, wenn sie aus Daten erzeugt würde. Die Live-Karte bleibt unverändert.</span>
<span class="gtl-b en">A demonstration of how the case card would look if generated from data. The live card remains untouched.</span>
<span class="gtl-b hr">Ogledni primjer kartice predmeta generirane iz podataka. Aktivna kartica ostaje netaknuta.</span>
<span class="gtl-b pl">Przykład karty sprawy generowanej z danych. Karta produkcyjna pozostaje nietknięta.</span>
<span class="gtl-b es">Demostración de la ficha del asunto generada a partir de datos. La ficha en producción no se altera.</span>
<span class="gtl-b it">Dimostrazione della scheda del caso generata dai dati. La scheda in produzione resta intatta.</span>
<span class="gtl-b fr">Démonstration de la fiche d'affaire générée à partir de données. La fiche en production reste intacte.</span>
<span class="gtl-b sv">Demonstration av ärendekortet genererat från data. Det aktiva kortet lämnas orört.</span>
</div>

<div class="head">
 <h1>{g(CARD["title"])}<span class="pill">{g(CARD["status"])}</span></h1>
 <div class="org">{g(CARD["organ"])}</div>
 <div class="meta"><b>{g(UI["az"])}:</b> {CARD["az"]} &nbsp;·&nbsp;
  <b>{g(UI["ourref"])}:</b> {CARD["ourref"]} &nbsp;·&nbsp; 10.12.2025 → 19.07.2026 &nbsp;·&nbsp; {len(ITEMS)} </div>
</div>

<div class="cols">
 <div class="col"><h2>▲ {g(UI["sent"])}</h2>{sent}</div>
 <div class="col"><h2>▼ {g(UI["received"])}</h2>{recv}</div>
</div>

<div class="foot">FIA FOX — prototyp karty konania · dáta a šablóna oddelené · zmena položky = jeden riadok v dátach</div>
</div>

<script>
document.querySelectorAll('.f').forEach(function(b){{
  b.addEventListener('click',function(){{
    var L=b.dataset.l; document.body.dataset.l=L; document.documentElement.lang=L;
    document.querySelectorAll('.f').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on');
    document.querySelectorAll('a[data-celex]').forEach(function(a){{ a.href=a.dataset[L]; }});
  }});
}});
document.querySelectorAll('a[data-celex]').forEach(function(a){{ a.href=a.dataset.sk; }});
</script>
</body></html>"""

open('dgcomp-karta-prototyp.html','w',encoding='utf-8').write(HTML)
print("prototyp:", len(HTML), "znakov |", len(ITEMS), "poloziek |", len(LANGS), "jazykov")
