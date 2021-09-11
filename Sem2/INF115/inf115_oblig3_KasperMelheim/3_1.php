<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>3_1</title>
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

  <h1>Tablenames and their attributes: </h1>

  </form>
    <?php
    $servername = "localhost";
    //Standard username og pass
    $username = "root";
    $password = "";
    
    $db = "employees";

    //Oppretter connection
    $conn = new mysqli($servername, $username, $password, $db);
    ?>

    <?php
    
    //sql spørring
    $sql = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'employees' ";
    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
        echo "<table border=3px>"; 
        echo "<tr> <th>Table</th><th>Attributes</th></tr>";
        
        while($row = $result->fetch_assoc()) {
                echo "<tr><th>$row[TABLE_NAME]</th><th>$row[COLUMN_NAME]</th></tr>";
        }
                echo "</table>"; //Close the table in HTML
    } 
    else {
            echo "Table is empty";
    }
    $conn->close();
?>
  
  </body>
</html>