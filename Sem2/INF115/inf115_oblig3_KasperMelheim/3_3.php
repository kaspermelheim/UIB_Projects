<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>3_3</title>
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

  <h1>Number of male and female born in each year: </h1>

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
    $sql = 'SELECT M_query.b_date, M_query.num_male, F_query.num_female
            FROM (SELECT year(birth_date) AS b_date, COUNT(*) AS num_male
            FROM employees.employees
            WHERE gender = "M"
            GROUP BY b_date) AS M_query
            INNER JOIN (SELECT year(birth_date) AS b_date, COUNT(*) AS num_female
            FROM employees.employees
            WHERE gender = "F"
            GROUP BY b_date) AS F_query
            ON M_query.b_date = F_query.b_date';

    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
        echo "<table border=3px>"; 
        echo "<tr> <th>Year</th><th>Male</th><th>Female</th></tr>";
        
        while($row = $result->fetch_assoc()) {
                echo "<tr><th>$row[b_date]</th><th>$row[num_male]</th><th>$row[num_female]</th></tr>";
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