<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>title</title>
    <style>
      table {
        
      }
      td {
        padding: 3px;
      }
      th {
        padding: 3px;
      }
      </style>
    
  </head>
  <body>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$db = "inf115_oblig1";
// Create connection
$conn = new mysqli($servername, $username, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Status: Connection failed: " . $conn->connect_error);
}
echo "Database status: Connected successfully.";

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
} else {
    echo "0 results";
}
$conn->close();
?>
  
  </body>
</html>