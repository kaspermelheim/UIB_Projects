<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_3</title>
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

  <h1>Tablenames from employees: </h1>

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
    $sql = "SHOW tables FROM employees";
    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                    echo $row['Tables_in_employees'] . "<br>";
            } 
    } 
    else {
            echo "Database is empty";
    }
    $conn->close();
  ?>
  
  </body>
</html>