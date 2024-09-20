<?php

include 'koneksi.php';

if (isset($_POST['submit'])) {
    $nama = $_POST['nama'];
    $email = $_POST['email'];
    $komentar = $_POST['komentar'];

    $sql = "INSERT INTO tamu (nama, email, komentar) VALUES (:nama, :email, :komentar)";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':nama', $nama);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':komentar', $komentar);

    if ($stmt->execute()) {
        echo "<p>Terima kasih, data Anda telah disimpan!</p>";
    } else {
        echo "<p>Error: " . $stmt->errorInfo()[2] . "</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Buku Tamu</title>
</head>

<body>
    <h1>Isi Buku Tamu</h1>

    <form method="post" action="input.php">
        <label for="nama">Nama:</label><br>
        <input type="text" id="nama" name="nama" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="komentar">Komentar:</label><br>
        <textarea id="komentar" name="komentar" required></textarea><br><br>

        <input type="submit" name="submit" value="Kirim">
    </form>

    <p><a href="index.php">Kembali ke Landing Page</a></p>
</body>

</html>