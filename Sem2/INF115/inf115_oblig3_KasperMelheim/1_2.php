<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>1_2</title>
    <style>
      table {
        
      }
      td {
        padding: 3px;
      }
      th {
        padding: 3px;
      }
      .error {
          color: red;
      }
      </style>
    
  </head>
  <body>

  <h1>Log in: </h1>

<p>
    <span class="error">* must fill in</span>
</p>

<?php

$nameErr = $yearErr = $ageErr = "";
$name = $year = $age = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Fill in name.";
  } else {
    $name = isFilled($_POST["name"]);
  }
  
  if (empty($_POST["year"])) {
    $yearErr = "Fill in year of birth.";
  } else {
    $year = isFilled($_POST["year"]);
  }
    
  if (empty($_POST["age"])) {
    $ageErr = "Fill in current age.";
  } else {
    $age = isFilled($_POST["age"]);
  }


if (is_numeric($_POST["year"]) && is_numeric($_POST["age"])) {
   
    if($_POST["year"] + $_POST["age"] == date("Y")) {
        echo 'Input age and year is corresponding with the current year.';
        echo '<br>';
        }
        else {
        echo 'Input age and year is not corresponding with the current year.';
        echo '<br';
    }

  } else {
    echo '';
  }
}

function isFilled($info) {
    $info = trim($info);
    $info = stripslashes($info);
    $info = htmlspecialchars($info);
    return $info;
  }
?>


<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
    Name: <input type="text" name="name">
    <span class="error">* <?php echo $nameErr;?></span>
    <br><br>
    Year-of-birth: <input type="text" name="year" >
    <span class="error">* <?php echo $yearErr;?></span>
    <br><br>
    Age: <input type="text" name="age">
    <span class="error">*<?php echo $ageErr;?></span>
    
    <br><br>
    <input type="submit" name="submit" value="Submit">  
    <input type="reset" value="Reset" name="reset" />
</form>

<?php
    echo "<h2>Info:</h2>";
    echo $name;
    echo "<br>";
    echo $year;
    echo "<br>";
    echo $age;
    
?>
  
  </body>
</html>