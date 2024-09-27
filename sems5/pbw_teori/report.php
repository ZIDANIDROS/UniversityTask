<?php
session_start();
include 'src/model/db.php'; // Pastikan ini mengarah ke file koneksi yang benar

if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
    exit;
}

// Cek apakah book_id ada dalam parameter URL
if (!isset($_GET['book_id'])) {
    header('Location: dashboard.php'); // Kembali ke dashboard jika tidak ada book_id
    exit;
}

$book_id = $_GET['book_id'];

// Ambil data transaksi terakhir untuk buku tersebut
$stmt = $pdo->prepare("SELECT * FROM transactions WHERE book_id = :book_id ORDER BY transaction_id DESC LIMIT 1");
$stmt->execute(['book_id' => $book_id]);
$transaction = $stmt->fetch(PDO::FETCH_ASSOC);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Laporan Pembelian</title>
</head>

<body>
    <h2>Laporan Pembelian</h2>
    <?php if ($transaction): ?>
        <p><strong>ID Transaksi:</strong> <?php echo $transaction['transaction_id']; ?></p>
        <p><strong>Judul Buku:</strong> <?php echo $transaction['book_id']; ?></p>
        <p><strong>Jumlah:</strong> <?php echo $transaction['amount']; ?></p>
        <p><strong>Tanggal Transaksi:</strong> <?php echo $transaction['transaction_date']; ?></p>
        <p><strong>Jenis Transaksi:</strong> <?php echo $transaction['transaction_type']; ?></p>
        <a href="dashboard.php">Kembali ke Dashboard</a>
    <?php else: ?>
        <p>Tidak ada laporan pembelian untuk buku ini.</p>
        <a href="dashboard.php">Kembali ke Dashboard</a>
    <?php endif; ?>
</body>

</html>