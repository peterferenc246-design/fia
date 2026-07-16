# FIA FOX — Formulár x5 ↔ živý register #303 (invariant)

Tento dokument je záväzný pre `Formular-podania-x5.html` a `cardedit.js`.
Cieľom je, aby sa knižnice formulára NIKDY nerozišli so živým registrom káuz na stránke #303
(slug `kauzy-koncept`, foxprof.club) a aby žiadne konanie/položka nevznikli bez väzby na formulár.

## Zdroj pravdy (dve vrstvy — nie protiklad)

- **Živý register #303 = zdroj pravdy o DÁTACH** (čo kauzy / konania / dokumenty naozaj existujú
  a ich aktuálne hodnoty). Nosič pravdy: atribút `data-snap` na KAŽDEJ položke (`.item`) —
  úplný autorský snímok (kauzaKey, kauza=názov konania, subj, dir, urls, dátum, prístup, vlákno…).
  `cardedit.js` funkcia `snapFor(item)` z neho zloží úplný editovateľný záznam a navrch prepíše
  živý stav z DOM. Register je teda kanonické úložisko; natvrdo zapísaný `CASES` vo formulári je
  len jeho fallback.

- **Formulár x5 = zdroj pravdy o SCHÉME / GENEROVANÍ** a je JEDINÝ autorský vstup. Každá položka
  sa rodí cezeň — preto vôbec má `data-snap`. Kartu do #303 nikdy nezavádzame na obídenie formulára.

## Uzavretá slučka (bez druhej kópie → bez driftu)

```
register #303 (data-snap na položkách)
        │  cardedit.js: snapFor() na VŠETKÝCH .item v #fia-kauzy AJ #fia-testcases
        ▼  postMessage {type:"fiafox-inventory", items:[snap,…]}  → iframe formulára
formulár: mergeLiveInventory(items) → doplní/aktualizuje KAUZY a CASES (aditívne, live prepisuje hardcoded)
        │  rozbaľovače Kauza / Konanie / Predmet dokumentu / Odpoveď na sa plnia z KAUZY/CASES
        ▼  buildSnap() → generovaný MK (data-snap) → Claude aplikuje na #303
register #303 (nový data-snap)  →  slučka sa uzavrie, round-trip konzistentná
```

## Mechanika (implementované)

### cardedit.js (beží na #303, len prihlásený admin)
- `harvestInventory()` — prejde `#fia-kauzy .item, #fia-testcases .item`, na každú `snapFor()`.
- `sendInventory(frame)` — pošle inventár do iframe formulára (`postMessage`, cieľový origin iframe).
- Odošle sa: 400 ms a 1500 ms po `init`, na `fiafox-inv-req` z iframe, a re-harvest po zmene DOM.
- `✏️ Upraviť` (a `↩ Odpovedať` pri došlých) sú na položkách v OBOCH kontajneroch.

### Formulár x5
- `mergeLiveInventory(items)` — pre každý snap: kanonizuje názov konania cez `caseId` (proti
  duplicitám), doplní `KAUZA_KEYS`/`KAUZY[kk].konania`, vytvorí/aktualizuje `CASES[konanie]`
  a `CASES[konanie].docs[subj]` (`_snapToDoc`). Aditívne — NIKDY nemaže. Live prepisuje hardcoded,
  ale NEDEGRADUJE existujúce per-jazyk odkazy, ak živý snap má len fallback.
- `slot.syncLive()` — po prijatí inventára aditívne prekreslí rozbaľovače; rozpracovaný slot
  (s vyplneným Predmetom) nechá bez zásahu, netknutý prekreslí.
- Po štarte si formulár vyžiada inventár (`fiafox-inv-req`).
- Fallback: kým inventár nedorazí (alebo pri chybe), formulár beží na hardcoded `KAUZY/CASES` —
  správanie sa nezhorší.

## Poistka pri vzniku (žiadne konanie/položka bez väzby)
V `collect()` po `buildSnap()`: položka sa NEVYGENERUJE, ak chýba `kauzaKey`, `kauza` (názov
konania) alebo `subj`. Vďaka tomu každá vygenerovaná položka nesie kompletný `data-snap`
a dá sa cez `snapFor` prečítať späť do formulára. Platí pre novú aj opravu, došlú aj odoslanú.

## Nasadenie (žiadny ZIP — Asset bol zrušený)
- `Formular-podania-x5.html` → commit do `peterferenc246-design/fia` → prehodenie SHA v
  rawcdn.githack iframe na #303.
- `cardedit.js` → commit → jsDelivr `@SHA` swap na #303 → purge
  (`https://purge.jsdelivr.net/gh/peterferenc246-design/fia@main/cardedit.js`).
- Zmena kariet v registri #303 samotná sa formulára netýka.
