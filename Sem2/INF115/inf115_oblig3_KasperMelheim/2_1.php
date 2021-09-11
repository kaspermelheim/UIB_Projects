<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_1</title>
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

  <h1>Database from MariaDB: </h1>

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
    $sql = "SELECT first_name, last_name FROM employees ORDER BY last_name ASC";
    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
            echo "<table id='phptable' border=3px>"; 
            echo "<tr> <th>first_name</th><th>last_name</th></tr>";
            while($row = $result->fetch_assoc()) {
                    echo "<tr><td>" . $row['first_name'] . "</td><td>" . $row['last_name'] . "</td></tr>";
            }
                    echo "</table>"; 
    } 
    else {
            echo "Table is empty";
    }
    $conn->close();
?>
  
  </body>
</html>