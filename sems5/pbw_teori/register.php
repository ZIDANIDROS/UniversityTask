<?php
include 'src/model/db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Cek apakah username dan password tidak kosong
    if (!empty($username) && !empty($password)) {
        // Hash password sebelum disimpan
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Simpan ke database
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        try {
            $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
            echo "Registrasi berhasil!";
        } catch (PDOException $e) {
            // Handle jika username sudah ada atau error lain
            if ($e->getCode() == 23000) {
                echo "Username sudah ada!";
            } else {
                echo "Terjadi kesalahan: " . $e->getMessage();
            }
        }
    } else {
        echo "Username dan password harus diisi.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>

<body>
    <h2>Register Pengguna Baru</h2>
    <form method="POST" action="">
        <label>Username: </label>
        <input type="text" name="username"><br><br>
        <label>Password: </label>
        <input type="password" name="password"><br><br>
        <button type="submit">Register</button>
    </form>
</body>

</html>