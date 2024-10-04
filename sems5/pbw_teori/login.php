<?php
session_start();
require __DIR__ . '/src/model/db.php'; // Menghubungkan ke database
require __DIR__ . '/src/model/User.php'; // Menghubungkan kelas User
require __DIR__ . '/src/controller/AuthController.php'; // Menghubungkan kelas AuthController

// Inisialisasi objek User
$userModel = new User($pdo);
$authController = new AuthController($userModel);

// Inisialisasi variabel result untuk menghindari undefined variable
$result = ['success' => false, 'message' => '']; // Inisialisasi dengan nilai default

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'] ?? ''; // Ambil username
    $password = $_POST['password'] ?? ''; // Ambil password

    // Debug: Tampilkan username dan password yang diterima
    error_log("Username: $username, Password: $password");

    // Panggil fungsi login dari AuthController
    $result = $authController->login($username, $password);

    // Debug: Tampilkan hasil dari login
    error_log(print_r($result, true));

    if ($result['success']) {
        // Ambil data pengguna setelah login berhasil
        $user = $userModel->findByUsername($username);
        if ($user) {
            $userRole = $user['role']; // Ambil role pengguna
            if ($userRole === 'buyer') {
                header("Location: dashboard.php"); // Arahkan ke dashboard buyer
            } else if ($userRole === 'seller') {
                header("Location: dashboard_seller.php"); // Arahkan ke dashboard seller
            }
            exit; // Pastikan tidak ada kode yang dieksekusi setelah redirect
        }
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
    <form method="POST" action="">
        <label>Username: </label>
        <input type="text" name="username" required><br><br>
        <label>Password: </label>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>

</html>