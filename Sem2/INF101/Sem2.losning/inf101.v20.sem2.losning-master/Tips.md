## Tips og triks

* [README](README.md) – for utfylling
* [Oppgavetekst](SEM-2.md)
* **Tips for å komme i gang**
* [Advanced](Advanced.md)


*Her ligger noen tips til oppgaven. Hvis du sitter fast kan denne lista hjelpe deg i gang.*

**NB: Spør gruppeleerne om hjelp og tips underveis.** Gruppelederne hjelper deg gjerne om du lurer på noe, er usikker på om det du har gjort er lurt, eller om du blir stående fast. 

Sjekk timeplanen for interaktive grupper på [Mattermost](https://mattermost.ii.uib.no/inf101v20/) eller ta kontakt med din gruppeleder på epost.  

## Hvordan komme i gang
Vi har to forslag til hvordan du kan angripe oppgaven. Du kan også gjøre en miks av disse to tilnærmingene.

#### 1. Bottom-up: Start med å skrive et program som "funker". 
Du kan starte med å lage et minimalt program som *funker*, men som ikke oppfyller krav for design og funksjonalitet. Etter hvert som du når mål for funksjonalitet, kan du begynne å dele programmet opp i flere klasser og pakker. 

For å jobbe på denne måten kan du velge *low-hanging fruit* - hva er den aller enkleste funksjonaliteten du kan tenke deg at programmet ditt har - og implementere det. Kanskje vil du kunne opprette, og skrive ut, et brett? Kanskje du kan ha som mål å skrive ut et 3x3 brett med x-er og o-er til terminalen? 

I denne tilnærmingen trenger du ikke tenke på kompliserte ting som regler, grafikk og win-conditions enda: bare implementer den ene tingen du valgte. 

Deretter velger du neste *low-hanging fruit* og implementerer det. Hvis du kan skrive ut et brett, hva med å ta imot input og fylle inn x-er og o-er basert på koordinater? Deretter kan du kanskje prøve å utvide programmet til å støtte forskjellige grids av forskjellige størelser.

Etter hvert som kodebasen din blir større og mer unhåndterlig kan du *refaktorere* den til klasser, metoder og interface. 

#### 2. Top-down: Start med å designe en model.
Hvis du liker å tenke abstrakt, kan det være du vil foretrekke å starte med å *modellere* problemet. Tenk over hva som er essensielle egenskaper ved de to spillene, hvordan du kan representere dem abstrakt og hvordan funksjonalitet kan deles mellom dem. 

([Hint](https://en.wikipedia.org/wiki/M,n,k-game))

Med denne tilnærmingen trenger du ikke tenke på detaljer som regler og win-conditions enda, men du vil kanskje ha nytte av å se på koden til forige oblig. Hvordan var spillet abstrahert der? 

For eksempel kan du tegne opp et diagram av interfaces og klasser du tror du trenger. Tenk på hvilke metoder og feltvariabler de må ha. Tenk på hvordan du vil skrive tester for dem. 

Deretter kan du implementere abstraksjonen ("modellen") din. Se [modellerings-delen](https://retting.ii.uib.no/inf101.v20.oppgaver/inf101.v20.sem1/-/blob/master/information/rogue.md) av Sem1 for et eksempel til hvordan du kan gjøre og beskrive dette. 

### Andre nyttige teknikker: 

**TDD.** Test Driven Development er et prinsipp for å utvikle kode der du *først* skriver testene, *deretter* koden. Fordelen med dette er at for å skrive tester må du tenke gjennom hvordan koden skal oppføre seg. Når du deretter gjør selve implementasjonen kan testene hjelpe deg med å finne feil.

**TDD + Refactoring = <3.** Hvis du utvikler solide tester, så kan du skrive koden din i sykler: 

1. Deklarer en type (et interface eller klasse)
2. lag tester som beskriver funksjonaliteten du vil ha
3. implementer funksjonaliteten så testene passerer
4. forbedre koden slik at den oppfyller godt OO-design
5. len deg tilbake og nyt følelsen av å jobbe organisert. 

**Penn og papir.** Bruk egne diagrammer flittig: hvis det blir mye å holde styr på, tegn opp klassene og hvordan de kaller hverandre. Utvid og endre på diagrammet etter hvert. Hvis du tror vi vil ha nytte av det til slutt så legg det gjerne ved innleveringen. 

**Rubberduck debugging.** Et klassisk programmerer-triks når du sitter fast er å forklare koden din. En gruppeleder er alltid et godt valg, men du kan også forklare den til samboeren din, bestemor, naboens hund, en potteplante eller gummiand. For mer info og en virtuell gummiand, sjekk ut [https://rubberduckdebugging.com/](https://rubberduckdebugging.com/). 

## Hva menes med brukergrensesnitt? 
Brukergrensesnittet er den delen av programmet som tar imot input fra "ekte" spillere (f.eks. du og gruppelederen din) og viser et output fra programmet. Typiske input er klikk-events eller streng-kommandoer; typiske output er å tegne brettet på i et grafikk-vindu eller ved hjelp av tegn og bokstaver i en terminal. Programmet må typisk kommunisere status på spillet, fortelle spillerne hvem sin tur det er og om noen har vunnet eller spillet er over. 

**Du trenger ikke å lage et grafisk brukergrensesnitt, det holder med tekst-interaksjon. Det viktige er at denne delen av koden din er klart skilt ut fra resten og godt dokumentert.**

Et tekstbasert brukergrensesnitt bruker konsoll-I/O med `Scanner` og `System.out.println()`, slik du så i Lab1. 

## Hva gjør jeg med den utleverte koden? 
Du har fått utlevert eksempelkode. **Du står fritt til å bruke eller slette koden du har fått utlevert**, men du må bruke prosjektstrukturen vi har gitt deg. Hvis du vil lage GUI kan du bruke den utleverte koden, eller skrive din egen. Hvis du vil bruke tekst-basert interaksjon kan du fritt slette eksempels-GUIet. 

## Forslag til bruk av INF101-konsepter
***Dette er ikke en sjekkliste du må oppfylle, og den er ikke komplett.*** Dette er en liste av INF101-konsepter som kan være nyttige og tips til hvordan å bruke dem. Du må sikkert bruke ting som ikke står på listen, og du kan gjerne la være å bruke ting fra listen dersom det ikke passer i koden din. 

* **Interfaces**. Det er naturlig at du bruker interface til å definere oppførselen til klassene dine. Der du kan bør du bruke interface-typen i stedet for klasse-typen. *Det gjør programmet ditt mer modulært og enklere å bytte ut kode.*
* **Arv**. Der du ser at objekter eller klasser deler oppførsel eller kode, kan du gjerne prøve å få til *gjenbruk av kode*. Det kan du gjøre ved at den ene arver fra den andre, eller at koden legges i en felles hjelper-klasse, eller abstrakt klasse. *Unntaket er hvis det bryter med abstraksjonen, altså virker ulogisk og rart.* 
* **Factory**. Dersom du trenger å lage mange objekter av en klasse, eller du trenger veldig typiske objekter med mange ganger, kan det være praktisk å legge inn en Factory. Dersom du oppretter objektene bare av og til, og det er kun et konstruktør-kall som skal til, er det ofte ikke vits å bruke fabrikker. Men hvis oppretting av objekter fører til at du må legge inn "boilerplate" kode, at du gjentar f.eks. if-setninger for fargevalg, eller liknende, er det nyttig å legge det inn i en Factory. 
* **Tester**. Test koden din så godt du kan. Se tidligere oppgaver for tips til hvordan. 
* **Forkrav**. Legg inn forkrav i metoder og konstruktører der det er nyttig. 
* **Datainvariant**. Legg gjerne inn datainvariant (sjekk på at feltvariablene har en gyldig kombinasjon av verdier) i klassene dine der du kan. Det vil hjelpe deg med debugging og regnes som en del av dokumentasjonen. 
* **Datastrukturer**. Se Grid fra tidligere oppgaver. 
* **Generisk type**. Datastrukturen din bør være generisk, og kanskje andre deler av programmet. 
* **Iterator**. Hvis du trenger å gå gjennom alle objeektene i en struktur (f.eks. en grid) kan det være nyttig å bruke iterator. 
* **Enum?** Det er ikke sikkert du trenger enums, men de kan ofte være hendige (kanskje for brikker?)
* **Klassediagram**. Tegn gjerne et diagram over koden din. Det er veldig nyttig for din egen del, og gjerne også for gruppelederne. 
* ***Abstraksjon***. Selv om koden fungerer er det nyttig å bruke abstraksjon til å gjøre koden din intuitiv for andre mennesker. 
* ***Innkapsling*** eller encapsulation. Pass på at du bruker private modifiers der du kan, og at du gjemmer vekk så mye som mulig av den indre tilstanden til klassene (feltvariabler, nøyaktig implementasjon). Det er nyttig å bruke interfaces til dette. 
