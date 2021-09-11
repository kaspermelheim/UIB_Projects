<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>4</title>
    <style>
      table {  
      }
      td {
        padding: 3px;
      }
      th {
        padding: 3px;
      }
      #blue {
          color: blue;
      }
      #div {
          background-color: lightblue;
          padding: 10px;
          width: 300px;
      }
      </style>
  </head>
  <body>

<div id="div">
  <form action="4.php" method="GET">
    <h1>Salary (Yearly):</h1>

    Choose Year: <select name="select">
     
    <?php
        $servername = "localhost";
        //Standard username og pass
        $username = "root";
        $password = "";
        $db = "employees";

        //Oppretter connection
        $conn = new mysqli($servername, $username, $password, $db);

        //sql spørring
        $sql = 'SELECT MIN(year(from_date)) AS from_date
        FROM employees.salaries';

        $result = $conn->query($sql);
        $startYear = $result->fetch_assoc();
        $startYear = $startYear["from_date"];

        if($result->num_rows > 0){
            for($x = 0; $x < (date("Y") - $startYear+1); $x++){
                $year = (date("Y")-$x);
                echo "<option value='$year'>" . $year . "</option>";
            }
        }

        $conn->close();

    ?>
    </select>
    Average<input type="radio" name="input" value="average">
    Total<input type="radio" name="input" value="sum">
    <br>
    <input type="submit" value="Select">
</form>

<?php
    $servername = "localhost";
    //Standard username og pass
    $username = "root";
    $password = "";
    $db = "employees";

    //Oppretter connection
    $conn = new mysqli($servername, $username, $password, $db);
    
    $year = isset($_GET["select"]) ? $_GET["select"] : date("Y");
    $radio = isset($_GET["input"]) ? $_GET["input"] : null;

    //sql spørring bestemt av radio buttons
    if($radio == "average"){
        $sql="SELECT AVG(salary) AS salary
        FROM employees.salaries
        WHERE year(from_date) <= $year AND $year < year(to_date)";
    }
    else if($radio == "sum"){
        $sql="SELECT SUM(salary) AS salary
        FROM employees.salaries
        WHERE year(from_date) <= $year AND $year < year(to_date)";
    }


    if($radio != null){
        $result = $conn->query($sql);
        $salary = $result->fetch_assoc();
        
        if($radio == "average"){
            echo("Average salary of $year : " . $salary['salary'] . " USD");
        }
        else if($radio == "sum"){
            echo("Total salary of $year : " . $salary['salary'] . " USD");
        }
    }
    else{
        echo("<p id='blue'>Choose one of the options</p>");
    }
        $conn->close();
    ?>
  </div>
  </body>
</html>