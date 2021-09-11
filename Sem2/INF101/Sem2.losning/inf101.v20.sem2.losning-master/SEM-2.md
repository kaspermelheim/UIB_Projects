# [Semesteroppgave 2: Fire på rad og Tripp-trapp-tresko]

* [README](README.md) – for utfylling
* **Oppgavetekst**
* [Tips for å komme i gang](Tips.md)
* [Advanced](Advanced.md)

## Læringsmål
- Utvikle objekt-orienterte program fra scratch 
- Spesifisere, implementere og teste ditt eget design 
- Dokumentere og motivere egne designvalg

## Intro
Denne oppgaven går ut på å lage et program for å spille [Fire på rad](https://en.wikipedia.org/wiki/Connect_Four) og [Tripp-trapp-tresko](https://en.wikipedia.org/wiki/Tic-tac-toe). 

**Fire på Rad** spilles tradisjonelt ved at to personer slipper brikker av forskjellige farger ned i en tom, stående plastramme. Adskilte kolonner gjør at brikkene legger seg oppå hverandre og fargene danner rader loddrett, vannrett og diagonalt. Den første spilleren som klarer å få få fire på rad av sin egen farge vinner spillet.

![](img/Connect_Four.gif)

**Tripp-trapp-tresko** spilles tradisjonelt ved help av penn og papir på et 3x3 rutenett. Spillerne tegner typisk opp rutenettet som to vertikale og to horisontale linjer, og bytter på å fylle inn sirkler og kryss i rutene til en spiller får tre på rad, eller alle rutene er fulle. 

![](img/TicTacToe.gif)

**Ditt program** skal støtte begge spillene. To spillere skal kunne spille mot hverandre, og én spiller skal kunne spille mot en AI. 

## Krav til programmet
***Her beskriver vi funksjonelle krav til programmet og essensielle krav for å bestå.***

**Du må utvikle koden din selv.**
Du får kun utlevert et tomt Java-prosjekt og må lage klasser, pakker og tester selv. Løsningen blir vurdert på funksjonalitet, kodekvalitet, dokumentasjon og testing og at den viser forståelse av INF101-konsepter. 

**Programmet må støtte både Tripp-trapp-tresko og Fire på rad.**
For eksempel kan man ved oppstart bli spurt om hvilket spill man ønsker å spille. *Begge spillene skal oppføre seg i henhold til sine regler.* 

**Programmet må støtte både én og to spillere.** To spillere må kunne spille mot hverandre på samme maskin, for eksempel ved å ha hver sin tur til å gi input. Én spiller må kunne spille mot datamaskinen: du må altså implementere en enkel AI for begge spillene. *Du kan få maks uttelling selv om AIen din gjør dumme valg.* Du kan få ekstrapoeng for smart AI. 

**Programmet må ha brukergrensesnitt.**
Vi aksepterer program som spilles via terminalen ved hjelp av tekst-input og program som spilles med grafisk, klikkbart grensesnitt. Du kan få maks uttelling selv om du har tekst-basert grensesnitt. *Du trenger kun implementere én av delene.* 

**Programmet må være velskrevet, forståelig, testet og dokumentert i henhold til INF101-pensum.** Et program som kjører perfekt, men som mangler tester, dokumentasjon, objekt-orientert design og [README.md](README.md) risikerer stryk.

**Du må fortelle oss hvordan vi skal rette programmet ditt.** Filen [README.md](README.md) skal inneholde din beskrivelse av hvordan man kjører programmet ditt, hva slags funksjonalitet du støtter, hvordan koden er organisert, kjente bugs og work-arounds, samt alle designvalg du har tatt. *Vi bruker din beskrivelse av programmet ditt for å gi deg poeng og  vil kun rette kode og funksjonalitet som du beskriver i [README.md](README.md).*

**Programmet ditt må ligge i prosjektet du har fått utdelt av oss.** For at vi skal kunne enkelt kjøre og teste koden din har vi gitt deg et tomt Java prosjekt. Du må levere programmet ved hjelp av dette prosjektet: program-koden skal ligge i `main` og test-kode i `test`. Resurser som bilder og liknende legges i `resources`. *Alle kodefiler, resurser og dokumentasjon må være levert til ditt online GitLab repositorie for at vi skal rette det.*

### Poeng og vurdering
Hvor mange poeng du får på oppgaven kommer an på hvor god løsningen din er. Både Fire på rad og Tripp-trapp-tresko er relativt enkle spill å implementere, og *kan* skrives i én fil uten klasser og metoder (i INF100-stil). ***Et program skrevet på denne måten tilsvarer stryk selv om det støtter all funksjonalitet.*** 

Vi forventer så klart at programmet oppfører seg cirka som det skal, men for å få god uttelling må du i tilegg vise at du kan bruke objekt-orientering på en god måte, og at du kan teste og dokumentere koden din. 

***Det er bedre å levere en oppgave som har høy kvalitet på koden og et par bugs, enn et spill som kjører korrekt, men har rotete kode med dårlig inndeling i klasser og manglende dokumentasjon!***

Dersom du har mangler eller bugs, eller dårlig organisert kode, vil du få trekk for det. Du kan minske poeng-trekk ved å beskrive mangler ved oppgaven i README-filen, og eventuelt hvorfor de er der/hvordan du *ville/burde* løst dem. Dette gjelder også designvalgene – hvis du oppdager for sent at du har gjort dumme valg vil du få mer uttelling dersom du forklarer erfaringen og hvordan du ville gjort det annerledes, selv om du ikke ikke har tid til å fikse implementasjonen.

**Like spill muliggjør kodegjenbruk.** Disse to spillene har en del fellestrekk selv om de også er forskjellige. Mye av koden deres kan derfor deles mellom dem. Du vil få mye poeng-uttelling dersom du finner gode løsninger for å gjenbruke kode mellom spillene. 

**Du står fritt til å gjenbruke kode fra alle tidligere lab-oppgaver, forelesningskode, og forige semesteroppgave.** Beskriv i [README.md](README.md) hvilken kode du henter fra hvor.

Du må gjerne diskutere oppgaven med andre, men dere må skrive individuell kode. Dersom du samarbeider tett med noen så beskriv det i README.md-filen. Se også om code review i [Tips og Triks](Tips.md#code-review-feedback-p%C3%A5-hverandres-kode)

**Ekstrapoeng.** Som på forige oppgave kan du få ekstrapoeng ved å implementere ekstra funksjonalitet. Dette kan inkludere fancy grafikk, super-smart AI, Facebook-integrasjon eller flere varianter av spillene. Flere forslag finner du i dokumentet [Advanced](Advanced.md)

**Hjelp - hvor starter jeg?** Se [Tips og Triks](Tips.md).

