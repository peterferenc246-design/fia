---
name: fia-mk
description: >
  Jednotný Skill pre údržbu registra káuz FIA FOX na WordPress stránke #303
  (slug kauzy-koncept, foxprof.club). Riadi sa VÝHRADNE vstupným MK blokom, ktorý
  určí Objekt (KARTA | POLOŽKA | DOKUMENT | DLAŽDICA), Akciu (PRIDAŤ | OPRAVIŤ |
  VYMAZAŤ) a Smer (ODOSLANÉ | DOŠLÉ, len pri POLOŽKA). Použi VŽDY, keď Peter chce:
  pridať/opraviť/vymazať kartu konania alebo položku (odoslané/došlé) na #303;
  opraviť 9-jazyčný .gtl text, subj, meta, spis, Az., orgán, dátum, stav, prístup;
  pridať/opraviť doc-link; pridať konanie do dlaždice #fia-reg; alebo zaviesť/
  aktualizovať viacjazyčný VLAJKA-VIEWER klon podania (preklad SK originálu do
  EN/DE/FR/HR/PL/IT, zlúčenie do jedného PDF, commit, napojenie 9 vlajok na
  viewer.html). Spúšťače: "pridaj kartu", "oprav kartu", "vymaž kartu/položku",
  "nová odoslaná/došlá položka", "oprav spis/Az./orgán/dátum/stav", "oprav gtl",
  "oprav doc-link", "pridaj konanie do dlaždice", "viacjazyčný klon", "VLAJKA-VIEWER",
  "prelož podanie na kartu", "napoj vlajky".
---

# FIA · #303 — jednotný Skill `fia-mk` (riadený MK)

## 0. ŽELEZNÉ PRAVIDLÁ (platia vždy, vo všetkých vetvách)
- **O všetkom rozhoduje MK.** Skill sa nespýta „čo" — prečíta `Objekt/Akcia/Smer` z MK a vykoná príslušnú vetvu bez ďalších otázok. Chýba pole → doplň logicky (Smer má zmysel len pri POLOŽKA) a pokračuj.
- **Nikdy nepublikujem naživo.** `wp_section_replace` upravuje už zverejnenú #303 in-place (status sa nemení). Publikuje výhradne Peter cez Rýchlu úpravu.
- **Chirurgické zápisy.** `old_str` musí byť presný reťazec z ČERSTVÉHO `wp_page_read(raw=true)` a mať **presne 1 výskyt**. Ak nie je unikátny → rozšír kontext. Nikdy Find&Replace v Gutenbergu.
- **Zákaz wholesale prepisu položky/karty** — zničí `data-thread`, `data-snap`, badge, komentárové kotvy. Meň len to, čo treba.
- **Bez nevyžiadaných prvkov** (thread badge, replyTo, `.thr`) — len ak MK žiada.
- **9 jazykov vždy** v poradí `de, en, sk, hr, pl, es, it, fr, sv`. DE = base pre DE-jurisdikciu, SK = base pre SK originály. ES a SV → EN, ak nie sú explicitne zapnuté.
- **user_confirmed=true** až po Petrovom „vykonaj/choď". Pred tým `over` = len diagnóza.
- **Pred zápisom preveriť dôverné dokumenty** (VERTRAULICH v prebiehajúcom konaní = procesné riziko).
- **Doručujem len vyžiadaný typ výstupu.** Žiadne bonusové DOCX/pracovné súbory.

## 1. PEVNÉ ÚDAJE (zapečené — Peter ich neopakuje v MK)
- **Podávateľ:** Peter Ferenc · Rammelkam 2, 84036 Kumhausen, Deutschland · info@foxprof.club · +49 157 317 33332 · FAX +1 231 538 6409
- **Stránka:** #303, slug `kauzy-koncept`, foxprof.club. Nástroje: `MCP Azure 8888:wp_page_read(page_id,offset,max_chars,raw=true)`, `MCP Azure 8888:wp_section_replace(page_id,old_str,new_str,user_confirmed)`.
- **LOKALIZÁCIA V #303 — nikdy neprehľadávaj stránku naslepo.** #303 má cez 730 000 znakov; hľadanie jednej položky sondami stojí rádovo viac tokenov než celý zdrojový dokument. Pozície drží **`tools/303_index.json`** v repe (kotva → offset). Postup: (1) načítaj index, (2) choď rovno na offset a **over malým oknom ~600 zn.**, že si na správnom mieste, (3) až potom čítaj presný výsek. **Po KAŽDOM `wp_section_replace` index aktualizuj:** nástroj vypíše `old=X zn., new=Y zn.` → posun = `Y − X`; priraď ho ku VŠETKÝM offsetom väčším než miesto zásahu (offsety pred zásahom sa nemenia). Robí sa to aritmeticky, **bez ďalšieho čítania = zadarmo**. Ak index chýba alebo overenie nesedí, dohľadaj sondami po 600 zn. a index doplň/oprav. Index nikdy neuchovávaj v texte Skillu — čísla starnú po každom zápise.
- **GitHub:** repo `peterferenc246-design/fia` (branch main). Token: `cat /home/claude/gh.dat | tr -d ' \n\r\t'` — **nikdy neechovať, nikdy nerevokovať**. Binárne (PDF <1 MB) najjednoduchšie cez **Contents API** PUT `/repos/.../contents/{path}` s `{message, content:<base64>, branch:"main"[, sha ak prepis]}`: base64 zapíš do SÚBORU (`base64 -w0 "$SRC" > /tmp/b64.txt`) a payload cez `json.dump({...}, open("/tmp/payload.json","w"))` do SÚBORU, potom `curl -d @/tmp/payload.json`. **NIKDY base64 cez argv** (Argument list too long) a **NIKDY nepresmeruj python stdout do toho istého payload súboru** (rozbije JSON). Commit SHA = `resp['commit']['sha']`. Väčšie/viacsúborové cez Git Data API (blob→tree→commit→PATCH ref). Nový HEAD SHA cez `git ls-remote`. Ak `git push` cez `http.extraheader` zlyhá na „invalid credentials", použi token v URL: `https://x-access-token:{TOK}@github.com/...`.
- **CDN:** `https://cdn.jsdelivr.net/gh/peterferenc246-design/fia@{SHA}/docs/{FILE}.pdf` (SHA-pin, hneď čerstvé).
- **VLAJKA-VIEWER:** produkčná báza `https://peterferenc246-design.github.io/fia/viewer.html` (GitHub Pages, `.nojekyll`, žiadny build → commit = redeploy ~1 min; NIE jsDelivr — HTML tam nemá MIME na navigáciu, NIE githack — interstitial).
  Parametre: `doc`=DOC1 (klon prekladov `..._ALL.pdf`, jsDelivr @SHA), `doc2`=DOC2 (**podpísaný originál INTACT** na GitHube, jsDelivr @SHA — **nikdy nerozdeľuj**, PDF.js ho renderuje read-only a QES/PAdES zostáva platný), `orig`=OneDrive link na reálne odoslaný podpísaný súbor (button „⬇ Podpísaný originál (QES)"), `langs=CODE:PAGE[:2|:o],...` (`:2`=jazyk žije v doc2/podpísanom, `:o`=externý odkaz na `orig` v novom tabe — legacy), `d` (1|2 aktívny doc), `page` (úvodná strana).
  - **Robustný skok (nutné vo viewer.html):** `history.scrollRestoration="manual"`, natívny `scrollTo` s offsetom pod sticky hlavičku, retry kým `cur==target`. Krehký `scrollIntoView({behavior:"instant"})` padá na str.1 → všetky vlajky by ukázali titulku.
  - **Cache:** po úprave `viewer.html` prehliadač (najmä inkognito celú session) drží starú verziu → over cez hard-refresh (Ctrl+Shift+R) alebo cache-bust `&vw=N` v URL a bumpni N pri ďalšej zmene viewera. Príznak starej verzie: „str. 1 / 39" (klon) namiesto „9 / 15" (podpísaný).
- **Assety:** `sig.png` v repe = **čisté modré ťahy, BEZ zapečeného mena** (opravené 18.07.2026; pôvodný defektný odložený ako `sig_legacy_with_text.png`). Pre DOCX klony `sig_hires_clean.png` (1000×543, ostrejší). Kompaktné bannery generuje `tools/mkbanner.py` (pomer ~2,8, šírka 3,6 cm).
- **DOCX štandard (FIA):** Calibri 11; okraje 1,6/1,6/2,2/2,2 cm; banner hore VPRAVO šírka ~3,6 cm; nadpisy navy `#1F3864`; page-break medzi pod-dokumentmi.
- **VEĽKOSŤ PÍSMA V KLONOCH:** klon, ktorý staviam OD NULY (WeasyPrint/HTML — listy súdu, e-maily, uznesenia), má telo textu **VŽDY 12 pt**. Podriadené prvky (rámček o ochrane údajov, pätička, poznámka pod čiarou) môžu byť menšie v pomere k originálu. **Výnimka:** klon stavaný Z PETROVHO WORDU (`tools/build_docx_clone.py`) si veľkosť písma PREBERÁ z jeho dokumentu a NEMENÍ ju — tam sa 12 pt nevynucuje. Potvrdené 18.07.2026.
- **PODPISOVÝ BLOK:** 2-stĺpcová tabuľka BEZ okrajov, `w:cantSplit` (nikdy cez 2 strany). Vľavo (bottom): záver + „Miesto, dátum". Vpravo (bottom): podpis NAD STREDOM bodkovanej čiary (šírka ~3,4 cm), pod ním bold „Peter Ferenc ...............". **Nikdy plávajúci textbox** — pri dlhšom preklade (FR/ES/IT) ho vytlačí pod spodný okraj a orežе sa.
- **Orgán label (9 jaz.):** DE Behörde · EN Body · SK Orgán · HR Tijelo · PL Organ · ES Órgano · IT Organo · FR Autorité · SV Myndighet.

## 1a. ČÍTANIE ZDROJOV — TOKENOVÁ DISCIPLÍNA (platí pre KAŽDÉ podanie)
- **Text na preklad ber VÝHRADNE z MD.** MD nesie text aj formátovanie naraz (`**tučné**`, nadpisy, odrážky) — jeden tok, jedno čítanie.
- **Word sa do kontextu NIKDY nenačítava.** Slúži len ako predloha formátovania pre kód: `python-docx` číta štýly a odseky, LibreOffice (`soffice --headless --convert-to pdf`) renderuje. Súbor na disku nestojí nič bez ohľadu na veľkosť.
- **Nevypisuj štruktúru Wordu do konverzácie.** Nechaj kód spárovať bloky MD s odsekmi Wordu potichu a vypíš JEDINÝ kontrolný riadok: `N blokov MD, M odsekov Wordu, K nespárovaných`. Odhalí to aj prípad, keď MarkItDown nezachytí obsah textových polí (podpisový blok!).
- **Podpísané PDF nečítaj celé.** Vypíš si ~300 znakov z niekoľkých strán len na zistenie, ktoré jazyky sú v ňom a na ktorých stranách (`pypdf`), NIKDY nehádaj.
- **Ak MD nie je**, nechaj kód vytiahnuť text z Wordu rovno v markdownovom tvare (s tučnými úsekmi) a vypísať RAZ — vyjde to nastarovnako ako MD.
- **Poradie nákladov (od najdrahšieho):** hľadanie v #303 bez indexu ≫ text na preklad > kontrolné výpisy > súbory na disku (zadarmo).

## 2. VSTUP (MK — Peter vypĺňa pri každom zadaní)
```
• Objekt:  KARTA | POLOŽKA | DOKUMENT | DLAŽDICA
• Akcia:   PRIDAŤ | OPRAVIŤ | VYMAZAŤ
• Smer:    ODOSLANÉ | DOŠLÉ            (len ak Objekt=POLOŽKA)
• Karta:   case-XXXXX                  (slug na #303; pri PRIDAŤ KARTA navrhni slug z názvu)
• Dáta:    [subj / spis / Az. / orgán / dátum / jurisdikcia / oblasť / prístup pub|pwd / stav …]
── len ak Objekt=DOKUMENT: ──
• Autoritatívny zdroj: [MD (preklad) + Word (formátovanie) v jednom RAR]   ← prekladá sa VŽDY z MD, NIKDY z PDF-extraktu
• Podpísaný originál (súbor + orig=): [reálny podpísaný PDF súbor + OneDrive/SharePoint link naň]   ← POVINNÉ. Reálne ODOSLANÝ podpísaný dokument. **Commitne sa INTACT na GitHub a použije ako `doc2`; OneDrive link ide do `orig=`.** Jazyky a ich strany zisti `pypdf` (NEHÁDAJ).
• Klonovať jazyky (do doc1 `_ALL.pdf`): [len jazyky, ktoré NIE sú v podpísanom origináli]
• Placeholder → EN:     [napr. ES, SV — ak sa neprekladajú]
• Typ/adresát:          [napr. Beschwerde · O2 Telefónica Germany]
```

## 3. DIAGNÓZA (vždy prvý krok pred akýmkoľvek zápisom)
Pozíciu vezmi z `tools/303_index.json` (§1), over malým oknom, potom prečítaj ČERSTVÝ raw výsek okolo `case-XXXXX` (`wp_page_read raw=true`). Nájdi presné kotvy: `data-snap`, `cmtid`, `data-thread`, `id="case-…"`, dlaždicu `#fia-reg .rbtn[data-ids~="case-…"]`. Nikdy nehádaj reťazce.

## 4. VETVENIE (switch podľa MK)

### 4.1 Objekt = DOKUMENT  (VLAJKA-VIEWER viacjazyčný klon)
Akcia PRIDAŤ (nový dokument) alebo OPRAVIŤ (predělať/rewire preklady). Postup:
1. Načítaj MD (§1a). Rozlož na odseky; zdieľané indexy nadpisov/podnadpisov pre všetky jazyky.
2. **KLON SA STAVIA Z PETROVHO WORDU, nie z vlastného layoutu.** `tools/build_docx_clone.py`: naklonuje DOCX, vymení LEN text (zachová Calibri/okraje/štýly/zarovnania/tučné úseky/hypertextové e-maily/zalomenie sekcií), vloží jazykový banner ako **plávajúci ukotvený objekt** (nezaberá riadok) a čistý podpis. Prevod cez LibreOffice.
   - **Pozor na ukotvenú grafiku:** pri výmene textu odstraňuj LEN behy s `w:t`; beh s `w:drawing`/`w:pict`/`mc:AlternateContent` nechaj — inak zmizne podpisový blok.
   - **Prázdne odseky nemajú behy** — ich výšku určuje `w:pPr/w:rPr/w:sz` (značka odseku). Bez toho fit-pass nezaberá.
   - **FIT-PASS:** FR/ES/IT sú dlhšie než SK; originál má N strán → klon musí mať tiež N. Stláčaj postupne LEN prázdne medzery, odstupy a riadkovanie (text ani veľkosť písma NIE).
3. **BREAKPOINT — FR VZORKA NAJPRV.** Vyrenderuj celý **FR** klon, over meraním (banner ~3,6 cm a pomer ~2,8; podpis nad STREDOM bodkovanej čiary — odchýlka 0,00 cm; počet strán = ako originál). **Doruč FR PDF Petrovi a ZASTAV.** Pokračuj až na „pracuj".
4. Po „pracuj": zvyšné jazyky rovnakým skriptom (`tools/lang_XX.py` = mapovanie index odseku → [(text, bold)] + LABELS pre odseky s hypertextom + BOXES pre záverečný blok).
5. **TRI SÚBORY — nikdy nezamieňať:**
   - **`doc1`** = `..._clone_ALL.pdf`: MERGE klonov jazykov, ktoré **nie sú** v podpísanom origináli.
   - **`doc2`** = **podpísaný originál INTACT**, commitnutý bez rozdelenia (chráni PAdES/QES).
   - **`orig=`** = OneDrive link na ten istý reálne odoslaný podpísaný súbor. POVINNÉ vo všetkých 19 URL.
   - **Mapu strán zisti `pypdf` pre OBA súbory.** Ak je jazyk aj v doc2 aj v doc1 → **preferuj doc2** (`:2`).
6. Commit oboch do `docs/` (Contents API per §1). **Overenie:** stiahni späť cez `raw.githubusercontent.com` a skontroluj počet strán + prítomnosť `/Sig` poľa v podpísanom (QES musí ostať).
7. **WIRE 19 viewer URL** na karte `case-XXXXX` — data-snap `fallback` + 9× `urls{de..sv}` + 9× viditeľných `.open` href (poradie de,en,sk,hr,pl,es,it,fr,sv):
   `viewer.html?doc=<@SHA/doc1>&doc2=<@SHA/doc2>&orig=<OneDrive>&langs=CODE:PAGE[:2],...&d=<1|2>&page=<N>`
   - **Konvencia escapovania:** v `data-snap` `&amp;`, vo viditeľnom `href` obyčajné `&`.
   - **Efektívny zápis = 2 chirurgické writy**, nie 19: (a) blok `"fname":…,"fallback":…,"urls":{…9…}` naraz, (b) blok 9 `.open` spanov naraz (+ `admin-fname` span pred ne). Oba `old_str` sú unikátne vďaka konkrétnej URL dokumentu.
   - **Reťazce generuj PROGRAMOVO** (python vypíše starý aj nový aj ich DĹŽKY), NIKDY neprepisuj SHA ručne. **Kontrola správnosti prepisu:** nástroj po zápise vráti `old=X, new=Y` — musí sedieť s vypočítanými dĺžkami.
   - Po zápise **aktualizuj `tools/303_index.json`** (§1).
8. Doruč LEN výsledné PDF klony + priamy viewer `@SHA` link na kontrolu naživo. Žiadne pracovné DOCX.

### 4.2 Objekt = KARTA
- **PRIDAŤ:** nová karta konania **VÝHRADNE cez x5 formulár** (`Formular-podania-x5.html`) — priprav dáta do x5, Peter vloží, potom SHA swap iframe. **Obísť x5 = zakázané** aj keď mám všetky dáta. Prvky: `id="case-…"` (slug z názvu), 9× `.gtl` subj/court-subj/meta, `data-cat`/`data-area`/`data-court`/`data-az`/`data-ourref`, share placeholder (Zdieľať/Teilen — menu kreslí kauzy.js).
- **OPRAVIŤ:** chirurgický `wp_section_replace` konkrétneho reťazca (subj/meta/spis/Az./orgán/dátum/stav/gtl). Ak sa mení spis/Az./orgán/dátum → uprav **aj** `data-*` atribúty **aj** `data-snap` (inak cardedit prepíše z DOM). Orgán label podľa §1.
- **VYMAZAŤ:** odstráň celý `<details class="case" id="case-…">…</details>` (aj modál `#case-…-modal`) + **očisti dlaždicu** `#fia-reg` (`data-ids`, počet konaní). Skontroluj osirelé `cmtid`/`data-thread`.

### 4.3 Objekt = POLOŽKA  (komunikačná položka v karte; Smer rozhoduje stĺpec)
- **PRIDAŤ:** nová položka **cez x5** (Smer=ODOSLANÉ → 1. `.col`; Smer=DOŠLÉ → 2. `.col`). Po vložení SHA swap. Nikdy neobísť x5.
- **OPRAVIŤ:** chirurgický `wp_section_replace` položky (subj/date/access/doc-link/9× gtl). Zachovaj `data-snap`, `cmtid`, `data-thread`, kotvy. **Ak MK nemá pole medzi ZMENENÝMI, nechaj ho tak** — napr. 9-jazyčné preklady `.subj`, ktoré už na karte sú, sa neprepisujú jednojazyčným textom z formulára.
- **VYMAZAŤ:** odstráň blok `<div class="item"…>…</div>`, uprav `.cnt` počítadlo stĺpca, očisti `cmtid`/`data-thread`/modál. Ak bola posledná v konaní → zváž dlaždicu.

### 4.4 Objekt = DLAŽDICA  (#fia-reg register tile)
Uprav `data-ids` (pridaj/odober `case-…`), `data-spis`, a počet konaní na dlaždici. Chirurgicky, 1 výskyt.

## 5. PRÍKAZY
- **„choď" / „vykonaj"** = spusti postup pre daný MK (pri DOKUMENT: krok 1–3, t.j. FR vzorka, potom čakaj).
- **„pracuj"** = pokračuj tam, kde si skončil (dokonči zvyšné jazyky + merge + commit + wire).
- **„choď <JAZYKY>"** = dorob ďalšie jazyky (napr. „choď ES SV") a re-wire.
- **„over"** = len diagnóza (raw čítanie), bez zápisu.

## 6. VÝSTUP
Podľa MK: potvrdenie zápisu (karta/položka/dlaždica) alebo PDF klony + viewer @SHA link (dokument). Nový HEAD SHA uveď vždy pri commite. Nikdy nepublikuj — swap odkazu / edit in-place je jediný zápis. Po každom zápise do #303 aktualizuj `tools/303_index.json`.
