<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_2</title>
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
    $sql = "SELECT DISTINCT title FROM titles";
    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
            echo "<table border=3px>"; 
            echo "<tr> <th>title</th></tr>";
            while($row = $result->fetch_assoc()) {
                    echo "<tr><td>" . $row['title'] . "</td></tr>";
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