<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>3_2</title>
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

  <h1>Number of employees in each department: </h1>

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
    $sql = "SELECT task1.dept_name, task1.name, task2.employees
            FROM (SELECT d.dept_no, d.dept_name, CONCAT(e.first_name, ' ', e.last_name) AS name
            FROM employees.departments AS d
            JOIN employees.dept_manager AS dm ON d.dept_no = dm.dept_no
            JOIN employees.employees  AS e ON dm.emp_no = e.emp_no
            GROUP BY dept_name) AS task1
            JOIN (SELECT COUNT(*) AS employees, dept_no
            FROM employees.dept_emp AS de
            GROUP BY dept_no) AS task2
            ON task1.dept_no = task2.dept_no";
    $result = $conn->query($sql);

    //Lager html table
    if ($result->num_rows > 0) {
        echo "<table border=3px>"; 
        echo "<tr> <th>Department</th><th>Manager</th><th>Number of employees</th></tr>";
        
        while($row = $result->fetch_assoc()) {
                echo "<tr><th>$row[dept_name]</th><th>$row[name]</th><th>$row[employees]</th></tr>";
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