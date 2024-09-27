<?php
session_start();
include 'src/model/db.php';

// Cek apakah pengguna sudah login
if (isset($_SESSION['user_id'])) {
    if ($_SESSION['role'] === 'seller') {
        header('Location: dashboard_seller.php');
    } else {
        header('Location: dashboard.php');
    }
    exit;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if (!empty($username) && !empty($password)) {
        // Menyiapkan query untuk mengambil data pengguna berdasarkan username
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch();

        // Memeriksa apakah pengguna ada dan password cocok
        if ($user && $password == $user['password']) {
            $_SESSION['user_id'] = $user['user_id'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['role'] = $user['role'];

            // Arahkan ke dashboard sesuai role
            if ($user['role'] === 'seller') {
                header('Location: dashboard_seller.php');
            } else {
                header('Location: dashboard.php');
            }
            exit;
        } else {
            $error = "Username atau password salah.";
        }
    } else {
        $error = "Username dan password harus diisi.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>

<body>
    <h2>Login</h2>
    <?php if (isset($error)) {
        echo "<p style='color:red;'>$error</p>";
    } ?>
    <form method="POST" action="">
        <label>Username: </label>
        <input type="text" name="username" required><br><br>
        <label>Password: </label>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
        <button type="submit"><a href="/">Kembali ke dashboard</a></button>
    </form>

</body>

</html>