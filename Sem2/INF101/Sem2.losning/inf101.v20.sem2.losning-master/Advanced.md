## Advanced

* [README](README.md) – for utfyllingface
* [Oppgavetekst](SEM-2.md)
* [Tips for å komme i gang](Tips.md)
* **Advanced**

## Hvordan oppnå ekstrapoeng
*Her gir vi noen forslag til hvordan du kan oppnå ekstrapoeng. Du kan også finne på egne ideer: bare beskriv dem klart i README-filen.*

## GUI
Grafisk brukergrensesnitt gir ekstrapoeng. Vi vet at det er vanskelig å skrive GUI, så vi har inkludert litt eksempelkode. **Du trenger ikke bruke eksempel-koden.** 

Syns du det ble veldig 90-talls? Gjør det bedre da vel! Hvis du klarer å gi gruppelederen som retter en behagelig brukeropplevelse så motiverer det desto mer til ekstrapoeng. *Bribe the DM*, as we say in DnD. 

Hvis du trenger hjelp til å komme i gang med GUI kan du kikke på:

* ...grafikkbiblioteket vi har brukt i INF101, f.eks. fra [Semesteroppgave 1](https://retting.ii.uib.no/inf101.v20.oppgaver/inf101.v20.sem1/-/tree/master/src%2Fmain%2Fjava%2Finf101%2Fv20%2Fgfx). 
* ...kopiere grid-GUIen fra [lab 3/4](https://retting.ii.uib.no/inf101.v20.oppgaver/inf101.v20.lab4.losning).
* Web-integrasjon? Kanskje litt beyond INF101, men vi blir veldig imponert hvis du får det til. 

### Grafikk-modul 
Hvis du vil sjekke om du har klart å skille koden for brukergrensesnittet klart fra resten (vi kaller det "modulær" kode) så kan du prøve å bytte ut brukergrensesnittet ditt med noen annens: dersom du har et fornuftig API til resten av programmet ditt bør det være relativt enkelt å koble noen andres brukergrensesnitt til resten av koden din, og på den måten endre én del av programmet uten å måtte endre kode som ikke har med input/output å gjøre. Du kan nok ikke bytte ut klassene direkte, men det bør gå an med litt jobb, og hvis dere blir enig om en lur måte å skrive interfacene på som dere har felles, kan dere bytte moduler uten å endre øvrig kode. 

*Det er ikke et krav for oppgaven å bytte kode med andre studenter, men hvis du får det til uten særlig mye arbeid ligger du sannsynligvis godt an.* 

## Code Review / Feedback på hverandres kode

*Dette er frivillig, men kan være både lærerikt og hjelpe deg til å forbedre innleveringen din.*

Det er veldig nyttig å måtte [forklare](https://en.wikipedia.org/wiki/Rubber_duck_debugging) hvordan man selv har tenkt og hvordan ens egen kode virker, og det er også veldig nyttig å prøve å sette seg inn i hvordan andre har tenkt når de har programmert. Vi anbefaler derfor at du finner går sammen med noen andre studenter (f.eks. i grupper på 2–4 personer) og gjør litt [lightweight](http://codingsight.com/lightweight-code-review/) [code reviews](https://en.wikipedia.org/wiki/Software_peer_review) av hverandres kode:

* Det er praktisk å gå gjennom ting muntlig: sitt rundt samme datamaskin, og forklar din egen kode til de andre (eller prøv å forstå og forklare noen andres kode!) – dere kan diskutere gode og dårlige løsninger, ideer til ting som kan gjøres annerledes eller forbedres osv.
* **Viktig:** poenget med dette er *å lære*, og *å forbedre* innleveringene – for at det skal funke er det viktig å være *positiv og konstruktiv* når du gir tilbakemeldinger eller kommentarer (ellers er det ingen som tør å vise deg koden sin neste gang!)
* Det burde passe greit å gjøre dette en gang i løpet av den første uken, og så en gang til noen dager før innlevering. 
* Det er et eget punkt i [README-filen](README.md) som dere kan krysse av hvis dere prøver dere på en eller annen variant av “code review” – skrive gjerne også noen setninger om hva dere gjorde og hvordan det fungerte (lærte du noe? forbedret du noe?)


### Random Events
To mix things up a litte, the implementation can support the functionality of random events: These events are executed in each round with a certain probability and change the state of the game. Examples are the following (but it can be anything fun, be creative!):

-  Throwing 'blocker' tokens into a random column that keep both players to throw their tokens there.
-  Looking at each token in the board and switching its owner with a certain probability. (I.e. some of the blue tokens become red and vice versa.)
-  Switching the owners of tokens in a random (small) area of the board.
-  Rotating the board.
-  ...


### Modulært 
Dersom du skriver programmet ditt modulært, er det lett å koble dine moduler sammen med andres og på den måten f.eks. bytte ut ditt brukergrensesnitt med noen andre sitt, eller koble noen andre sin AI til ditt spill. For å få dette til må du ha god enkapsulering, fornuftig navngiving og forståelig dokumentasjon. Husk at tester er en del av dokumentasjonen. 

For å få programmet modulært må det bestå av flere komponenter eller deler, der hver del implementeres separat fra kjerneprogrammet. Dette betyr ikke at dere trenger forskjellige prosjekter, men at kode-komponenter er klart adskilte (funksjonalitet for AI skal være begrenset til AI-modulen og ikke "lekke" inn i I/O-modulen. Spillets funksjonalitet og regler må ikke påvirkes av at man bytter ut modulen for I/O, osv. 

Siden vi ikke har gitt dere noen interface eller API å følge, er det usannsynlig at du har nøyaktig samme APIer som andre studenter. Derfor må dere nok jobbe litt for å koble modulene deres sammen. En måte å gjøre det på, er å skrive en "koblings-klasse" som oversetter mellom interfacene deres. Den må dere gjerne skrive sammen. Dette blir altså en ny klasse, som ikke finnes i noen av programmene fra før, og som har som jobb å "oversette" mellom forskjellige APIer. Det gjør at dere slipper å endre deres egen kode. 

Eventuelt kan dere bli enige om et felles interface, en *standard*, og følge denne begge to. 

Dersom du samarbeider med noen for å få dette til, skriv i README-filen hvem og hvordan. 

### Bedre AI 
AI-spillerene kan gjøres smartere på mange måter. Du kan finne på dine egene strategier, f.eks. ved å ha en egen klasse for Strategi, og la AI-spillere velge hvilken de skal bruke, eller til og med bytte underveis. Begge spillene lar seg 'løse': Det vil si at det går an å lage en perfekt AI-spiller. 

Hvis du gjør modul-delen over kan du la din AI-spiller konkurrere mot andres. 


### Ultimate Tic Tac Toe 
Let's be real - Tic Tac Toe er nokså kjedelig å spille for de fleste av oss. Vi er selvfølgelig stole av deg og koden din, men det er usannsylig at spillet ditt slår an blant folk over 8 år. Hvis du vil lage en variant som er mer utfordrende for oss voksne foreslår vi Tic Tac Toe Ultimate. 

Forklaring og regler her: [https://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/](https://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/)

Eksempel-spill her: [http://bejofo.net/ttt](http://bejofo.net/ttt )