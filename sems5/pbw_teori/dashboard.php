<?php
session_start();
include 'src/model/db.php'; // Pastikan ini mengarah ke file koneksi yang benar

if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit;
}

// Ambil data buku yang masih ada (status 'available')
$stmt = $pdo->prepare("SELECT * FROM books WHERE status = 'available'");
$stmt->execute();
$availableBooks = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>

<body>
    <h2>Selamat datang, <?php echo $_SESSION['username']; ?>!</h2>
    <a href="src/model/logout.php">Logout</a>

    <h3>Buku yang Tersedia</h3>
    <table border="1">
        <tr>
            <th>Book ID</th>
            <th>Judul</th>
            <th>Harga</th>
            <th>Pemilik</th>
            <th>Status</th>
            <th>Aksi</th>
        </tr>
        <?php if (count($availableBooks) > 0): ?>
        <?php foreach ($availableBooks as $book): ?>
        <tr>
            <td><?php echo $book['book_id']; ?></td>
            <td><?php echo $book['judul']; ?></td>
            <td><?php echo $book['harga']; ?></td>
            <td><?php echo $book['pemilik']; ?></td>
            <td><?php echo $book['status']; ?></td>
            <td>
                <a href="transaksi.php?book_id=<?php echo $book['book_id']; ?>">Transaksi</a>
            </td>
        </tr>
        <?php endforeach; ?>
        <?php else: ?>
        <tr>
            <td colspan="6">Tidak ada buku yang tersedia.</td>
        </tr>
        <?php endif; ?>
    </table>
</body>

</html>