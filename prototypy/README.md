# prototypy/

Ukazky mimo ostrej prevadzky. **Nic z tohto priecinka nie je napojene na foxprof.club**
a nic z toho nezasahuje do stranky #303 ani do materialov kauz.

## Struktura
- `index.html` — HOME: 6 kauz -> 14 konani, 9 jazykov.
  Darovaci portal ostava na WordPresse (GiveWP) — tlacidlo Podporit vedie na existujucu
  kampanovu stranku v jazyku vlajky (#107 DE, #243 EN, #256 SK, #403 HR, #407 PL, #408 ES,
  #409 IT, #410 FR, #411 SV). Impressum a Datenschutz tiez ostavaju na WordPresse.
- `dgcomp-karta-prototyp.html` — KARTA KONANIA DG COMP (12 poloziek, 9 jazykov).
- `gen_home.py`, `gen_karta.py` — generatory: hore DATA, dole sablona.
  Zmena polozky alebo konania = jeden riadok v DATA + spustenie skriptu.

## Pravidlo jedneho zdroja
Suhrny sa neduplikuju: kazda polozka karty ma tlacidlo, ktore skoci priamo na prislusnu spravu
v `dgcomp-correspondence-full.html` (kotva `#msg-N`). Register odkazuje na znenie, neopisuje ho.

## Zoskupenie kauz
Rozdelenie 14 konani do 6 kauz je NAVRH, nie rozhodnutie. Meni sa jednym riadkom v `gen_home.py`.

Ak sa prototyp neosvedci, cely priecinok sa zmaze jednym commitom a nic po nom nezostane.
