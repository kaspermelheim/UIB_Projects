# [Semesteroppgave 2: Fire på rad og Tripp-trapp-tresko]


* **README**
* [Oppgavetekst](SEM-2.md)
* [Tips for å komme i gang](Tips.md)
* [Advanced](Advanced.md)

**Innleveringsfrist:** Hele oppgaven skal være ferdig og levert via din private gitlab-repositorie til **Fredag 24. april kl. 2359** ([AoE](https://www.timeanddate.com/worldclock/fixedtime.html?msg=4&iso=20180427T2359&p1=3399)).  

### Innlevering 
 Du finner koden din i repositoriet med URIen:

    https://retting.ii.uib.no/<brukernavn>/inf101.v20.sem2.git

Oppgaven leveres inn ved å pushe til retting.ii.uib.no, [slik du har gjort med alle tidligere INF101-oppgaver](https://retting.ii.uib.no/inf101/inf101.v20/wikis/hente-levere-oppgaver). Husk å få med eventuelle nye filer du har opprettet.

**VIKTIG:** *Sjekk kvitteringssiden som kommer opp når du pusher, i tilfelle det skjer feil!* 

Vi anbefaler at du gjør commit hver dag, eller hver gang du er ferdig med en
deloppgave, i tilfelle du mister det du jobber med på din egen maskin. Du kan levere inn så mye og ofte du vil. Versjonen som teller er den **siste du pushet før innleveringsfristen**.

Denne oppgaven teller på din endelige vurdering i faget. Maks poeng er 100. Du kan få opp til 120 totalt, inkludert ekstrapoeng. 

# Fyll inn egne svar/beskrivelse/kommentarer til prosjektet under
* Levert av:   Martin vatshelle (mva021)
* [X] hele semesteroppgaven er ferdig og klar til retting!
* Code review:
   * [ ] jeg har fått tilbakemelding underveis fra @brukernavn, ...
   * [X] jeg har gitt tilbakemelding underveis til @Lang liste av studenter, ...
* Sjekkliste:
   * [X] Kjørbart Fire på Rad-spill
	   * [X] Funksjonelt spill 
	   * [X] Fungerende user interface
	   * [X] Støtter AI 
   * [X] Kjørbart Tripp-trapp-tresko-spill
	   * [X] Funksjonelt spill 
	   * [X] Fungerende user interface
	   * [X] Støtter AI 
   * [X] Forklart designvalg, hvordan koden er organisert, abstraksjon, og andre ting 
   * [X] Tester
   * [X] Dokumentasjon (JavaDoc, kommentarer, diagrammer, README, etc.)
   * [X] Fornuftige navn på klasser, interfaces, metoder og variabler
   * [X] Fornuftige abstraksjoner og innkapsling (bruk av klasser, interface, metoder, etc.)

## Oversikt
Denne Koden er et Løsningsforslag til Semesteroppgave 2 i INF 101 våren 2020.

Løsningsforslaget gjør litt mer enn det som er spurt etter i oppgaveteksten og mer enn det som krves for å få 100%.
Noen av dere har laget en løsning med input fra terminal mens andre har laget en løsning med GUI. Dette løsningsforslaget har laget begge deler. En ekstra fordel med denne løsningen er at 2 AI spillere kan spille mot hverandre noe som gjør at man får testet AI mye bedre enn ellers.

En klassediagram over klassene i dette løsningsforslaget finner dere på Mitt UiB, her er en kort liste

Grid, Location, GridDirection og GridLocationIterator 
- er en litt annen versjon av Grid enn den som ble delt ut med oppgaveteksten. Men den er basert på det som ble brukt i Semesteroppgave 1.

GameBoard 
- er en klasse som arver fra Grid<Player>. Hovedformålet med denne klassen er å holde styr på hvor de forskjellige spillerene har plasert, skrive ut brettet til skjemen og telle hvor mange på rad spillerene har oppnådd.

Player, AbstractPlayer, GuiPlayer, ConsolePlayer, MiniMaxPlayer og RandomPlayer 
- er klasser for forskjellige typer Player. Player er et Interface og AbstractPlayer er en klasse som har det som er felles for alle de andre Player typene. GuiPlayer og ConsolePlayer er klasser for å personer som spiller ved å gi input. MiniMaxPlayer og RandomPlayer er 2 AIer av forskjellig "intelligens". Alle disse Spillerene kan brukes på begge spillene (og potensielt flere spill i fremtiden).

PlayerList 
- er en enkel klasse som holder styr på 2 spillere, hvem som starter spillet, hvem sin tur det er nå og hvem sin tur det er neste gang.
Denne er laget såpass generell at den kan takle flere enn 2 spillere og at den kan fjerne spillere underveis. Man trenger ikke lage denne klassen så generell.

IGame, AbstractGame, TicTacToe og ConnectFour
- er klasser som holder styr på reglene i spillet og driver spillet fremover. Spillet drives fremover ved en løkke som kaller Player sin getMove() metode. Untaket er GuiPlayer der spillet stoppes og det ventes på innput fra GUIen før spillet startes opp igjen.
Hovedmetodene i disse klassene er isWinner(Player p) of canPlace(Location loc, Player p).

GamePanel, ClickableGrid, MNKGameGUI og GameGUI
- er klasser for å håndtere GUI interfacet. Jeg har gjort en del endringer i forhold til den eksempel GUI koden som ble gitt ut med oppgaven, men mye er det samme fortsatt.

### Bruk
For å starte programmet kjør: 
Spillet kan enten startes ved å kjøre main metoden i TerminalMenu hvis du vil spille den text baserte versjonen, eller main metoden i GameGUI hvis du vil spille den GUI baserte versjonen.

## Designvalg
Klassen AbstractGame har blitt en sentral klasse i spillet som har en game loop som driver spillet fremover.
Jeg har valgt å Bruke samme GameLoop til å drive spillet uansett om det er GUI eller Terminal som brukes til input, dette gjorde at AbstractGame og IGame ble noe større enn de hadde trengt å være, skulle gjerne delt opp AbstractGame i 2 klasser.

En av de viktigste valgene jeg gjorde var at Player fikk metoden getMove(IGame game). Dette la føringer på mye av designet som jeg endte opp med. Alle Player klassene er dermed i stand til å spille begge spillene.

Spillbrettet modelerte jeg som Grid<Player> og ungikk dermed noe av problematikken med forskjellige typer brikker, hvis dette spillet skulle utvides til noe mer generellt f.eks. Sjakk så måtte jeg ha hatt en egen klasse for Player,Piece kombinasjoner 

### Bruk av abstraksjon
Jeg har delt spillet opp i 3 deler, Spillere, Spillbrett og regler.
- 4 typer spillere implementerer et felles Interface Player.
- Spillbrettet er representert ved GameBoard
- Reglene som er felles for de to spillene er implementert i AbstractGame. De reglene som er forskjellig fanges opp av metodene canPlace() og isWinner() som er implementert forskjellig i TicTacToe or ConnectFour

### Erfaring – hvilke valg viste seg å være gode / dårlige?
Å ha getMove() som returnerer en Location har vært et godt valg.
Var veldig fornøyd med at samme MiniMax player kan spille begge spillene.

Det var Praktisk å modellere GameBoard som Grid<Player> men jeg ser at dette begrenser litt hvordan jeg kan utvide spillet i fremtiden.

Jeg måtte lage en metode stop() i AbstractGame for å stoppe spillet å vente på input fra en GUI player. Jeg ville ikke lage denne metoden public for da kunne andre spillere stoppe spillet før det var slutt så inne i GameLoopen må jeg sjekke for instanceOf GuiPlayer som ikke føltes som fin kode.

Klassen ClickableGrid ble veldig bra, virket som en grei måte å gjøre om fra museklikk til til Location

## Testing
Jeg har skrevet JUnit tester for spill logikken. GUI klassene og Terminal klassene er ikke testet.
Det er totalt 65 tester.

Måten jeg har laget spillet på gjør at 2 AI spillere kan spille mot hverandre. Det gjorde at jeg f.eks. kunne lage tester som verifiserte at AI spilleren var smartere enn en RandomPlayer.

Jeg oppdaget flere bugs mens jeg laget spillet, da skrev jeg tester for å se at jeg hadde laget tester som failet for denne bugen og så fikset jeg bugen og så at testen passerte, jeg tror denne måten å jobbe på førte til ganske god dekning på testene.

## Funksjonalitet, bugs
Så vidt jeg vet fungerer spillet som det skal.
Når spillet er over og man trykker på en av knappene så starter spillet på nytt, men det tar ikke vare på brukervalgene fra forrige spill.
Så du må skrive inn navn på nytt. Men man får den fordelen at man kan bytte fra AI til Multiplayer mellom spillene. Dette er en feature jeg kunne forbedret

## Evt. erfaring fra code review
Jeg ble inspirert av at flere studenter har prøvd seg på å implementere en MiniMax algoritme for AIen. Dette passer nok bedre inn i INF102 pensum men jeg legger likevel med en AI inspirert av disse MiniMax implementasjonene i denne løsningen.



## Annet
Jeg begynte å implementere en enkel løsning først før jeg tok meg tid til å tegne klassediagrammet. Jeg burde nok tegnet klassediagrammet tidligere.