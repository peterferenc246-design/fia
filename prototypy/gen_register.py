#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROTOTYP — Fallregister: dlazdice kauz -> konania. Mimo WordPressu, nezasahuje do #303."""

LANGS = ["de","en","sk","hr","pl","es","it","fr","sv"]
FLAG  = {"de":"de","en":"gb","sk":"sk","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
WP    = "https://foxprof.club/"

def S(de,en,sk,hr,pl,es,it,fr,sv): return dict(zip(LANGS,[de,en,sk,hr,pl,es,it,fr,sv]))

# ═══════════ DÁTA: KAUZY (dlaždice) ═══════════
# jur: de / sk / eu  ·  kod = referenčný kód kauzy  ·  warn = červený podtitul

KAUZY = [
 dict(id="k-jv", kod="TFIA-2026-JV", jur=["de","eu"],
   nazov=S("Telekom — Kartell / Joint Venture","Telekom — cartel / joint venture","Telekom — kartel / spoločný podnik",
           "Telekom — kartel / zajednički pothvat","Telekom — kartel / wspólne przedsiębiorstwo",
           "Telekom — cártel / empresa común","Telekom — cartello / impresa comune",
           "Telekom — entente / entreprise commune","Telekom — kartell / gemensamt företag"),
   warn=S("Eingriff in die Vermögensrechte der Verbraucheröffentlichkeit — BETRUG",
          "Interference with consumers' property rights — FRAUD",
          "Zásah do majetkových práv spotrebiteľskej verejnosti — PODVOD",
          "Zadiranje u imovinska prava potrošača — PRIJEVARA",
          "Ingerencja w prawa majątkowe konsumentów — OSZUSTWO",
          "Injerencia en los derechos patrimoniales de los consumidores — FRAUDE",
          "Interferenza nei diritti patrimoniali dei consumatori — FRODE",
          "Atteinte aux droits patrimoniaux des consommateurs — FRAUDE",
          "Ingrepp i konsumenternas egendomsrätt — BEDRÄGERI")),
 dict(id="k-fon", kod="TCFIA-2026-FON", jur=["de"],
   nazov=S("Telefónica — Betrug","Telefónica — fraud","Telefónica — podvod","Telefónica — prijevara",
           "Telefónica — oszustwo","Telefónica — fraude","Telefónica — frode","Telefónica — fraude","Telefónica — bedrägeri")),
 dict(id="k-lra", kod="LRA-2026-BG", jur=["de"],
   nazov=S("Landratsamt — Bußgeld","Landratsamt — administrative fine","Landratsamt — pokuta",
           "Landratsamt — novčana kazna","Landratsamt — grzywna","Landratsamt — multa",
           "Landratsamt — sanzione","Landratsamt — amende","Landratsamt — böter")),
 dict(id="k-ins", kod="PER-DE-2026-INS-005", jur=["de"], priprava=True,
   nazov=S("Insolvenzantrag (Personal)","Insolvency application (personal)","Návrh na osobný bankrot",
           "Prijedlog za osobni stečaj","Wniosek o upadłość konsumencką","Solicitud de concurso personal",
           "Domanda di insolvenza personale","Demande d'insolvabilité personnelle","Ansökan om personlig insolvens")),
 dict(id="k-exs", kod="PR-2026-EXS", jur=["sk"],
   nazov=S("Schadenersatz 15 000 €","Damages 15 000 €","Náhrada škody 15 000 €","Naknada štete 15 000 €",
           "Odszkodowanie 15 000 €","Indemnización 15 000 €","Risarcimento 15 000 €",
           "Dommages-intérêts 15 000 €","Skadestånd 15 000 €")),
 dict(id="k-vszp", kod="PR-2026-VsZP-006", jur=["sk"],
   nazov=S("Schadenersatz 10 000 € — VšZP","Damages 10 000 € — VšZP","Náhrada škody 10 000 € — VšZP",
           "Naknada štete 10 000 € — VšZP","Odszkodowanie 10 000 € — VšZP","Indemnización 10 000 € — VšZP",
           "Risarcimento 10 000 € — VšZP","Dommages-intérêts 10 000 € — VšZP","Skadestånd 10 000 € — VšZP")),
 dict(id="k-ms", kod="PIF-EU-2026-MBS", jur=["de","eu"],
   nazov=S("Microsoft — DSGVO-Verstöße","Microsoft — GDPR infringements","Microsoft — porušenia GDPR",
           "Microsoft — povrede GDPR-a","Microsoft — naruszenia RODO","Microsoft — infracciones del RGPD",
           "Microsoft — violazioni del GDPR","Microsoft — violations du RGPD","Microsoft — dataskyddsöverträdelser")),
 dict(id="k-dak", kod="PER-DE-2026-DAK", jur=["de"],
   nazov=S("DAK — Betrug (Krankenkasse)","DAK — fraud (health insurer)","DAK — podvod (zdravotná poisťovňa)",
           "DAK — prijevara (zdravstveno osiguranje)","DAK — oszustwo (kasa chorych)","DAK — fraude (caja de enfermedad)",
           "DAK — frode (cassa malattia)","DAK — fraude (caisse maladie)","DAK — bedrägeri (sjukkassa)")),
]

# ═══════════ DÁTA: KONANIA ═══════════
K = []
def add(kauza, org, az, ourref, datum, stav, nazov, url=None, jur="de"):
    K.append(dict(kauza=kauza, org=org, az=az, ourref=ourref, datum=datum, stav=stav,
                  nazov=nazov, url=url, jur=jur))

add("k-jv","Všeobecný súd Európskej únie","T-61/26","TFIA-2026-JV-001","2026-03-10","laeuft",
    "Nichtigkeitsklage M.10815 · Art. 263 AEUV", jur="eu")
add("k-jv","Európska komisia — DG COMP · Generálny sekretariát","EASE 2025/6534","TFIA-2026-JV-009",
    "2026-07-19","laeuft","Zugang zu Dokumenten · VO 1049/2001","dgcomp-karta-prototyp.html", jur="eu")
add("k-jv","Landgericht Landshut","91 O 2699/24","TFIA-2026-JV-002","2024-10-02","laeuft",
    "Klage gegen Deutsche Telekom AG und Schufa Holding AG")
add("k-jv","Polizeiinspektion / StA Landshut","709 AR 303/24 601","TFIA-2026-JV-004","2024-11-08","abgelehnt",
    "Strafrechtliche Mitteilung — Telekom und Schufa")
add("k-jv","BaFin Bonn · Commerzbank AG","ZKG","TFIA-2026-JV-010","2026-05-01","laeuft",
    "Zahlungskontengesetz — Verfahren")
add("k-fon","O2 Telefónica Germany · Bundesnetzagentur","—","TCFIA-2026-FON-001","2026-04-01","laeuft",
    "Deaktivierung der SIM-Karte — Betrug")
add("k-lra","Landratsamt Landshut","30-8223.1 AD","LRA-2026-BG-001","2026-02-01","laeuft",
    "Nezákonne uložená pokuta")
add("k-lra","Landgericht Landshut — Strafsachen","2 Qs 80/25","LRA-2026-BG-002","2026-06-01","laeuft",
    "Sofortige Beschwerde gegen Erzwingungshaft")
add("k-exs","ÚDZS Slovensko","12479/2026/911","PR-2026-EXS-016","2026-03-01","laeuft",
    "Nezákonná exekúcia za nulový dlh", jur="sk")
add("k-vszp","Okresný súd Bratislava V","156EX-171/25","PR-2026-VsZP-006","2026-05-01","laeuft",
    "Žaloba o náhradu škody", jur="sk")
add("k-vszp","Generálna prokuratúra SR","—","PR-2026-VsZP-007","2026-06-01","laeuft",
    "Trestné oznámenie na prokurátorov", jur="sk")
add("k-ms","Data Protection Commission Ireland","DPC0526916540","PIF-EU-2026-MBS-004","2026-04-17","laeuft",
    "Beschwerde nach Art. 77 DSGVO", jur="eu")
add("k-ms","Európska prokuratúra (EPPO)","P.000800/2026","PIF-EU-2026-MBS-002","2026-04-17","laeuft",
    "Strafanzeige — Art. 325 AEUV", jur="eu")
add("k-dak","Staatsanwaltschaft Hamburg · Hauptzollamt","—","PER-DE-2026-DAK-001","2026-03-01","laeuft",
    "DAK — Strafanzeige und Einwendung gegen die Vollstreckung")

for z in KAUZY:
    z["n"] = sum(1 for k in K if k["kauza"] == z["id"])

STAV = {"laeuft": S("Läuft","Pending","Prebieha","U tijeku","W toku","En curso","In corso","En cours","Pågår"),
        "abgelehnt": S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag")}

UI = {
 "title": S("Fallregister","Case register","Register káuz","Registar predmeta","Rejestr spraw",
            "Registro de casos","Registro dei casi","Registre des affaires","Ärenderegister"),
 "home": S("← Zur Startseite","← Home","← Späť na úvod","← Naslovnica","← Strona główna",
           "← Inicio","← Home","← Accueil","← Startsidan"),
 "all": S("Alle","All","Všetko","Sve","Wszystko","Todo","Tutti","Tout","Alla"),
 "de": S("Deutschland","Germany","Nemecko","Njemačka","Niemcy","Alemania","Germania","Allemagne","Tyskland"),
 "sk": S("Slowakei","Slovakia","Slovensko","Slovačka","Słowacja","Eslovaquia","Slovacchia","Slovaquie","Slovakien"),
 "eu": S("EU","EU","EÚ","EU","UE","UE","UE","UE","EU"),
 "allv": S("Alle Verfahren anzeigen","Show all proceedings","Zobraziť všetky konania","Prikaži sve postupke",
           "Pokaż wszystkie postępowania","Mostrar todos los procedimientos","Mostra tutti i procedimenti",
           "Afficher toutes les procédures","Visa alla förfaranden"),
 "allk": S("★ Alle Fälle","★ All cases","★ Všetky kauzy","★ Svi predmeti","★ Wszystkie sprawy",
           "★ Todos los casos","★ Tutti i casi","★ Toutes les affaires","★ Alla ärenden"),
 "verf": S("Verfahren","proceedings","konania","postupci","postępowania","procedimientos","procedimenti","procédures","förfaranden"),
 "prip": S("In Vorbereitung","In preparation","Pripravuje sa","U pripremi","W przygotowaniu",
           "En preparación","In preparazione","En préparation","Under förberedelse"),
 "hint": S("👆 Wählen Sie einen Fall im Register oben — die zugehörigen Verfahren (Klagen, Beschwerden, Strafanzeigen) werden mit ihrer Historie angezeigt.",
   "👆 Select a case above — the related proceedings (actions, complaints, criminal reports) will be shown with their history.",
   "👆 Vyberte kauzu v registri vyššie — zobrazia sa jej konania (žaloby, sťažnosti, trestné oznámenia) aj s históriou.",
   "👆 Odaberite predmet u registru — prikazat će se pripadajući postupci (tužbe, pritužbe, kaznene prijave) s poviješću.",
   "👆 Wybierz sprawę w rejestrze — zostaną wyświetlone powiązane postępowania (skargi, zawiadomienia) wraz z historią.",
   "👆 Seleccione un caso arriba — se mostrarán los procedimientos relacionados (recursos, reclamaciones, denuncias) con su historial.",
   "👆 Selezionate un caso qui sopra — verranno mostrati i procedimenti collegati (ricorsi, reclami, denunce) con la loro storia.",
   "👆 Choisissez une affaire ci-dessus — les procédures liées (recours, plaintes, signalements) s'afficheront avec leur historique.",
   "👆 Välj ett ärende ovan — tillhörande förfaranden (talan, klagomål, anmälningar) visas med sin historik."),
 "sort": S("SORTIEREN","SORT","ZORADIŤ","SORTIRAJ","SORTUJ","ORDENAR","ORDINA","TRIER","SORTERA"),
 "s_dat": S("📅 Datum","📅 Date","📅 Dátum","📅 Datum","📅 Data","📅 Fecha","📅 Data","📅 Date","📅 Datum"),
 "s_az": S("🏛 Az.","🏛 File ref.","🏛 Spis","🏛 Broj","🏛 Sygn.","🏛 Ref.","🏛 Rif.","🏛 Réf.","🏛 Nr"),
 "s_our": S("🦊 Unser Az.","🦊 Our ref.","🦊 Naša značka","🦊 Naš broj","🦊 Nasza sygn.",
            "🦊 Ntra. ref.","🦊 Ns. rif.","🦊 Notre réf.","🦊 Vårt nr"),
 "open": S("Akte öffnen →","Open the file →","Otvoriť kartu →","Otvori karticu →","Otwórz kartę →",
           "Abrir la ficha →","Apri la scheda →","Ouvrir la fiche →","Öppna kortet →"),
 "soon": S("in Vorbereitung","in preparation","pripravuje sa","u pripremi","w przygotowaniu",
           "en preparación","in preparazione","en préparation","under förberedelse"),
 "about_h": S("Über diese Seite","About this page","O tejto stránke","O ovoj stranici","O tej stronie",
              "Sobre esta página","Su questa pagina","À propos de cette page","Om denna sida"),
}

ABOUT = {
"de":["Diese Seite ist ein öffentliches Register der Rechtsverfahren der Initiative FIA FOX — Bürgerinitiative für faires Internet. Sie entstand, damit jeder transparent verfolgen kann, mit welchen rechtlichen Schritten die Initiative ein faires, kartellfreies Internet in Europa erstreitet: von Klagen vor den Gerichten der EU über Beschwerden bei den Wettbewerbsbehörden bis hin zu Eingaben im Bereich des Datenschutzes.",
 "Zu jedem Fall finden Sie die Aktenkommunikation — eine Übersicht der gesendeten Eingaben und der empfangenen Antworten — samt Zugang zu den Dokumenten. Ein Klick auf einen Fall klappt die Karte auf und zeigt ihren Inhalt.",
 "Mit den Flaggen oben schalten Sie die Sprache der gesamten Seite um. Bei jedem Dokument bedeutet 🌐 Öffentlich einen frei zugänglichen Beleg, 🔒 Passwort ein gezielt geteiltes Dokument.",
 "Mit der Veröffentlichung der hier geführten Materialien verfolgt die Initiative ausschließlich die Information der Öffentlichkeit in einer Angelegenheit von öffentlichem Interesse. Dokumente werden nur im rechtlich zulässigen Umfang zugänglich gemacht."],
"en":["This page is a public register of the legal proceedings of the FIA FOX initiative — a citizens' initiative for a fair internet. It exists so that anyone can transparently follow the legal steps by which the initiative pursues a fair, cartel-free internet in Europe: from actions before the EU courts, through complaints to the competition authorities, to submissions in the field of data protection.",
 "For each case you will find the case correspondence — an overview of the submissions sent and the replies received — together with access to the documents. Clicking a case opens the card and shows its content.",
 "The flags above switch the language of the whole page. For each document, 🌐 Public means a freely accessible record, 🔒 Password a document shared selectively.",
 "In publishing the materials kept here, the initiative pursues solely the information of the public in a matter of public interest. Documents are made accessible only to the extent permitted by law."],
"sk":["Táto stránka je verejný register právnych konaní iniciatívy FIA FOX — občianskej iniciatívy za férový internet. Vznikla preto, aby ktokoľvek mohol transparentne sledovať, akými právnymi krokmi iniciatíva presadzuje férový internet bez kartelov v Európe: od žalôb pred súdmi EÚ cez sťažnosti na súťažné orgány až po podania v oblasti ochrany osobných údajov.",
 "Ku každej kauze nájdete spisovú komunikáciu — prehľad odoslaných podaní a doručených odpovedí — spolu s prístupom k dokumentom. Kliknutie na kauzu rozbalí kartu a zobrazí jej obsah.",
 "Vlajkami hore prepnete jazyk celej stránky. Pri každom dokumente znamená 🌐 Verejné voľne dostupný doklad, 🔒 Heslo dokument zdieľaný cielene.",
 "Zverejnením tu vedených materiálov iniciatíva sleduje výlučne informovanie verejnosti vo veci verejného záujmu. Dokumenty sa sprístupňujú len v právne prípustnom rozsahu."],
"hr":["Ova je stranica javni registar pravnih postupaka inicijative FIA FOX — građanske inicijative za pošten internet. Nastala je kako bi svatko mogao transparentno pratiti kojim pravnim koracima inicijativa ostvaruje pošten internet bez kartela u Europi.",
 "Uz svaki predmet nalazi se korespondencija spisa — pregled poslanih podnesaka i primljenih odgovora — te pristup dokumentima. Klik na predmet otvara karticu i prikazuje njezin sadržaj.",
 "Zastavama gore mijenjate jezik cijele stranice. Uz svaki dokument 🌐 Javno znači slobodno dostupan dokaz, 🔒 Lozinka ciljano podijeljen dokument.",
 "Objavom ovdje vođenih materijala inicijativa isključivo informira javnost o pitanju od javnog interesa. Dokumenti se objavljuju samo u pravno dopuštenom opsegu."],
"pl":["Ta strona to publiczny rejestr postępowań prawnych inicjatywy FIA FOX — inicjatywy obywatelskiej na rzecz uczciwego internetu. Powstała, aby każdy mógł przejrzyście śledzić, jakimi krokami prawnymi inicjatywa dąży do uczciwego internetu bez karteli w Europie.",
 "Przy każdej sprawie znajduje się korespondencja akt — przegląd wysłanych pism i otrzymanych odpowiedzi — wraz z dostępem do dokumentów. Kliknięcie sprawy rozwija kartę i pokazuje jej treść.",
 "Flagami u góry przełączasz język całej strony. Przy każdym dokumencie 🌐 Publiczne oznacza swobodnie dostępny dowód, 🔒 Hasło dokument udostępniony wybiórczo.",
 "Publikując prowadzone tu materiały, inicjatywa realizuje wyłącznie informowanie opinii publicznej w sprawie o znaczeniu publicznym. Dokumenty udostępnia się tylko w zakresie dozwolonym prawem."],
"es":["Esta página es un registro público de los procedimientos jurídicos de la iniciativa FIA FOX — una iniciativa ciudadana por un internet justo. Nació para que cualquiera pueda seguir de forma transparente los pasos jurídicos con los que la iniciativa persigue un internet justo y sin cárteles en Europa.",
 "En cada caso encontrará la correspondencia del expediente — un resumen de los escritos enviados y de las respuestas recibidas — junto con el acceso a los documentos. Al pulsar un caso se despliega la ficha y se muestra su contenido.",
 "Con las banderas de arriba se cambia el idioma de toda la página. En cada documento, 🌐 Público indica un justificante de libre acceso y 🔒 Contraseña un documento compartido de forma selectiva.",
 "Al publicar los materiales aquí recogidos, la iniciativa persigue únicamente informar al público en un asunto de interés general. Los documentos se hacen accesibles solo en la medida permitida por la ley."],
"it":["Questa pagina è un registro pubblico dei procedimenti giuridici dell'iniziativa FIA FOX — un'iniziativa dei cittadini per un internet equo. È nata affinché chiunque possa seguire in modo trasparente i passi giuridici con cui l'iniziativa persegue un internet equo e senza cartelli in Europa.",
 "Per ogni caso troverete la corrispondenza del fascicolo — una panoramica delle istanze inviate e delle risposte ricevute — insieme all'accesso ai documenti. Cliccando su un caso la scheda si apre e ne mostra il contenuto.",
 "Con le bandiere in alto si cambia la lingua dell'intera pagina. Per ogni documento, 🌐 Pubblico indica un atto liberamente accessibile, 🔒 Password un documento condiviso in modo mirato.",
 "Pubblicando i materiali qui raccolti, l'iniziativa persegue esclusivamente l'informazione del pubblico su una questione di interesse generale. I documenti sono resi accessibili solo nei limiti consentiti dalla legge."],
"fr":["Cette page est un registre public des procédures juridiques de l'initiative FIA FOX — une initiative citoyenne pour un internet équitable. Elle a été créée pour que chacun puisse suivre de façon transparente les démarches juridiques par lesquelles l'initiative défend un internet équitable et sans ententes en Europe.",
 "Pour chaque affaire, vous trouverez la correspondance du dossier — un aperçu des écrits envoyés et des réponses reçues — ainsi que l'accès aux documents. Un clic sur une affaire déplie la fiche et en affiche le contenu.",
 "Les drapeaux en haut changent la langue de toute la page. Pour chaque document, 🌐 Public désigne une pièce librement accessible, 🔒 Mot de passe un document partagé de manière ciblée.",
 "En publiant les matériaux réunis ici, l'initiative poursuit uniquement l'information du public dans une affaire d'intérêt général. Les documents ne sont rendus accessibles que dans la mesure permise par la loi."],
"sv":["Den här sidan är ett offentligt register över FIA FOX-initiativets rättsliga förfaranden — ett medborgarinitiativ för ett rättvist internet. Det tillkom för att var och en öppet ska kunna följa med vilka rättsliga steg initiativet driver ett rättvist internet utan karteller i Europa.",
 "Till varje ärende finns aktkorrespondensen — en översikt över inlämnade skrivelser och mottagna svar — samt tillgång till handlingarna. Ett klick på ett ärende fäller ut kortet och visar dess innehåll.",
 "Med flaggorna ovan byter du språk för hela sidan. Vid varje handling betyder 🌐 Offentlig ett fritt tillgängligt underlag, 🔒 Lösenord en handling som delats riktat.",
 "Genom att publicera materialet här eftersträvar initiativet enbart att informera allmänheten i en fråga av allmänt intresse. Handlingar görs tillgängliga endast i den utsträckning lagen tillåter."],
}

# ═══════════ ŠABLÓNA ═══════════
def g(d,b=False):
    c="gtl-b" if b else "gtl"
    return "".join(f'<span class="{c} {L}">{d[L]}</span>' for L in LANGS)

FL = {"de":"de","sk":"sk","eu":"eu"}
def jflags(js):
    out=""
    for j in js:
        if j=="eu": out+='<span class="jf">🇪🇺</span>'
        else: out+=f'<img class="jf" src="https://flagcdn.com/{FL[j]}.svg" alt="{j}">'
    return out

def tile(z):
    warn = f'<div class="tw">{g(z["warn"])}</div>' if z.get("warn") else ""
    cnt = (f'<span class="tc prip">{g(UI["prip"])}</span>' if z.get("priprava")
           else f'<span class="tc">• {z["n"]} {g(UI["verf"])}</span>')
    return (f'<button class="tile" data-k="{z["id"]}" data-jur="{" ".join(z["jur"])}">'
            f'<div class="tf">{jflags(z["jur"])}</div>'
            f'<div class="tn">{g(z["nazov"])}</div><div class="tk">{z["kod"]}</div>{warn}{cnt}</button>')

def kon(k):
    btn = (f'<a class="go" href="{k["url"]}">{g(UI["open"])}</a>' if k["url"]
           else f'<span class="soon">{g(UI["soon"])}</span>')
    return (f'<div class="kon" data-k="{k["kauza"]}" data-d="{k["datum"]}" data-az="{k["az"]}" data-our="{k["ourref"]}">'
            f'<div><div class="knaz">{k["nazov"]}</div>'
            f'<div class="korg">{k["org"]} &nbsp;·&nbsp; <b>{k["az"]}</b> &nbsp;·&nbsp; {k["ourref"]}</div></div>'
            f'<div class="kside"><span class="st st-{k["stav"]}">{g(STAV[k["stav"]])}</span>{btn}</div></div>')

flags = "".join(f'<button class="f{" on" if L=="sk" else ""}" data-l="{L}">'
                f'<img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in LANGS)
show = "".join(f'body[data-l="{L}"] .gtl.{L}{{display:inline}}body[data-l="{L}"] .gtl-b.{L}{{display:block}}' for L in LANGS)
about = "".join(f'<div class="gtl-b {L}">' + "".join(f"<p>{p}</p>" for p in ABOUT[L]) + "</div>" for L in LANGS)

HTML = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Fallregister · PROTOTYP</title>
<style>
:root{{--navy:#1F3864;--hero:#2E5BA6;--red:#C00000;--soft:#D6E6F2;--bd:#c9d8e8}}
*{{box-sizing:border-box}}
body{{margin:0;color:#22303f;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
 background:linear-gradient(#8ec5ea 0%,#b9dcf3 34%,#dcecf8 64%,#f3e9d6 100%);background-attachment:fixed;min-height:100vh}}
.top{{text-align:center;padding:20px 16px 4px}}
.top h1{{margin:0;font-size:22px;color:var(--navy);font-weight:800}}
.top .sub{{font-size:13px;color:#4a6076;margin-top:3px}}
.wrap{{max-width:960px;margin:0 auto;padding:0 16px 50px}}
.navbar{{background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(31,56,100,.10);
 padding:9px 14px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}}
.hm{{border:1px solid var(--bd);border-radius:6px;padding:5px 14px;text-decoration:none;color:var(--navy);font-size:13px}}
.hm:hover{{background:#f2f7fc}}
.lang{{display:flex;align-items:center;gap:5px;flex-wrap:wrap}}
.lang .lb{{font-size:10px;color:#8a97a6;letter-spacing:.12em;margin-right:3px}}
.f{{background:none;border:1px solid rgba(31,56,100,.3);border-radius:3px;padding:0;cursor:pointer;
 width:30px;height:20px;opacity:.5;overflow:hidden}}
.f img{{width:30px;height:20px;object-fit:cover;display:block}}
.f.on{{opacity:1;border-color:var(--navy);box-shadow:0 0 0 2px rgba(31,56,100,.25)}}
.panel{{background:#fff;border-radius:8px;box-shadow:0 2px 10px rgba(31,56,100,.10);padding:20px 22px;margin-bottom:14px}}
.panel>h2{{margin:0 0 14px;font-size:22px;color:var(--navy)}}
.tabs{{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}}
.tab{{border:1px solid var(--bd);background:#fbfcfd;border-radius:6px;padding:5px 14px;font-size:13px;
 cursor:pointer;color:#3d4d5e;display:flex;align-items:center;gap:6px}}
.tab.on{{background:var(--navy);color:#fff;border-color:var(--navy)}}
.tab img{{width:18px;height:12px;object-fit:cover;border-radius:2px}}
.allrow{{border:1px solid var(--bd);border-left:4px solid var(--navy);border-radius:6px;padding:11px 15px;
 margin-bottom:12px;cursor:pointer;background:#fbfcfd}}
.allrow.on{{background:#eef4fb}}
.allrow .t{{font-size:14px;color:var(--navy);font-weight:600}}
.allrow .b{{display:inline-block;margin-top:5px;font-size:11px;background:#fff3d6;color:#8a5a00;
 border:1px solid #f0c040;border-radius:999px;padding:1px 10px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:11px}}
@media(max-width:880px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:520px){{.grid{{grid-template-columns:1fr}}}}
.tile{{text-align:left;background:#fbfcfd;border:1px solid var(--bd);border-left:4px solid var(--navy);
 border-radius:6px;padding:11px 13px;cursor:pointer;font:inherit;color:inherit}}
.tile:hover{{background:#f2f7fc}}
.tile.on{{background:#eef4fb;box-shadow:0 0 0 2px rgba(31,56,100,.28)}}
.tf{{display:flex;gap:4px;align-items:center;margin-bottom:5px}}
.jf{{width:17px;height:12px;object-fit:cover;border-radius:2px;font-size:12px;line-height:1}}
.tn{{font-size:13.5px;font-weight:700;color:var(--navy);line-height:1.3}}
.tk{{font-size:10.5px;color:#8a97a6;letter-spacing:.04em;margin-top:3px}}
.tw{{font-size:11px;color:var(--red);font-style:italic;font-weight:700;margin-top:5px;line-height:1.3}}
.tc{{display:inline-block;margin-top:7px;font-size:11px;color:#54637a;background:#eef2f7;border-radius:999px;padding:1px 9px}}
.tc.prip{{background:#fff3d6;color:#8a5a00;border:1px solid #f0c040}}
.hint{{background:rgba(255,255,255,.6);border:1px dashed var(--bd);border-radius:8px;
 padding:13px 18px;text-align:center;font-size:12.5px;color:#5a6a7d;margin-bottom:14px}}
.sortbar{{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:center;margin:14px 0}}
.sortbar .lb{{font-size:10.5px;color:#5a6a7d;letter-spacing:.12em}}
.sb{{border:1px solid var(--bd);background:#fff;border-radius:6px;padding:4px 13px;font-size:12.5px;cursor:pointer;color:#3d4d5e}}
.sb.on{{background:var(--navy);color:#fff;border-color:var(--navy)}}
.kon{{background:#fff;border-radius:7px;box-shadow:0 1px 6px rgba(31,56,100,.09);padding:12px 16px;
 margin-bottom:9px;display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}}
.knaz{{font-size:14.5px;color:var(--navy);font-weight:600}}
.korg{{font-size:12.5px;color:#7a8899;margin-top:2px}}
.kside{{display:flex;align-items:center;gap:10px}}
.st{{font-size:11px;border-radius:999px;padding:2px 10px;white-space:nowrap}}
.st-laeuft{{background:#fff3d6;color:#8a5a00;border:1px solid #f0c040}}
.st-abgelehnt{{background:#fde8e8;color:#8a1c1c;border:1px solid #e8b4b4}}
.go{{font-size:12.5px;text-decoration:none;background:var(--navy);color:#fff;border-radius:4px;padding:5px 13px;white-space:nowrap}}
.soon{{font-size:12px;color:#9aa7b5}}
.about{{background:#fff;border-left:4px solid var(--navy);border-radius:8px;
 box-shadow:0 2px 10px rgba(31,56,100,.10);padding:20px 24px;margin-top:16px}}
.about h3{{margin:0 0 10px;font-size:17px;color:var(--navy)}}
.about p{{margin:0 0 10px;font-size:13.5px;line-height:1.65;color:#3d4d5e}}
.proto{{background:#fff6d6;border:1px solid #f0c040;border-left:5px solid var(--red);
 padding:10px 14px;margin:10px 0 14px;border-radius:4px;font-size:12.5px}}
.gtl,.gtl-b{{display:none}}
{show}
</style></head>
<body data-l="sk">

<div class="top"><h1>FIA FOX — Fair Internet Initiative</h1>
<div class="sub gtl de">Bürgerinitiative für faires Internet und fairen Wettbewerb in der EU</div>
<div class="sub gtl sk">Občianska iniciatíva za férový internet a spravodlivú súťaž v EÚ</div>
<div class="sub gtl en">Citizens' initiative for a fair internet and fair competition in the EU</div>
<div class="sub gtl hr">Građanska inicijativa za pošten internet i natjecanje u EU</div>
<div class="sub gtl pl">Inicjatywa obywatelska na rzecz uczciwego internetu w UE</div>
<div class="sub gtl es">Iniciativa ciudadana por un internet justo en la UE</div>
<div class="sub gtl it">Iniziativa dei cittadini per un internet equo nell'UE</div>
<div class="sub gtl fr">Initiative citoyenne pour un internet équitable dans l'UE</div>
<div class="sub gtl sv">Medborgarinitiativ för ett rättvist internet i EU</div>
</div>

<div class="wrap">

<div class="navbar">
 <a class="hm" href="index.html">{g(UI["home"])}</a>
 <div class="lang"><span class="lb">LANG</span>{flags}</div>
</div>

<div class="proto"><b>PROTOTYP</b> — mimo WordPressu, ostrý register #303 beží nezmenený.</div>

<div class="panel">
 <h2>{g(UI["title"])}</h2>
 <div class="tabs">
  <button class="tab on" data-j="all">{g(UI["all"])}</button>
  <button class="tab" data-j="de"><img src="https://flagcdn.com/de.svg" alt="DE">{g(UI["de"])}</button>
  <button class="tab" data-j="sk"><img src="https://flagcdn.com/sk.svg" alt="SK">{g(UI["sk"])}</button>
  <button class="tab" data-j="eu">🇪🇺 {g(UI["eu"])}</button>
 </div>
 <div class="allrow on" id="allrow"><div class="t">🌐 {g(UI["allv"])}</div><span class="b">{g(UI["allk"])}</span></div>
 <div class="grid">{"".join(tile(z) for z in KAUZY)}</div>
</div>

<div class="hint">{g(UI["hint"])}</div>

<div class="sortbar"><span class="lb">{g(UI["sort"])}</span>
 <button class="sb on" data-s="d">{g(UI["s_dat"])}</button>
 <button class="sb" data-s="az">{g(UI["s_az"])}</button>
 <button class="sb" data-s="our">{g(UI["s_our"])}</button>
</div>

<div id="list">{"".join(kon(k) for k in K)}</div>

<div class="about"><h3>{g(UI["about_h"])}</h3>{about}</div>
</div>

<script>
var SEL=null, JUR='all', SORT='d';
function apply(){{
  document.querySelectorAll('.tile').forEach(function(t){{
    var okj = JUR==='all' || t.dataset.jur.split(' ').indexOf(JUR)>=0;
    t.style.display = okj ? '' : 'none';
    t.classList.toggle('on', SEL===t.dataset.k);
  }});
  document.getElementById('allrow').classList.toggle('on', SEL===null);
  var l=document.getElementById('list'), rows=[].slice.call(l.querySelectorAll('.kon'));
  rows.forEach(function(r){{ r.style.display = (SEL===null||r.dataset.k===SEL) ? '' : 'none'; }});
  rows.sort(function(a,b){{
    if(SORT==='d')  return b.dataset.d.localeCompare(a.dataset.d);
    if(SORT==='az') return a.dataset.az.localeCompare(b.dataset.az);
    return a.dataset.our.localeCompare(b.dataset.our);
  }}).forEach(function(r){{ l.appendChild(r); }});
}}
document.querySelectorAll('.tile').forEach(function(t){{
  t.addEventListener('click',function(){{ SEL = (SEL===t.dataset.k)?null:t.dataset.k; apply(); }});
}});
document.getElementById('allrow').addEventListener('click',function(){{ SEL=null; apply(); }});
document.querySelectorAll('.tab').forEach(function(b){{
  b.addEventListener('click',function(){{
    JUR=b.dataset.j; SEL=null;
    document.querySelectorAll('.tab').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on'); apply();
  }});
}});
document.querySelectorAll('.sb').forEach(function(b){{
  b.addEventListener('click',function(){{
    SORT=b.dataset.s;
    document.querySelectorAll('.sb').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on'); apply();
  }});
}});
document.querySelectorAll('.f').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.body.dataset.l=b.dataset.l; document.documentElement.lang=b.dataset.l;
    document.querySelectorAll('.f').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on');
  }});
}});
apply();
</script>
</body></html>"""

open('register.html','w',encoding='utf-8').write(HTML)
print("register:", len(HTML), "znakov |", len(KAUZY), "kauz |", len(K), "konani")
for z in KAUZY: print(f"   {z['kod']:<22} {z['n']} konani")
