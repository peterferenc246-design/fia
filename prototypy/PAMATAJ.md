# PAMÄTAJ — prototyp a darovacia kampaň

*Zápisník priečinka `prototypy/`. Claude ho číta pred prácou na prototype alebo na kampani, Peter doň dopisuje.*
*Zapísané 23.07.2026 na pokyn Petra.*

---

## Poradie priorít

Bez peňazí sa nedá viesť ani jedno z konaní, takže kampaň nie je odbočka od práce — je jej podmienkou.

To, čo je postavené v tomto priečinku, je presne to, čo kampaň potrebuje. Ľudia nedávajú peniaze na sľuby, dávajú ich na doložené veci. Register, kde je vidieť sedem kauz, trinásť konaní a dvadsaťdeväť dokumentov s podpismi a odpoveďami inštitúcií, je najsilnejší argument, aký sa dá mať. Ten sa nedá vymyslieť ani nahradiť textom.

---

## Čo na spustenie reálne chýba

**Platobná cesta stojí.** GiveWP je hotový v deviatich jazykoch (#107 DE, #243 EN, #256 SK, #403 HR, #407 PL, #408 ES, #409 IT, #410 FR, #411 SV). Toto riešiť netreba.

**Chýba jasné zadanie, čo za tie peniaze bude.** Dnes na darovacej stránke stojí, že príspevky slúžia na prevod iniciatívy na registrované združenie a na bežné náklady a koordináciu. To je príliš všeobecné na to, aby to niekoho pohlo. Kampaň potrebuje konkrétne číslo a konkrétny účel: koľko stoja súdne poplatky, koľko preklady, koľko prevádzka, aký je cieľ zbierky.

**Chýba stránka, kam kampaň smeruje.** Presse (#357) je koncept, nie je zverejnená, a bočné tlačidlo na ňu preto nevedie nikam. To je prvá vec, ktorú treba doplniť.

**Chýba anonymné darovanie.** Je to v úlohách od začiatku — zaškrtávacie políčko „Meno nezverejniť!". Bez neho nedá časť ľudí, ktorí nechcú byť verejne spájaní s konaním proti Telekomu.

**Chýba obrázok na zdieľanie.** Bez neho Facebook vytiahne náhodný obrázok zo stránky a príspevok vyzerá lacno. Potrebuje 1200 × 630 (pomer 1.91:1). Po nasadení pretlačiť cache cez FB Sharing Debugger → Scrape Again: https://developers.facebook.com/tools/debug/

---

## Čo vie Claude spraviť hneď

- Napísať text kampane — konkrétny, s číslami a účelmi, v deviatich jazykoch, aby sedel na existujúci GiveWP portál.
- Postaviť kampaňovú stránku, ktorá vedie z hero priamo na register ako dôkaz.
- Vyrobiť podklad pre obrázok na zdieľanie.

Sú to hodiny, nie dni. Chýbajú k tomu tri čísla od Petra: **cieľová suma zbierky**, **doterajšie náklady na súdne poplatky a preklady**, **primeraná mesačná suma na živobytie koordinátora**.

---

## Upozornenie, ktoré chráni Petra

Ak časť peňazí má ísť na jeho živobytie, musí to byť v texte napísané. Nie skryté pod „koordináciou iniciatívy".

Dôvod je praktický aj právny: zbierka na neregistrovanú iniciatívu v Nemecku má svoje pravidlá a nepresný účel je presne to, čím sa dá kampaň spochybniť — a protivníci majú dôvod hľadať. Vetu typu „časť prostriedkov kryje životné náklady koordinátora, ktorý na iniciatíve pracuje na plný úväzok" ľudia prijmú. Zamlčanie neprijmú, ak to raz vyjde najavo.

Claude nie je daňový ani právny poradca a pravidlá pre zbierky si musí Peter overiť — ale je to jednoduchšie spraviť teraz než opravovať potom.

---

## Otvorené a časovo citlivé mimo kampane

**M.10815 — lehota na žalobu.** Nie je uzavreté, či dvojmesačná lehota podľa čl. 263 šiesteho odseku ZFEÚ proti rozhodnutiu Generálneho sekretariátu z 03.02.2026 neuplynula okolo polovice apríla 2026 (dva mesiace + desaťdňová lehota z dôvodu vzdialenosti). Podľa ustálenej judikatúry potvrdzujúci akt ani odpoveď na list uplynutú lehotu neotvárajú. **Register sa dá dogenerovať kedykoľvek, lehota nie.**

---

## Štandard písania verejných textov

Pre kampaň, Presse, sociálne siete a verejné súhrny platí kontrolný zoznam „Signs of AI writing":
bez nafukovania významu, bez promo jazyka, bez vágneho pripisovania, bez pravidla troch, bez výplňových fráz.
Namiesto prídavných mien konkrétne čísla, dátumy a spisové značky.

**Na právne podania sa tento štandard neuplatňuje.** Tam je neutrálny vecný tón správny a citácie, dátumy, spisové značky ani odkazy na články predpisov sa nikdy neparafrázujú.

---

## Stav prototypu k 23.07.2026

| Súbor | Čo to je |
|---|---|
| `index.html` | Home vo vzhľade foxprof.club — hero s maskotom, vstup do registra, darovací box, misia, bočné menu |
| `register.html` | Register — dlaždice kauz, filtre DE/SK/EU, radenie, zoznam konaní |
| `karta-case-*.html` | 13 kariet konaní, každá s odoslanými a došlými dokumentmi a súhrnmi v 9 jazykoch |
| `_data/fia_data.json` | Dáta vyťažené zo #303: 18 kariet, 29 položiek, 17 súhrnov (153 jazykových verzií), 7 kauz |
| `_data/extract.py` | Extraktor z exportu WordPressu — beh 0,08 s |
| `_data/gen_live.py` | Generátor registra a všetkých kariet — beh 0,04 s |

Ostrý web foxprof.club a stránka #303 bežia nezmenené. Nič z tohto priečinka do nich nezasahuje.

---

## Poznámky Petra

*(sem píš — Claude to prečíta pri ďalšej práci)*
