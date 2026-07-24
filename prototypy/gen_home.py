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


HERO = S("Bürgerinitiative für ein faires Internet ohne rechtswidrige Kartell- und Monopolstrukturen und für fairen Wettbewerb in der Europäischen Union — ohne Eingriff in die Vermögensrechte der Bürgerinnen und Bürger.",
 "A citizens' initiative for a fair internet without unlawful cartel and monopoly structures and for fair competition in the European Union — without interference with the property rights of its citizens.",
 "Občianska iniciatíva za férový internet bez nezákonných kartelových a monopolných štruktúr a za spravodlivú hospodársku súťaž v Európskej únii — bez zásahov do majetkových práv občanov.",
 "Građanska inicijativa za pošten internet bez nezakonitih kartelnih i monopolnih struktura i za pošteno tržišno natjecanje u Europskoj uniji — bez zadiranja u imovinska prava građana.",
 "Inicjatywa obywatelska na rzecz uczciwego internetu bez bezprawnych struktur kartelowych i monopolowych oraz uczciwej konkurencji w Unii Europejskiej — bez ingerencji w prawa majątkowe obywateli.",
 "Iniciativa ciudadana por un internet justo sin estructuras ilícitas de cártel y monopolio y por una competencia leal en la Unión Europea — sin injerencia en los derechos patrimoniales de los ciudadanos.",
 "Iniziativa dei cittadini per un internet equo senza strutture illecite di cartello e monopolio e per una concorrenza leale nell'Unione europea — senza interferenze nei diritti patrimoniali dei cittadini.",
 "Initiative citoyenne pour un internet équitable sans structures illicites d'entente et de monopole et pour une concurrence loyale dans l'Union européenne — sans atteinte aux droits patrimoniaux des citoyens.",
 "Medborgarinitiativ för ett rättvist internet utan olagliga kartell- och monopolstrukturer och för sund konkurrens i Europeiska unionen — utan ingrepp i medborgarnas egendomsrätt.")

DAR_H = S("💝 Unterstützen Sie unsere Mission","💝 Support our mission","💝 Podporte našu misiu","💝 Podržite našu misiju",
 "💝 Wesprzyj naszą misję","💝 Apoye nuestra misión","💝 Sostieni la nostra missione","💝 Soutenez notre mission","💝 Stöd vårt uppdrag")
DAR_1 = S("FIA FOX arbeitet unabhängig und ohne externe Finanzierung durch Unternehmen oder Institutionen.",
 "FIA FOX works independently and without external funding from companies or institutions.",
 "FIA FOX pracuje nezávisle a bez externého financovania od firiem či inštitúcií.",
 "FIA FOX djeluje neovisno i bez vanjskog financiranja od tvrtki ili institucija.",
 "FIA FOX działa niezależnie i bez zewnętrznego finansowania od firm czy instytucji.",
 "FIA FOX trabaja de forma independiente y sin financiación externa de empresas o instituciones.",
 "FIA FOX opera in modo indipendente e senza finanziamenti esterni da imprese o istituzioni.",
 "FIA FOX agit de manière indépendante et sans financement externe d'entreprises ou d'institutions.",
 "FIA FOX arbetar oberoende och utan extern finansiering från företag eller institutioner.")
DAR_2 = S("Ihre Beiträge dienen der Überführung der Initiative in einen eingetragenen Verein im Sinne des Gesetzes sowie der Deckung der laufenden Kosten und der Koordination der Initiative.",
 "Your contributions serve to convert the initiative into a registered association within the meaning of the law and to cover its running costs and coordination.",
 "Vaše príspevky slúžia na prevedenie iniciatívy na registrované združenie v zmysle zákona a na pokrytie bežných nákladov a koordinácie iniciatívy.",
 "Vaši prilozi služe pretvaranju inicijative u registrirano udruženje u smislu zakona te pokrivanju tekućih troškova i koordinacije.",
 "Państwa wpłaty służą przekształceniu inicjatywy w zarejestrowane stowarzyszenie w rozumieniu prawa oraz pokryciu bieżących kosztów i koordynacji.",
 "Sus contribuciones sirven para convertir la iniciativa en una asociación registrada conforme a la ley y para cubrir los gastos corrientes y la coordinación.",
 "I vostri contributi servono a trasformare l'iniziativa in un'associazione registrata ai sensi di legge e a coprire i costi correnti e il coordinamento.",
 "Vos contributions servent à transformer l'initiative en association déclarée au sens de la loi et à couvrir les frais courants et la coordination.",
 "Era bidrag används för att ombilda initiativet till en registrerad förening enligt lag och för att täcka löpande kostnader och samordning.")
DAR_B = S("💝 Jetzt spenden →","💝 Donate now →","💝 Prispieť teraz →","💝 Doniraj sada →","💝 Wesprzyj teraz →",
 "💝 Donar ahora →","💝 Dona ora →","💝 Faire un don →","💝 Ge en gåva →")

MIS_H = S("Unsere Mission","Our mission","Naša misia","Naša misija","Nasza misja","Nuestra misión","La nostra missione","Notre mission","Vårt uppdrag")
MIS_1 = S("Bürgerinitiative für faires Internet und fairen Wettbewerb in der Europäischen Union.",
 "A citizens' initiative for a fair internet and fair competition in the European Union.",
 "Občianska iniciatíva za férový internet a spravodlivú hospodársku súťaž v Európskej únii.",
 "Građanska inicijativa za pošten internet i pošteno tržišno natjecanje u Europskoj uniji.",
 "Inicjatywa obywatelska na rzecz uczciwego internetu i uczciwej konkurencji w Unii Europejskiej.",
 "Iniciativa ciudadana por un internet justo y una competencia leal en la Unión Europea.",
 "Iniziativa dei cittadini per un internet equo e una concorrenza leale nell'Unione europea.",
 "Initiative citoyenne pour un internet équitable et une concurrence loyale dans l'Union européenne.",
 "Medborgarinitiativ för ett rättvist internet och sund konkurrens i Europeiska unionen.")
MIS_2 = S("Wir wenden uns gegen wettbewerbswidrige Kartell- und Monopolpraktiken marktbeherrschender Konzerne, die nach Auffassung der Initiative zu deren ungerechtfertigter Bereicherung, zu überhöhten Preisen, zur Einschränkung des fairen Wettbewerbs und zu Eingriffen in die Vermögensrechte der Bürgerinnen und Bürger der Europäischen Union führen.",
 "We oppose the anti-competitive cartel and monopoly practices of dominant corporations which, in the initiative's view, lead to their unjustified enrichment, to excessive prices, to the restriction of fair competition and to interference with the property rights of the citizens of the European Union.",
 "Staviame sa proti protisúťažným kartelovým a monopolným praktikám dominantných koncernov, ktoré podľa iniciatívy vedú k ich neoprávnenému obohateniu, k neprimeraným cenám, k obmedzeniu spravodlivej súťaže a k zásahom do majetkových práv občanov Európskej únie.",
 "Suprotstavljamo se protutržišnim kartelnim i monopolnim praksama vladajućih korporacija koje, prema inicijativi, vode njihovu neopravdanom bogaćenju, previsokim cijenama, ograničenju poštenog tržišnog natjecanja i zadiranju u imovinska prava građana Europske unije.",
 "Sprzeciwiamy się antykonkurencyjnym praktykom kartelowym i monopolowym dominujących koncernów, które zdaniem inicjatywy prowadzą do ich nieuzasadnionego wzbogacenia, do zawyżonych cen, do ograniczenia uczciwej konkurencji i do ingerencji w prawa majątkowe obywateli Unii Europejskiej.",
 "Nos oponemos a las prácticas anticompetitivas de cártel y monopolio de las grandes empresas dominantes que, a juicio de la iniciativa, conducen a su enriquecimiento injustificado, a precios excesivos, a la restricción de la competencia leal y a injerencias en los derechos patrimoniales de los ciudadanos de la Unión Europea.",
 "Ci opponiamo alle pratiche anticoncorrenziali di cartello e monopolio dei gruppi dominanti che, secondo l'iniziativa, portano al loro ingiustificato arricchimento, a prezzi eccessivi, alla restrizione della concorrenza leale e a interferenze nei diritti patrimoniali dei cittadini dell'Unione europea.",
 "Nous nous opposons aux pratiques anticoncurrentielles d'entente et de monopole des groupes dominants qui, selon l'initiative, conduisent à leur enrichissement injustifié, à des prix excessifs, à la restriction d'une concurrence loyale et à des atteintes aux droits patrimoniaux des citoyens de l'Union européenne.",
 "Vi motsätter oss konkurrensbegränsande kartell- och monopolmetoder hos dominerande koncerner som enligt initiativet leder till deras oberättigade berikning, till överpriser, till inskränkt sund konkurrens och till ingrepp i EU-medborgarnas egendomsrätt.")
MIS_3 = S("FIA FOX ist die zivilgesellschaftliche Antwort: Dokumentation, Rechtsaktivismus und öffentliche Kontrolle.",
 "FIA FOX is the civil-society answer: documentation, legal activism and public scrutiny.",
 "FIA FOX je odpoveď občianskej spoločnosti: dokumentácia, právny aktivizmus a verejná kontrola.",
 "FIA FOX je odgovor civilnog društva: dokumentacija, pravni aktivizam i javni nadzor.",
 "FIA FOX to odpowiedź społeczeństwa obywatelskiego: dokumentacja, aktywizm prawny i kontrola publiczna.",
 "FIA FOX es la respuesta de la sociedad civil: documentación, activismo jurídico y control público.",
 "FIA FOX è la risposta della società civile: documentazione, attivismo giuridico e controllo pubblico.",
 "FIA FOX est la réponse de la société civile : documentation, activisme juridique et contrôle public.",
 "FIA FOX är civilsamhällets svar: dokumentation, rättsaktivism och offentlig granskning.")
SITE_T = S("FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative",
 "FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative",
 "FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative","FIA FOX — Fair Internet Initiative")
SITE_S = S("Bürgerinitiative für faires Internet und fairen Wettbewerb in der EU",
 "Citizens' initiative for a fair internet and fair competition in the EU",
 "Občianska iniciatíva za férový internet a spravodlivú súťaž v EÚ",
 "Građanska inicijativa za pošten internet i pošteno natjecanje u EU",
 "Inicjatywa obywatelska na rzecz uczciwego internetu i konkurencji w UE",
 "Iniciativa ciudadana por un internet justo y competencia leal en la UE",
 "Iniziativa dei cittadini per un internet equo e concorrenza leale nell'UE",
 "Initiative citoyenne pour un internet équitable et une concurrence loyale dans l'UE",
 "Medborgarinitiativ för rättvist internet och sund konkurrens i EU")
NAV = [("♥", S("Spenden","Donate","Prispieť","Doniraj","Wesprzyj","Donar","Dona","Faire un don","Ge en gåva"), "DAR"),
       ("⚖", S("Fallregister","Case register","Register káuz","Registar predmeta","Rejestr spraw","Registro de casos","Registro dei casi","Registre des affaires","Ärenderegister"), "register.html"),
       ("◆", S("Soziale Medien","Social media","Sociálne siete","Društvene mreže","Media społecznościowe","Redes sociales","Social media","Réseaux sociaux","Sociala medier"), "teilen/"),
       ("▣", S("Galerie","Gallery","Galéria","Galerija","Galeria","Galería","Galleria","Galerie","Galleri"), "galerie/"),
       ("▤", S("Presse","Press","Tlač","Tisak","Prasa","Prensa","Stampa","Presse","Press"), "PREP"),
       ("≡", S("Mehr","More","Viac","Više","Więcej","Más","Altro","Plus","Mer"), ""),
      ]

SHA_BAN = "3d3ef3c0f812c7eab2996baee85469adf6224bde"
BAN = "https://raw.githubusercontent.com/peterferenc246-design/fia/" + SHA_BAN + "/banners/register_{L}.png"
FOTO = WP + "wp-content/uploads/2026/06/DSC_0680-na-kontakt-outlook-Peter-Ferenc-150DPI-2021_08_06-11_06_25-UTC.jpg"

SH_H = S("Diese Seite teilen","Share this page","Zdieľať túto stránku","Podijeli ovu stranicu","Udostępnij tę stronę",
 "Compartir esta página","Condividi questa pagina","Partager cette page","Dela denna sida")
SH = [
 (S("Auf Facebook teilen","Share on Facebook","Zdieľať na Facebooku","Podijeli na Facebooku","Udostępnij na Facebooku","Compartir en Facebook","Condividi su Facebook","Partager sur Facebook","Dela på Facebook"),
  "https://www.facebook.com/sharer/sharer.php?u=https://foxprof.club/"),
 (S("Auf X teilen","Share on X","Zdieľať na X","Podijeli na X-u","Udostępnij na X","Compartir en X","Condividi su X","Partager sur X","Dela på X"),
  "https://twitter.com/intent/tweet?url=https://foxprof.club/&text=FIA%20FOX"),
 (S("Auf LinkedIn teilen","Share on LinkedIn","Zdieľať na LinkedIn","Podijeli na LinkedInu","Udostępnij na LinkedIn","Compartir en LinkedIn","Condividi su LinkedIn","Partager sur LinkedIn","Dela på LinkedIn"),
  "https://www.linkedin.com/sharing/share-offsite/?url=https://foxprof.club/"),
 (S("Per Telegram teilen","Share via Telegram","Zdieľať cez Telegram","Podijeli putem Telegrama","Udostępnij przez Telegram","Compartir por Telegram","Condividi via Telegram","Partager via Telegram","Dela via Telegram"),
  "https://t.me/share/url?url=https://foxprof.club/&text=FIA%20FOX"),
 (S("Per E-Mail teilen","Share by e-mail","Zdieľať e-mailom","Podijeli e-poštom","Udostępnij e-mailem","Compartir por correo","Condividi via e-mail","Partager par e-mail","Dela via e-post"),
  "mailto:?subject=FIA%20FOX&body=https://foxprof.club/"),
 (S("Per WhatsApp teilen","Share via WhatsApp","Zdieľať cez WhatsApp","Podijeli putem WhatsAppa","Udostępnij przez WhatsApp","Compartir por WhatsApp","Condividi via WhatsApp","Partager via WhatsApp","Dela via WhatsApp"),
  "https://wa.me/?text=FIA%20FOX%20https%3A%2F%2Ffoxprof.club%2F"),
 (S("Auf Reddit teilen","Share on Reddit","Zdieľať na Reddite","Podijeli na Redditu","Udostępnij na Reddicie","Compartir en Reddit","Condividi su Reddit","Partager sur Reddit","Dela på Reddit"),
  "https://www.reddit.com/submit?url=https://foxprof.club/&title=FIA%20FOX"),
 (S("Auf Bluesky teilen","Share on Bluesky","Zdieľať na Bluesky","Podijeli na Blueskyju","Udostępnij na Bluesky","Compartir en Bluesky","Condividi su Bluesky","Partager sur Bluesky","Dela på Bluesky"),
  "https://bsky.app/intent/compose?text=FIA%20FOX%20https%3A%2F%2Ffoxprof.club%2F"),
 (S("Auf XING teilen","Share on XING","Zdieľať na XING","Podijeli na XING-u","Udostępnij na XING","Compartir en XING","Condividi su XING","Partager sur XING","Dela på XING"),
  "https://www.xing.com/spi/shares/new?url=https://foxprof.club/"),
]
SH_COPY = S("Link kopieren","Copy link","Kopírovať odkaz","Kopiraj poveznicu","Kopiuj link","Copiar enlace","Copia link","Copier le lien","Kopiera länk")
K_H = S("Kontakt","Contact","Kontakt","Kontakt","Kontakt","Contacto","Contatto","Contact","Kontakt")
K_ROLE = S("Initiator & Koordinator","Initiator & coordinator","Iniciátor a koordinátor","Inicijator i koordinator",
 "Inicjator i koordynator","Iniciador y coordinador","Iniziatore e coordinatore","Initiateur et coordinateur","Initiativtagare och samordnare")
K_ADR = S("Anschrift","Address","Adresa","Adresa","Adres","Dirección","Indirizzo","Adresse","Adress")
K_TEL = S("Telefon","Phone","Telefón","Telefon","Telefon","Teléfono","Telefono","Téléphone","Telefon")
F_NAME = S("Name","Name","Meno","Ime","Imię","Nombre","Nome","Nom","Namn")
F_MSG = S("Nachricht","Message","Správa","Poruka","Wiadomość","Mensaje","Messaggio","Message","Meddelande")
F_SEND = S("Absenden","Send","Odoslať","Pošalji","Wyślij","Enviar","Invia","Envoyer","Skicka")
SOC_H = S("Folgen Sie uns","Follow us","Sledujte nás","Pratite nas","Obserwuj nas","Síganos","Seguici","Suivez-nous","Följ oss")
FOOT_D = S("Datenschutzerklärung","Privacy policy","Ochrana osobných údajov","Zaštita podataka","Ochrona danych",
 "Protección de datos","Informativa privacy","Politique de confidentialité","Integritetspolicy")
FOOT_N = S("Inhalte gemäß journalistischem Privileg, Art. 85 DSGVO i. V. m. § 23 BDSG.",
 "Content under the journalistic privilege, Art. 85 GDPR in conjunction with § 23 BDSG.",
 "Obsah na základe novinárskej výsady, čl. 85 GDPR v spojení s § 23 BDSG.",
 "Sadržaj na temelju novinarske povlastice, čl. 85. GDPR-a u vezi s § 23. BDSG-a.",
 "Treści na podstawie przywileju dziennikarskiego, art. 85 RODO w zw. z § 23 BDSG.",
 "Contenidos al amparo del privilegio periodístico, art. 85 RGPD en relación con el § 23 BDSG.",
 "Contenuti in forza del privilegio giornalistico, art. 85 GDPR in combinato disposto con il § 23 BDSG.",
 "Contenus au titre du privilège journalistique, art. 85 RGPD combiné au § 23 BDSG.",
 "Innehåll enligt det journalistiska privilegiet, art. 85 GDPR jämförd med § 23 BDSG.")
SOC = [("Facebook","https://www.facebook.com/StopTelekomKartellEuropa","f"),
       ("X","https://x.com/FOXtiptop","X"),
       ("Instagram","https://www.instagram.com/fiasfoxspravodlivost/","IG"),
       ("LinkedIn","https://www.linkedin.com/in/foxpro-peter-ferenc-025913196/","in")]

REG_B = S("⚖ Zum Fallregister →","⚖ To the case register →","⚖ Do registra káuz →","⚖ U registar predmeta →",
 "⚖ Do rejestru spraw →","⚖ Al registro de casos →","⚖ Al registro dei casi →","⚖ Vers le registre →","⚖ Till ärenderegistret →")
MASCOT = "https://foxprof.club/wp-content/uploads/2026/06/fia-fox-mascot-v6.png"

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


def nav_item(ic, lb, k):
    if k == "DAR":
        return f'<a class="nv gold" data-k="DAR" href="#"><i>{ic}</i>{g(lb)}</a>'
    if k == "PREP":
        return f'<span class="nv prep" title="in Vorbereitung"><i>{ic}</i>{g(lb)}</span>'
    if k.endswith(".html"):
        return f'<a class="nv" href="{k}"><i>{ic}</i>{g(lb)}</a>'
    return f'<a class="nv" href="{WP}{k}" target="_blank" rel="noopener"><i>{ic}</i>{g(lb)}</a>'

nav_html = "".join(nav_item(ic, lb, k) for ic, lb, k in NAV)
banners = "".join(f'<a class="banl gtl-b {L}" href="register.html"><img class="ban" src="{BAN.format(L=L)}" alt="Verejny register"></a>' for L in LANGS)
share = "".join(f'<a class="shb" href="{u}" target="_blank" rel="noopener">{g(lb)}</a>' for lb, u in SH)
share += ('<a class="shb cp" href="' + WP + '" onclick="navigator.clipboard.writeText(\'' + WP + '\');'
          'this.classList.add(\'ok\');return false">' + g(SH_COPY) + '</a>')
socials = "".join(f'<a class="soc" href="{u}" target="_blank" rel="noopener" title="{n}">{i}</a>' for n, u, i in SOC)

HTML = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FIA FOX — Verejný register podvodov | Fair Internet Initiative</title>
<meta name="description" content="Verejný register právnych konaní iniciatívy FIA FOX: 7 káuz, 13 konaní, 29 dokumentov s podpismi a odpoveďami inštitúcií. Občianska iniciatíva za férový internet bez kartelov v EÚ.">
<link rel="canonical" href="https://register.foxprof.club/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://register.foxprof.club/">
<meta property="og:title" content="FIA FOX — Verejný register podvodov">
<meta property="og:description" content="7 káuz, 13 konaní, 29 dokumentov. Občianska iniciatíva za férový internet bez kartelov v Európskej únii.">
<style>
:root{{--navy:#1F3864;--hero:#2E5BA6;--red:#C00000;--gold:#FFD966;--soft:#D6E6F2;--bd:#c9d8e8}}
*{{box-sizing:border-box}}
body{{margin:0;color:#22303f;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
 background:linear-gradient(#8ec5ea 0%,#b9dcf3 38%,#dcecf8 68%,#eef6fc 100%);background-attachment:fixed;min-height:100vh}}
body::before{{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
 background:radial-gradient(circle at 82% 12%,#ffe680 0 42px,rgba(255,230,128,.35) 43px 78px,transparent 79px),
 radial-gradient(circle at 12% 16%,#fff 0 46px,transparent 47px),
 radial-gradient(circle at 20% 19%,#fff 0 34px,transparent 35px),
 radial-gradient(circle at 6% 20%,#fff 0 28px,transparent 29px),
 radial-gradient(circle at 62% 9%,#fff 0 30px,transparent 31px),
 radial-gradient(circle at 69% 11%,#fff 0 22px,transparent 23px),
 radial-gradient(circle at 40% 26%,#fff 0 24px,transparent 25px);opacity:.85}}
.pg{{position:relative;z-index:1}}
.top{{text-align:center;padding:22px 16px 6px}}
.top h1{{margin:0;font-size:23px;color:var(--navy);font-weight:800}}
.top .sub{{font-size:13.5px;color:#4a6076;margin-top:4px}}
.flags{{display:flex;justify-content:center;gap:6px;margin:12px 0 4px;flex-wrap:wrap}}
.f{{background:none;border:1px solid rgba(31,56,100,.35);border-radius:3px;padding:0;cursor:pointer;
 width:32px;height:21px;opacity:.55;overflow:hidden}}
.f img{{width:32px;height:21px;object-fit:cover;display:block}}
.f.on{{opacity:1;border-color:var(--navy);box-shadow:0 0 0 2px rgba(31,56,100,.25)}}
.side{{position:fixed;left:0;top:150px;z-index:5;display:flex;flex-direction:column;gap:8px}}
.nv{{display:flex;align-items:center;gap:8px;background:var(--navy);color:#fff;text-decoration:none;
 font-size:13px;font-weight:600;padding:9px 16px 9px 12px;border-radius:0 7px 7px 0;box-shadow:0 2px 6px rgba(0,0,0,.18);
 white-space:nowrap;max-width:210px}}
.nv:hover{{filter:brightness(1.12)}}
.nv i{{font-style:normal;font-size:13px}}
.wrap{{max-width:960px;margin:0 auto;padding:0 18px 60px}}
.proto{{background:#fff6d6;border:1px solid #f0c040;border-left:5px solid var(--red);
 padding:11px 15px;margin:10px 0 18px;border-radius:4px;font-size:13px}}
.hero{{background:var(--hero);color:#fff;padding:34px 36px;display:flex;align-items:center;gap:26px;flex-wrap:wrap}}
.hero .l{{flex:1 1 300px}}
.hero .r{{flex:0 1 290px;text-align:center}}
.hero .r img{{max-width:100%;height:auto;display:block;margin:0 auto}}
.hero h2{{margin:0;font-size:54px;font-weight:900;letter-spacing:.04em;line-height:1.05}}
.hero .fi{{color:var(--gold);font-size:23px;font-weight:600;font-style:italic;margin:8px 0 14px}}
.hero p{{margin:0;font-size:15.5px}}
.card{{background:#fff;border-radius:8px;box-shadow:0 2px 10px rgba(31,56,100,.10);overflow:hidden;margin-bottom:22px}}
.dar{{background:var(--soft);border:2px solid var(--navy);border-radius:8px;padding:26px 28px;text-align:center;margin-bottom:22px}}
.dar h3{{margin:0 0 12px;color:var(--navy);font-size:24px}}
.dar p{{margin:0 0 10px;font-size:15px}}
.dbtn{{display:inline-block;margin-top:8px;background:var(--red);color:#fff;text-decoration:none;
 border-radius:6px;padding:13px 38px;font-size:18px;font-weight:700}}
.dbtn:hover{{background:#a00000}}
.mis{{background:rgba(255,255,255,.82);border-radius:8px;padding:24px 28px;text-align:center;margin-bottom:26px}}
.mis h3{{margin:0 0 12px;font-size:24px;color:var(--navy)}}
.mis p{{margin:0 0 10px;line-height:1.7}}
.mis .b{{font-weight:700}}
.mis .n{{color:var(--navy);font-weight:700}}
h2.sec{{text-align:center;color:var(--navy);font-size:26px;margin:0 0 4px}}
p.secs{{text-align:center;color:#4a6076;font-size:13.5px;margin:0 0 18px}}
.kauza{{background:#fff;border-radius:8px;box-shadow:0 2px 10px rgba(31,56,100,.10);padding:20px 24px;margin-bottom:14px}}
.khead{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}}
.kauza h3{{margin:0;font-size:19px;color:var(--navy)}}
.cnt{{font-size:11.5px;color:#7a8899;text-transform:uppercase;letter-spacing:.07em;white-space:nowrap}}
.kpop{{margin:6px 0 14px;font-size:13.5px;color:#5a6a7d}}
.kon{{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;
 border-top:1px solid #e6edf5;padding:11px 0}}
.knaz{{font-size:14.5px;color:var(--navy);font-weight:600}}
.korg{{font-size:12.5px;color:#7a8899;margin-top:2px}}
.kside{{display:flex;align-items:center;gap:10px}}
.st{{font-size:11px;border-radius:999px;padding:2px 10px;white-space:nowrap}}
.st-laeuft{{background:#fff3d6;color:#8a5a00;border:1px solid #f0c040}}
.st-abgelehnt{{background:#fde8e8;color:#8a1c1c;border:1px solid #e8b4b4}}
.go{{font-size:12.5px;text-decoration:none;background:var(--navy);color:#fff;border-radius:4px;padding:5px 13px;white-space:nowrap}}
.go:hover{{background:#16294a}}
.soon{{font-size:12px;color:#9aa7b5;white-space:nowrap}}
.banl{{display:none}} body[data-l="de"] .banl.de,body[data-l="en"] .banl.en,body[data-l="sk"] .banl.sk,
body[data-l="hr"] .banl.hr,body[data-l="pl"] .banl.pl,body[data-l="es"] .banl.es,
body[data-l="it"] .banl.it,body[data-l="fr"] .banl.fr,body[data-l="sv"] .banl.sv{{display:block}}
.ban{{width:100%;height:auto;display:block}}
hr.sep{{border:0;border-top:1px solid rgba(31,56,100,.25);margin:26px 0}}
h3.c,h4.c{{text-align:center;color:var(--navy)}}
.shr{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}}
.shb{{background:var(--navy);color:#fff;text-decoration:none;border-radius:6px;padding:8px 16px;font-size:13.5px}}
.shb:hover{{background:#16294a}} .shb.cp{{background:#0B7A3B}} .shb.cp.ok{{background:#0a5c2e}}
.kon{{display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin-top:1em}}
.kon .kl{{flex:1 1 55%}} .kon .kr{{flex:0 1 38%;text-align:right}}
.kon .nm{{color:var(--navy);font-size:1.4em;font-weight:700;margin:0}}
.kon .rl{{color:#7A7A7A;font-style:italic;margin:.2em 0 0}}
.kon img{{max-width:100%;height:auto;border:1px solid var(--navy);border-radius:8px}}
table.kt{{width:100%;border-collapse:collapse;border:1px solid var(--navy);color:var(--navy);margin-top:1em;font-size:14px}}
table.kt td{{border:1px solid var(--navy);padding:10px 12px;vertical-align:top;width:50%}}
table.kt a{{color:var(--navy)}}
form.cf label{{display:block;font-size:14px;margin:14px 0 4px}}
form.cf .req{{color:var(--red)}}
form.cf input,form.cf textarea{{width:100%;border:1px solid var(--bd);border-radius:4px;padding:9px 11px;font:inherit;font-size:14px;background:#fff}}
form.cf textarea{{min-height:150px;resize:vertical}}
form.cf button{{margin-top:14px;background:#8a6d3b;color:#fff;border:0;border-radius:4px;padding:9px 22px;font:inherit;cursor:pointer}}
.socs{{display:flex;justify-content:center;gap:14px;margin-top:.6em}}
.soc{{width:42px;height:42px;border-radius:50%;background:var(--navy);color:#fff;text-decoration:none;
 display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px}}
.fl{{text-align:center;font-weight:600;margin-top:1.2em}} .fl a{{color:#8a6d3b}}
.fn{{text-align:center;color:#7A7A7A;font-size:.85em;font-style:italic;margin-top:.5em}}
.regcta{{background:linear-gradient(135deg,#fff 0%,#eef4fb 100%);border-radius:8px;box-shadow:0 2px 10px rgba(31,56,100,.10);
 border-left:5px solid var(--navy);padding:20px 26px;margin-bottom:22px;
 display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}}
.regcta .rt{{font-size:19px;color:var(--navy);font-weight:700}}
.regcta .rn{{font-size:13.5px;color:#5a6a7d;margin-top:3px}}
.regcta .rn b{{color:var(--navy);font-size:18px}}
.rbtn{{background:var(--navy);color:#fff;text-decoration:none;border-radius:6px;padding:11px 24px;font-weight:700;font-size:15px}}
.rbtn:hover{{background:#16294a}}
.nv.gold{{background:linear-gradient(#ffd34d,#f5b722);color:#3a2c00}}
.nv.prep{{opacity:.55;cursor:default}}
.foot{{margin-top:26px;padding:14px 0;border-top:1px solid var(--bd);font-size:12.5px;color:#4a6076;
 display:flex;gap:18px;flex-wrap:wrap;justify-content:center}}
.foot a{{color:#3a5570}}
@media(max-width:900px){{.side{{position:static;flex-direction:row;flex-wrap:wrap;justify-content:center;padding:8px}}
 .nv{{border-radius:6px}} .hero h2{{font-size:40px}}}}
.gtl,.gtl-b{{display:none}}
{show}
</style></head>
<body data-l="sk">

<div class="side">{nav_html}</div>

<div class="pg">
<div class="top">
 <h1>{g(SITE_T)}</h1>
 <div class="sub">{g(SITE_S)}</div>
 <div class="flags">{flags}</div>
</div>

<div class="wrap">


{banners}

<div class="card"><div class="hero">
 <div class="l">
  <h2>FIA&nbsp;FOX</h2>
  <div class="fi">Fair Internet Initiative</div>
  <p>{g(HERO)}</p>
 </div>
 <div class="r"><img src="{MASCOT}" alt="FIA FOX"></div>
</div></div>

<div class="dar">
 <h3>{g(DAR_H)}</h3>
 <p>{g(DAR_1)}</p>
 <p>{g(DAR_2)}</p>
 <a class="dbtn" id="dar" href="{WP}{DAR['sk']}" target="_blank" rel="noopener">{g(DAR_B)}</a>
</div>

<div class="mis">
 <h3>{g(MIS_H)}</h3>
 <p class="b">{g(MIS_1)}</p>
 <p>{g(MIS_2)}</p>
 <p class="n">{g(MIS_3)}</p>
</div>

<hr class="sep">
<h3 class="c">{g(SH_H)}</h3>
<div class="shr">{share}</div>

<hr class="sep">
<h3 class="c">{g(K_H)}</h3>
<div class="kon">
 <div class="kl"><p class="nm">Peter Ferenc</p><p class="rl">{g(K_ROLE)}</p></div>
 <div class="kr"><img src="{FOTO}" alt="Peter Ferenc"></div></div>
<table class="kt"><tbody><tr>
 <td>&#128205; <b>{g(K_ADR)}:</b><br>Rammelkam 2<br>84036 Kumhausen<br>Deutschland</td>
 <td>&#128231; <b>E-Mail:</b> <a href="mailto:info@foxprof.club">info@foxprof.club</a><br>
  &#127760; <b>Web:</b> <a href="{WP}">foxprof.club</a><br>
  &#128222; <b>{g(K_TEL)}:</b> <a href="tel:+4915731733332">+49 157 317 33332</a><br>
  &#128224; <b>Fax:</b> +1 231 538 6409</td></tr></tbody></table>

<form class="cf" id="cf">
 <label>{g(F_NAME)} <span class="req">*</span></label><input id="cf-n" required>
 <label>E-Mail <span class="req">*</span></label><input id="cf-e" type="email" required>
 <label>{g(F_MSG)} <span class="req">*</span></label><textarea id="cf-m" required></textarea>
 <button type="submit">{g(F_SEND)}</button></form>

<h4 class="c" style="margin-top:1.5em">{g(SOC_H)}</h4>
<div class="socs">{socials}</div>

<hr class="sep">
<p class="fl"><a href="{WP}impressum/" target="_blank" rel="noopener">Impressum</a> &nbsp;&#183;&nbsp;
 <a href="{WP}datenschutz/" target="_blank" rel="noopener">{g(FOOT_D)}</a></p>
<p class="fn">{g(FOOT_N)}</p>

<div class="foot">
 <a href="{WP}impressum/" target="_blank" rel="noopener">{g(UI["imp"])}</a>
 <a href="{WP}datenschutz/" target="_blank" rel="noopener">{g(UI["gdpr"])}</a>
 <a id="uvod" href="{WP}{UVOD['sk']}" target="_blank" rel="noopener">{g(UI["uvod"])}</a>
 <span>prototyp · dáta a šablóna oddelené</span>
</div>
</div></div>

<script>
var DAR = {DAR!r}, UVOD = {UVOD!r}, WP = "{WP}";
function setL(L){{
  document.body.dataset.l=L; document.documentElement.lang=L;
  document.querySelectorAll('.f').forEach(function(x){{x.classList.remove('on');}});
  var b=document.querySelector('.f[data-l="'+L+'"]'); if(b) b.classList.add('on');
  document.getElementById('dar').href  = WP + DAR[L];
  document.getElementById('uvod').href = WP + UVOD[L];
  document.querySelectorAll('.nv[data-k="DAR"]').forEach(function(a){{ a.href = WP + DAR[L]; }});
}}
document.querySelectorAll('.f').forEach(function(b){{
  b.addEventListener('click',function(){{ setL(b.dataset.l); }});
}});
document.getElementById('cf').addEventListener('submit',function(e){{
 e.preventDefault();
 var b=encodeURIComponent(document.getElementById('cf-n').value+' <'+document.getElementById('cf-e').value+'>'
   +String.fromCharCode(10,10)+document.getElementById('cf-m').value);
 window.location.href='mailto:info@foxprof.club?subject=FIA%20FOX&body='+b;
}});
setL('sk');
</script>
</body></html>"""

open('index.html','w',encoding='utf-8').write(HTML)
print("home:", len(HTML), "znakov |", len(KAUZY), "kauz |", total, "konani |", len(LANGS), "jazykov")
