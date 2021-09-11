<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>1_3</title>
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

  <h1>Choose preferred language: </h1>

  <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <input type="radio" name="language" value="english">English
    <input type="radio" name="language" value="norwegian">Norwegian

    <br><br>
    <input type="submit" name="submit" value="Choose"> 
  </form>
  <?php

$language = "";
$form = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if ($_POST["language"] == "english") {
    echo '<br><br>Name: <input type="text" name="name">
    <br><br>
    Year-of-birth: <input type="text" name="year" >
  
    <br><br>
    Age: <input type="text" name="age">
    
    <br><br>
    <input type="submit" name="submit" value="Submit">  
    <input type="reset" value="Reset" name="reset" />';
  }
  if($_POST["language"] == "norwegian") {
    echo '<br><br>Navn: <input type="text" name="name">
    <br><br>
    Fødelsår: <input type="text" name="year" >
  
    <br><br>
    Alder: <input type="text" name="age">
    
    <br><br>
    <input type="submit" name="submit" value="Send">  
    <input type="reset" value="Fjern" name="reset" />';
  }
}


?>

  

  
<?php
echo "<br>";
echo $form;
?>

  
  </body>
</html>