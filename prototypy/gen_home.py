#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROTOTYP — Home stranka: KAUZY -> KONANIA. Mimo WordPressu, nezasahuje do #303.
   Darovaci portal ostava na WordPresse (GiveWP), Home nan len odkazuje v jazyku vlajky."""

LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"]
FLAG  = {"de":"de","en":"gb","sk":"sk","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
WP    = "https://foxprof.club/"

# ── existujuci darovaci portal na WordPresse (GiveWP), 9 jazykovych stranok ──
DAR = {
 "de":"fia-fox-fur-gunstigeres-kartellfreies-internet-in-europa/",
 "en":"fia-fox-for-a-fairer-cartel-free-internet-in-europe/",
 "sk":"fia-fox-za-ferovejsi-internet-bez-kartelov-v-europe/",
 "hr":"fia-fox-za-jeftiniji-internet-bez-kartela-u-europi/",
 "pl":"fia-fox-za-tanszy-internet-bez-karteli-w-europie/",
 "es":"fia-fox-por-un-internet-mas-barato-sin-carteles-en-europa/",
 "it":"fia-fox-per-un-internet-piu-economico-senza-cartelli-in-europa/",
 "fr":"fia-fox-pour-un-internet-moins-cher-sans-cartels-en-europe/",
 "sv":"fia-fox-for-ett-billigare-internet-utan-karteller-i-europa/",
}
UVOD = {"de":"willkommen/","en":"welcome/","sk":"164-2/","hr":"dobrodosli/","pl":"witamy/",
        "es":"bienvenidos/","it":"benvenuti/","fr":"bienvenue/","sv":"209-2/"}

def S(de,en,sk,hr,pl,es,it,fr,sv): return dict(zip(LANGS,[de,en,sk,hr,pl,es,it,fr,sv]))

# ═══════════════ DÁTA: KAUZY → KONANIA ═══════════════
# hotovo=URL karty (prototyp), inak None = pripravuje sa

KAUZY = [
 dict(kod="k-jv", n=2,
   nazov=S("Telekom-Kartell und Gemeinschaftsunternehmen M.10815",
           "Telecoms cartel and the M.10815 joint venture",
           "Telekomunikačný kartel a spoločný podnik M.10815",
           "Telekomunikacijski kartel i zajednički pothvat M.10815",
           "Kartel telekomunikacyjny i wspólne przedsiębiorstwo M.10815",
           "Cártel de telecomunicaciones y la empresa común M.10815",
           "Cartello delle telecomunicazioni e l'impresa comune M.10815",
           "Entente dans les télécoms et l'entreprise commune M.10815",
           "Telekomkartellen och det gemensamma företaget M.10815"),
   popis=S("Nichtigkeitsklage gegen den Beschluss der Kommission und der Kampf um den Zugang zur Akte.",
           "Action for annulment of the Commission decision and the fight for access to the file.",
           "Žaloba o neplatnosť rozhodnutia Komisie a zápas o prístup k spisu.",
           "Tužba za poništenje odluke Komisije i borba za pristup spisu.",
           "Skarga o stwierdzenie nieważności decyzji Komisji i walka o dostęp do akt.",
           "Recurso de anulación de la decisión de la Comisión y la lucha por el acceso al expediente.",
           "Ricorso di annullamento della decisione della Commissione e la lotta per l'accesso al fascicolo.",
           "Recours en annulation de la décision de la Commission et la lutte pour l'accès au dossier.",
           "Talan om ogiltigförklaring av kommissionens beslut och kampen om aktinsyn."),
   konania=[
     dict(org="Všeobecný súd Európskej únie", az="T-61/26", stav="laeuft",
          nazov="Nichtigkeitsklage M.10815 · Art. 263 AEUV", url=None),
     dict(org="Európska komisia — DG COMP · Generálny sekretariát", az="EASE 2025/6534 · TFIA-2026-JV-009",
          stav="laeuft", nazov="Zugang zu Dokumenten · VO 1049/2001",
          url="dgcomp-karta-prototyp.html"),
   ]),
 dict(kod="k-dt", n=3,
   nazov=S("Deutsche Telekom, Schufa und Credit Scoring","Deutsche Telekom, Schufa and credit scoring",
           "Deutsche Telekom, Schufa a credit scoring","Deutsche Telekom, Schufa i kreditni scoring",
           "Deutsche Telekom, Schufa i scoring kredytowy","Deutsche Telekom, Schufa y la calificación crediticia",
           "Deutsche Telekom, Schufa e il credit scoring","Deutsche Telekom, Schufa et le score de crédit",
           "Deutsche Telekom, Schufa och kreditbedömning"),
   popis=S("Verweigerter Internetzugang aufgrund automatisierter Bewertung — Zivil-, Straf- und Aufsichtsverfahren.",
           "Internet access refused on the basis of automated scoring — civil, criminal and regulatory proceedings.",
           "Odmietnutý prístup k internetu na základe automatizovaného hodnotenia — civilné, trestné a dozorné konania.",
           "Odbijen pristup internetu na temelju automatizirane ocjene — građanski, kazneni i nadzorni postupci.",
           "Odmowa dostępu do internetu na podstawie oceny automatycznej — postępowania cywilne, karne i nadzorcze.",
           "Acceso a internet denegado por calificación automatizada — procedimientos civiles, penales y de supervisión.",
           "Accesso a internet negato per valutazione automatizzata — procedimenti civili, penali e di vigilanza.",
           "Accès à internet refusé sur la base d'un score automatisé — procédures civiles, pénales et de contrôle.",
           "Nekad internetåtkomst på grund av automatiserad bedömning — tviste-, brott- och tillsynsärenden."),
   konania=[
     dict(org="Landgericht Landshut", az="91 O 2699/24 (pôv. 23 O 2699/24)", stav="laeuft",
          nazov="Klage gegen Deutsche Telekom AG und Schufa Holding AG", url=None),
     dict(org="Polizeiinspektion / StA Landshut", az="709 AR 303/24 601", stav="abgelehnt",
          nazov="Strafrechtliche Mitteilung — Telekom und Schufa", url=None),
     dict(org="O2 Telefónica / Bundesnetzagentur", az="—", stav="laeuft",
          nazov="Deaktivierung der SIM-Karte", url=None),
   ]),
 dict(kod="k-ms", n=2,
   nazov=S("Microsoft — DSGVO und finanzielle Interessen der EU","Microsoft — GDPR and the EU's financial interests",
           "Microsoft — GDPR a finančné záujmy EÚ","Microsoft — GDPR i financijski interesi EU-a",
           "Microsoft — RODO i interesy finansowe UE","Microsoft — RGPD e intereses financieros de la UE",
           "Microsoft — GDPR e interessi finanziari dell'UE","Microsoft — RGPD et intérêts financiers de l'UE",
           "Microsoft — dataskydd och EU:s ekonomiska intressen"),
   popis=S("Beschwerde bei der Aufsichtsbehörde und Anzeige bei der Europäischen Staatsanwaltschaft.",
           "Complaint to the supervisory authority and report to the European Public Prosecutor's Office.",
           "Sťažnosť dozornému orgánu a oznámenie Európskej prokuratúre.",
           "Pritužba nadzornom tijelu i prijava Uredu europskog javnog tužitelja.",
           "Skarga do organu nadzorczego i zawiadomienie Prokuratury Europejskiej.",
           "Reclamación ante la autoridad de control y denuncia ante la Fiscalía Europea.",
           "Reclamo all'autorità di controllo e denuncia alla Procura europea.",
           "Réclamation auprès de l'autorité de contrôle et signalement au Parquet européen.",
           "Klagomål till tillsynsmyndigheten och anmälan till Europeiska åklagarmyndigheten."),
   konania=[
     dict(org="Data Protection Commission Ireland", az="DPC0526916540 · PIF-EU-2026-MBS-004", stav="laeuft",
          nazov="Beschwerde nach Art. 77 DSGVO", url=None),
     dict(org="Európska prokuratúra (EPPO)", az="PIF-EU-2026-MBS-002 · P.000800/2026", stav="laeuft",
          nazov="Strafanzeige — Art. 325 AEUV", url=None),
   ]),
 dict(kod="k-bank", n=1,
   nazov=S("Banken und Zugang zum Basiskonto","Banks and access to a basic payment account",
           "Banky a prístup k platobnému účtu","Banke i pristup osnovnom računu",
           "Banki i dostęp do podstawowego rachunku","Bancos y acceso a la cuenta de pago básica",
           "Banche e accesso al conto di base","Banques et accès au compte de paiement de base",
           "Banker och tillgång till betalkonto"),
   popis=S("ZKG-Verfahren gegen die Commerzbank vor der BaFin.","ZKG proceedings against Commerzbank before BaFin.",
           "Konanie podľa ZKG proti Commerzbank pred BaFin.","Postupak po ZKG protiv Commerzbank pred BaFin-om.",
           "Postępowanie ZKG przeciwko Commerzbank przed BaFin.","Procedimiento ZKG contra Commerzbank ante BaFin.",
           "Procedimento ZKG contro Commerzbank dinanzi alla BaFin.","Procédure ZKG contre Commerzbank devant la BaFin.",
           "ZKG-förfarande mot Commerzbank vid BaFin."),
   konania=[
     dict(org="BaFin Bonn · Commerzbank AG", az="TFIA-2026-JV-010", stav="laeuft",
          nazov="Zahlungskontengesetz — Verfahren", url=None),
   ]),
 dict(kod="k-zdrav", n=3,
   nazov=S("Krankenversicherung und Vollstreckung","Health insurance and enforcement",
           "Zdravotné poistenie a exekúcie","Zdravstveno osiguranje i ovrha",
           "Ubezpieczenie zdrowotne i egzekucja","Seguro de enfermedad y ejecución",
           "Assicurazione sanitaria ed esecuzione","Assurance maladie et exécution forcée",
           "Sjukförsäkring och verkställighet"),
   popis=S("Vollstreckung ohne Schuld und Eingriffe in Vermögensrechte in Deutschland und der Slowakei.",
           "Enforcement without debt and interference with property rights in Germany and Slovakia.",
           "Exekúcia bez dlhu a zásahy do majetkových práv v Nemecku a na Slovensku.",
           "Ovrha bez duga i zadiranje u imovinska prava u Njemačkoj i Slovačkoj.",
           "Egzekucja bez długu i ingerencja w prawa majątkowe w Niemczech i na Słowacji.",
           "Ejecución sin deuda e injerencia en derechos patrimoniales en Alemania y Eslovaquia.",
           "Esecuzione senza debito e interferenze nei diritti patrimoniali in Germania e Slovacchia.",
           "Exécution sans dette et atteintes aux droits patrimoniaux en Allemagne et en Slovaquie.",
           "Verkställighet utan skuld och ingrepp i egendomsrätt i Tyskland och Slovakien."),
   konania=[
     dict(org="Staatsanwaltschaft Hamburg · Hauptzollamt", az="—", stav="laeuft",
          nazov="DAK — Strafanzeige und Einwendung gegen die Vollstreckung", url=None),
     dict(org="ÚDZS Slovensko", az="12479/2026/911 · PO 1328/2026", stav="laeuft",
          nazov="Nezákonná exekúcia za nulový dlh", url=None),
     dict(org="Okresný súd Bratislava V", az="156EX-171/25", stav="laeuft",
          nazov="Žaloba o náhradu škody", url=None),
   ]),
 dict(kod="k-spravne", n=3,
   nazov=S("Verwaltungs- und Strafverfahren","Administrative and criminal proceedings",
           "Správne a trestné konania","Upravni i kazneni postupci",
           "Postępowania administracyjne i karne","Procedimientos administrativos y penales",
           "Procedimenti amministrativi e penali","Procédures administratives et pénales",
           "Förvaltnings- och brottmålsförfaranden"),
   popis=S("Bußgeld, Erzwingungshaft und Anzeige gegen Staatsanwälte.",
           "Administrative fine, coercive detention and a complaint against prosecutors.",
           "Pokuta, Erzwingungshaft a trestné oznámenie na prokurátorov.",
           "Novčana kazna, prisilni pritvor i prijava protiv državnih odvjetnika.",
           "Grzywna, areszt przymuszający i zawiadomienie na prokuratorów.",
           "Multa, arresto coercitivo y denuncia contra fiscales.",
           "Sanzione, arresto coercitivo e denuncia contro i procuratori.",
           "Amende, contrainte par corps et plainte contre des procureurs.",
           "Böter, tvångshäkte och anmälan mot åklagare."),
   konania=[
     dict(org="Landratsamt Landshut", az="30-8223.1 AD", stav="laeuft",
          nazov="Nezákonne uložená pokuta", url=None),
     dict(org="Landgericht Landshut — Strafsachen", az="2 Qs 80/25", stav="laeuft",
          nazov="Sofortige Beschwerde gegen Erzwingungshaft", url=None),
     dict(org="Generálna prokuratúra SR", az="—", stav="laeuft",
          nazov="Trestné oznámenie na prokurátorov", url=None),
   ]),
]

STAV = {"laeuft": S("Läuft","Pending","Prebieha","U tijeku","W toku","En curso","In corso","En cours","Pågår"),
        "abgelehnt": S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag")}

UI = {
 "tag": S("Bürgerinitiative für ein kartellfreies Internet in Europa",
          "Citizens' initiative for a cartel-free internet in Europe",
          "Občianska iniciatíva za internet bez kartelov v Európe",
          "Građanska inicijativa za internet bez kartela u Europi",
          "Inicjatywa obywatelska na rzecz internetu bez karteli w Europie",
          "Iniciativa ciudadana por un internet sin cárteles en Europa",
          "Iniziativa dei cittadini per un internet senza cartelli in Europa",
          "Initiative citoyenne pour un internet sans ententes en Europe",
          "Medborgarinitiativ för ett internet utan karteller i Europa"),
 "kauzy": S("Fälle","Cases","Kauzy","Predmeti","Sprawy","Casos","Casi","Affaires","Ärenden"),
 "konania": S("Verfahren","Proceedings","Konania","Postupci","Postępowania","Procedimientos","Procedimenti","Procédures","Förfaranden"),
 "open": S("Akte öffnen","Open the file","Otvoriť kartu","Otvori karticu","Otwórz kartę","Abrir la ficha","Apri la scheda","Ouvrir la fiche","Öppna kortet"),
 "soon": S("in Vorbereitung","in preparation","pripravuje sa","u pripremi","w przygotowaniu","en preparación","in preparazione","en préparation","under förberedelse"),
 "dar": S("Unterstützen","Support","Podporiť","Podrži","Wesprzyj","Apoyar","Sostieni","Soutenir","Stöd"),
 "uvod": S("Über die Initiative","About the initiative","O iniciatíve","O inicijativi","O inicjatywie","Sobre la iniciativa","Sull'iniziativa","À propos de l'initiative","Om initiativet"),
 "imp": S("Impressum","Legal notice","Impressum","Impressum","Nota prawna","Aviso legal","Note legali","Mentions légales","Rättslig information"),
 "gdpr": S("Datenschutz","Privacy","Ochrana údajov","Zaštita podataka","Ochrona danych","Protección de datos","Protezione dei dati","Confidentialité","Dataskydd"),
}

# ═══════════════ ŠABLÓNA ═══════════════

def g(d, b=False):
    c = "gtl-b" if b else "gtl"
    return "".join(f'<span class="{c} {L}">{d[L]}</span>' for L in LANGS)

def kon_html(k):
    if k["url"]:
        btn = f'<a class="go" href="{k["url"]}">{g(UI["open"])} →</a>'
    else:
        btn = f'<span class="soon">{g(UI["soon"])}</span>'
    return (f'<div class="kon"><div class="kmain"><div class="knaz">{k["nazov"]}</div>'
            f'<div class="korg">{k["org"]} &nbsp;·&nbsp; <b>{k["az"]}</b></div></div>'
            f'<div class="kside"><span class="st st-{k["stav"]}">{g(STAV[k["stav"]])}</span>{btn}</div></div>')

def kauza_html(z):
    return (f'<section class="kauza"><div class="khead"><h2>{g(z["nazov"])}</h2>'
            f'<span class="cnt">{z["n"]} {g(UI["konania"])}</span></div>'
            f'<p class="kpop">{g(z["popis"])}</p>'
            f'{"".join(kon_html(k) for k in z["konania"])}</section>')

flags = "".join(f'<button class="f{" on" if L=="sk" else ""}" data-l="{L}">'
                f'<img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in LANGS)
show = "".join(f'body[data-l="{L}"] .gtl.{L}{{display:inline}}body[data-l="{L}"] .gtl-b.{L}{{display:block}}' for L in LANGS)
total = sum(z["n"] for z in KAUZY)

HTML = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>PROTOTYP — FIA FOX</title>
<style>
:root{{--navy:#1F3864;--red:#C00000;--bg:#f4f6f9;--bd:#dfe5ec;--ink:#22303f}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif}}
a{{color:inherit}}
#bar{{position:sticky;top:0;z-index:20;background:var(--navy);color:#fff}}
#bar .in{{max-width:1100px;margin:0 auto;padding:9px 18px;display:flex;align-items:center;gap:13px;flex-wrap:wrap}}
#bar .nm{{font-weight:700;letter-spacing:.02em}}
#bar a{{color:#fff;text-decoration:none;font-size:13px;border-bottom:1px solid rgba(255,255,255,.45)}}
#bar a:hover{{border-bottom-color:#fff}}
#bar .dar{{background:#ffd34d;color:#3a2c00;border:0;border-radius:3px;padding:3px 12px;font-weight:700}}
.f{{background:none;border:0;padding:0;cursor:pointer;width:25px;height:17px;opacity:.5;border-radius:2px;overflow:hidden}}
.f img{{width:25px;height:17px;object-fit:cover;display:block}}
.f.on{{opacity:1;outline:2px solid #ffd34d}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 18px 60px}}
.proto{{background:#fff4cc;border:1px solid #f0c040;border-left:5px solid var(--red);
 padding:12px 16px;margin:18px 0;border-radius:4px;font-size:13.5px}}
.hero{{background:var(--navy);color:#fff;border-radius:6px;padding:34px 34px 30px;margin-bottom:22px}}
.hero h1{{margin:0 0 8px;font-size:34px;letter-spacing:-.02em}}
.hero .tag{{font-size:15px;opacity:.9}}
.hero .nums{{margin-top:18px;padding-top:14px;border-top:1px solid rgba(255,255,255,.25);font-size:13px;opacity:.9}}
.hero .nums b{{font-size:20px;color:#ffd34d;margin-right:5px}}
.kauza{{background:#fff;border:1px solid var(--bd);border-radius:6px;padding:20px 24px;margin-bottom:16px}}
.khead{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}}
.kauza h2{{margin:0;font-size:19px;color:var(--navy);letter-spacing:-.01em}}
.cnt{{font-size:11.5px;color:#7a8899;text-transform:uppercase;letter-spacing:.07em;white-space:nowrap}}
.kpop{{margin:6px 0 16px;font-size:13.5px;color:#5a6a7d}}
.kon{{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;
 border-top:1px solid var(--bd);padding:11px 0}}
.knaz{{font-size:14.5px;color:var(--navy);font-weight:600}}
.korg{{font-size:12.5px;color:#7a8899;margin-top:2px}}
.kside{{display:flex;align-items:center;gap:10px}}
.st{{font-size:11px;border-radius:999px;padding:2px 10px;white-space:nowrap}}
.st-laeuft{{background:#fff3d6;color:#8a5a00;border:1px solid #f0c040}}
.st-abgelehnt{{background:#fde8e8;color:#8a1c1c;border:1px solid #e8b4b4}}
.go{{font-size:12.5px;text-decoration:none;background:var(--navy);color:#fff;border-radius:3px;padding:4px 12px;white-space:nowrap}}
.go:hover{{background:#16294a}}
.soon{{font-size:12px;color:#9aa7b5;white-space:nowrap}}
.foot{{margin-top:26px;padding-top:14px;border-top:1px solid var(--bd);font-size:12.5px;color:#7a8899;
 display:flex;gap:16px;flex-wrap:wrap}}
.foot a{{color:#5a6a7d}}
.gtl,.gtl-b{{display:none}}
{show}
</style></head>
<body data-l="sk">

<div id="bar"><div class="in">
 <span class="nm">FIA FOX · PROTOTYP</span>
 {flags}
 <a class="dar" id="dar" href="{WP}{DAR['sk']}" target="_blank" rel="noopener">♥ {g(UI["dar"])}</a>
 <a id="uvod" href="{WP}{UVOD['sk']}" target="_blank" rel="noopener">{g(UI["uvod"])}</a>
</div></div>

<div class="wrap">

<div class="proto"><b>PROTOTYP — mimo WordPressu.</b>
<span class="gtl-b sk">Ukážka, ako by vyzeral register generovaný z dát: Home → kauzy → konania. Ostrý web foxprof.club a stránka #303 bežia nezmenené a táto stránka do nich nijako nezasahuje. Darovací portál ostáva na WordPresse — tlačidlo Podporiť vedie na existujúcu kampaňovú stránku v jazyku vlajky.</span>
<span class="gtl-b de">Muster: Startseite → Fälle → Verfahren. Die Live-Website bleibt unverändert; der Spendenbereich bleibt auf WordPress.</span>
<span class="gtl-b en">Demonstration: home → cases → proceedings. The live site remains untouched; donations stay on WordPress.</span>
<span class="gtl-b hr">Ogledni primjer: početna → predmeti → postupci. Aktivna stranica ostaje netaknuta.</span>
<span class="gtl-b pl">Przykład: strona główna → sprawy → postępowania. Witryna produkcyjna pozostaje nietknięta.</span>
<span class="gtl-b es">Demostración: inicio → casos → procedimientos. El sitio en producción no se altera.</span>
<span class="gtl-b it">Dimostrazione: home → casi → procedimenti. Il sito in produzione resta intatto.</span>
<span class="gtl-b fr">Démonstration : accueil → affaires → procédures. Le site en production reste intact.</span>
<span class="gtl-b sv">Demonstration: start → ärenden → förfaranden. Den aktiva webbplatsen lämnas orörd.</span>
</div>

<div class="hero">
 <h1>FIA FOX</h1>
 <div class="tag">{g(UI["tag"])}</div>
 <div class="nums"><b>{len(KAUZY)}</b> {g(UI["kauzy"])} &nbsp;&nbsp; <b>{total}</b> {g(UI["konania"])}</div>
</div>

{"".join(kauza_html(z) for z in KAUZY)}

<div class="foot">
 <a id="f-imp" href="{WP}impressum/" target="_blank" rel="noopener">{g(UI["imp"])}</a>
 <a id="f-gdpr" href="{WP}datenschutz/" target="_blank" rel="noopener">{g(UI["gdpr"])}</a>
 <span>FIA FOX — prototyp · dáta a šablóna oddelené</span>
</div>
</div>

<script>
var DAR = {DAR!r}, UVOD = {UVOD!r}, WP = "{WP}";
document.querySelectorAll('.f').forEach(function(b){{
  b.addEventListener('click',function(){{
    var L=b.dataset.l; document.body.dataset.l=L; document.documentElement.lang=L;
    document.querySelectorAll('.f').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on');
    document.getElementById('dar').href  = WP + DAR[L];
    document.getElementById('uvod').href = WP + UVOD[L];
  }});
}});
</script>
</body></html>"""

open('index.html','w',encoding='utf-8').write(HTML)
print("home:", len(HTML), "znakov |", len(KAUZY), "kauz |", total, "konani |", len(LANGS), "jazykov")
