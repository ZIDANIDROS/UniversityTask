<?php
session_start();
include 'src/model/db.php'; // Pastikan ini mengarah ke file koneksi yang benar

// Periksa apakah pengguna sudah login
if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit;
}

// Ambil ID pengguna dari session
$user_id = $_SESSION['user_id'];

// Proses form penjualan jika disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $judul = $_POST['judul'];
    $harga = $_POST['harga'];

    // Masukkan buku baru ke dalam tabel books
    $stmt = $pdo->prepare("INSERT INTO books (judul, harga, pemilik, status) VALUES (:judul, :harga, :pemilik, 'available')");
    $stmt->execute([
        'judul' => $judul,
        'harga' => $harga,
        'pemilik' => $user_id // Menyimpan pemilik buku sesuai ID pengguna yang login
    ]);

    header('Location: dashboard_seller.php'); // Refresh halaman setelah penambahan
    exit;
}

// Ambil daftar buku yang dijual oleh pengguna berdasarkan ID pengguna yang login
$stmt = $pdo->prepare("SELECT * FROM books WHERE pemilik = :pemilik");
$stmt->execute(['pemilik' => $user_id]);
$soldBooks = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Dashboard Seller</title>
</head>

<body>
    <h2>Dashboard Seller</h2>
    <a href="src/model/logout.php">Logout</a>

    <h3>Form Penjualan Buku</h3>
    <form method="POST" action="">
        <label for="judul">Judul Buku:</label>
        <input type="text" name="judul" required><br><br>
        <label for="harga">Harga:</label>
        <input type="number" name="harga" required><br><br>
        <button type="submit">Tambah Buku</button>
    </form>

    <h3>Buku yang Dijual</h3>
    <table border="1">
        <tr>
            <th>Book ID</th>
            <th>Judul</th>
            <th>Harga</th>
            <th>Status</th>
        </tr>
        <?php if (count($soldBooks) > 0): ?>
        <?php foreach ($soldBooks as $book): ?>
        <tr>
            <td><?php echo $book['book_id']; ?></td>
            <td><?php echo htmlspecialchars($book['judul']); ?></td>
            <td><?php echo htmlspecialchars($book['harga']); ?></td>
            <td><?php echo htmlspecialchars($book['status']); ?></td>
        </tr>
        <?php endforeach; ?>
        <?php else: ?>
        <tr>
            <td colspan="4">Tidak ada buku yang dijual.</td>
        </tr>
        <?php endif; ?>
    </table>
</body>

</html>