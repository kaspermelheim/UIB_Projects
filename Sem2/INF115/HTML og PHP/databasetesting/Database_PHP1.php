<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="no">
    <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Database_HTML</title>
            <link rel="stylesheet" href="Database_HTMLstil.css">

    </head>
    <body>
            <header>
                    <div id="headerdiv">
                        <h1>Database til HTML</h1>
                        <p>Hente ut database fra mariaDB (sql) og bruke php for å presentere i HTML</p>
                    </div>
            </header>
            <div id="main">
                    <div id="d1">
                        <h2>Database i mariaDB</h2>
                        
                                <p>Vi får tilgang til mariaDB ved hjelp av XAMPP. Dette programmet hjelper oss å hoste en server lokalt på datamaskinen vår.
                                Ved å skrive inn localhost i en nettleser får vi tilgang til den nettlesererbaserte applikasjonen.<br><br> Inne i phpmyadmin (mariaDB) kan vi 
                                opprette en database. Denne kan vi fylle med columns og rows, og sette inn data i disse. På denne nettsida henter vi ut endatabase
                                fra mariaDB og presenterer den oversiktelig på et brukervennlig format.
                                </p>
                                <div id="imgdiv">
                                        <img id="mainimg" src="mariaDB.png" alt="Skjermdump fra mariaDB">
                                        <p>Skjermdump fra mariaDB av en database som inneholder 4 tabeller,
                                                alle fyllt med forskjellig data.
                                        </p>
                                </div>

                        <h3>Database hentet fra mariaDB - Oblig1 eksempel</h3>
                        <p>Viser fram de 4 tabellene vi brukte i oblig1 i emnet INF115, Codons, Nucleotides, Amino_acid_properties og Amino_acid_nomenclature.</p>
                        <br>
                        <p style="text-decoration: underline">Tabell Codons:</p>
                                
                        <?php
                                $servername = "localhost";
                                $username = "root";
                                $password = "";
                                $db = "inf115_oblig1";
                                // Create connection
                                $conn = new mysqli($servername, $username, $password, $db);
                                ?>

                                <?php
                                // Check connection
                                if ($conn->connect_error) {
                                        die("<br>Database status: Connection failed: " . $conn->connect_error);
                                }
                                echo "<p id='statusok'> Database status: Connected successfully.</p>";

                                $sql = "SELECT Codon_id, Codon_Sequence, Position1, Position2, Position3, Amino_acid_id FROM Codons GROUP BY Amino_acid_id";
                                $result = $conn->query($sql);

                                if ($result->num_rows > 0) {
                                        echo "<table border=3px>"; // start a table tag in the HTML
                                        echo "<tr> <th>Codon_id</th><th>Codon_Sequence</th><th>Position1</th><th>Position2</th><th>Position3</th><th>Amino_acid_id</th></tr>";
                                        // output data of each row
                                        while($row = $result->fetch_assoc()) {
                                                echo "<tr><td>" . $row['Codon_id'] . "</td><td>" . $row['Codon_Sequence'] . "</td><td>" . $row['Position1'] . "</td>
                                                <td>" . $row['Position2'] . "</td><td>" . $row['Position3'] . "</td><td>" . $row['Amino_acid_id'] . "</td></tr>";  //$row['index'] the index here is a field name
                                        }
                                                echo "</table>"; //Close the table in HTML
                                } 
                                else {
                                        echo "0 results";
                                }
                                $conn->close();
                        ?>

                        <br>
                        <p style="text-decoration: underline">Tabell Nucleotides:</p>

                        <?php
                                $servername = "localhost";
                                $username = "root";
                                $password = "";
                                $db = "inf115_oblig1";
                                // Create connection
                                $conn = new mysqli($servername, $username, $password, $db);

                                // Check connection
                                if ($conn->connect_error) {
                                        die("<br>Database status: Connection failed: " . $conn->connect_error);
                                }
                                echo "<p id='statusok'> Database status: Connected successfully.</p>";

                                $sql = "SELECT Symbol, Name, Type FROM Nucleotides";
                                $result = $conn->query($sql);

                                if ($result->num_rows > 0) {
                                        echo "<table border=3px>"; // start a table tag in the HTML
                                        echo "<tr> <th>Symbol</th><th>Name</th><th>Type</th></tr>";
                                        // output data of each row
                                        while($row = $result->fetch_assoc()) {
                                                echo "<tr><td>" . $row['Symbol'] . "</td><td>" . $row['Name'] . "</td><td>" . $row['Type'] . "</td></tr>";  //$row['index'] the index here is a field name
                                        }
                                                echo "</table>"; //Close the table in HTML
                                } 
                                else {
                                        echo "0 results";
                                }
                                $conn->close();
                        ?>

                        <br>
                        <p style="text-decoration: underline">Tabell Amino_acid_nomenclature:</p>

                        <?php
                                $servername = "localhost";
                                $username = "root";
                                $password = "";
                                $db = "inf115_oblig1";
                                // Create connection
                                $conn = new mysqli($servername, $username, $password, $db);
                                
                                // Check connection
                                if ($conn->connect_error) {
                                        die("<br>Database status: Connection failed: " . $conn->connect_error);
                                }
                                echo "<p id='statusok'> Database status: Connected successfully.</p>";

                                $sql = "SELECT Name, Molecular_mass, Polarity, Charge FROM Amino_acid_properties";
                                $result = $conn->query($sql);

                                if ($result->num_rows > 0) {
                                        echo "<table border=3px>"; // start a table tag in the HTML
                                        echo "<tr> <th>Name</th><th>Molecular_mass</th><th>Polarity</th><th>Charge</th></tr>";
                                        // output data of each row
                                        while($row = $result->fetch_assoc()) {
                                                echo "<tr><td>" . $row['Name'] . "</td><td>" . $row['Molecular_mass'] . "</td><td>" . $row['Polarity'] . "</td>
                                                <td>" . $row['Charge'] . "</td></tr>";  //$row['index'] the index here is a field name
                                        }
                                                echo "</table>"; //Close the table in HTML
                                } 
                                else {
                                        echo "0 results";
                                }
                                $conn->close();
                        ?>

                        <br>
                        <p style="text-decoration: underline">Tabell Amino_acid_properties:</p>

                        <?php
                                $servername = "localhost";
                                $username = "root";
                                $password = "";
                                $db = "inf115_oblig1";
                                // Create connection
                                $conn = new mysqli($servername, $username, $password, $db);
                                
                                // Check connection
                                if ($conn->connect_error) {
                                        die("<br><p id='statusfailed'>Database status: Connection failed: </p>" . $conn->connect_error);
                                }
                                echo "<p id='statusok'> Database status: Connected successfully.</p>";

                                $sql = "SELECT Amino_id, Symbol, Name, Code FROM Amino_acid_nomenclature";
                                $result = $conn->query($sql);

                                if ($result->num_rows > 0) {
                                        echo "<table border=3px>"; // start a table tag in the HTML
                                        echo "<tr> <th>Amino_id</th><th>Symbol</th><th>Name</th><th>Code</th></tr>";
                                        // output data of each row
                                        while($row = $result->fetch_assoc()) {
                                                echo "<tr><td>" . $row['Amino_id'] . "</td><td>" . $row['Symbol'] . "</td><td>" . $row['Name'] . "</td>
                                                <td>" . $row['Code'] . "</td></tr>";  //$row['index'] the index here is a field name
                                        }
                                                echo "</table>"; //Close the table in HTML
                                } 
                                else {
                                        echo "0 results";
                                }
                                $conn->close();
                        ?>
                    </div>


            </div>

            <footer>
                    <div id="footerdiv">
                            <p>Made by Kasper Melheim.<br>
                                Languages used: PHP, HTML and SQL.
                            </p>
                    </div>
            </footer>
    </body>
</html>
