<?php
session_start();

$_SESSION = [];
session_destroy();
header('Location: ../../'); // Perhatikan jalur relatif
exit;
