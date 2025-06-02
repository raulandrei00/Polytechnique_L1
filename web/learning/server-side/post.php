<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> CSC_1S004 </title>
</head>

<body>

    <h1> HTML Form </h1>

    <form method="post">
    Name: <input type="text" name="Name"> <br>
    Surname: <input type="text" name="Surname"> <br>
    <input type="submit" value="Submit">
    </form>


    <?php
    if( !empty($_POST['Name']) && !empty($_POST['Surname']) ){
        $name = $_POST['Name'];
        $surname = $_POST['Surname'];
        print "<p>Hello $name $surname</p>";
    }
    ?>

</body>

</html>
