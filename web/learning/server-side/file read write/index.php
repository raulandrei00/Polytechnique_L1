<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> CSC_1S004 </title>
</head>

<body>

    <?php
    // Read current file content
    $f = file_get_contents("info.txt");

    // Increment value
    $f = $f+1;

    // Store updated value in file
    file_put_contents("info.txt",$f);

    // Display current value
    print "This page has been viewed $f times";
    ?>

</body>

</html>
