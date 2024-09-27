<?php
require_once 'controllers/GuestController.php';

$guestController = new GuestController();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $comment = $_POST['comment'];
    $guestController->create($name, $comment);
    header("Location: index.php");
}

$guests = $guestController->readAll();
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Perbaikan pada href untuk file CSS -->
    <link rel="stylesheet" type="text/css" href="views/css/style.css" />
  </head>

  <body>
    <?php include 'views/guest_form.php'; ?>
    <?php include 'views/guest_list.php'; ?>
  </body>
</html>
