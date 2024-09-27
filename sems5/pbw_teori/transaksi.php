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

// Ambil data buku berdasarkan book_id
$stmt = $pdo->prepare("SELECT * FROM books WHERE book_id = :book_id");
$stmt->execute(['book_id' => $book_id]);
$book = $stmt->fetch(PDO::FETCH_ASSOC);

// Proses pembelian jika form disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_id = $_SESSION['user_id'];
    $amount = $book['harga'];

    // Tambahkan transaksi ke tabel transactions
    $stmt = $pdo->prepare("INSERT INTO transactions (transaction_date, transaction_type, amount, user_id, book_id) VALUES (NOW(), 'buy', :amount, :user_id, :book_id)");
    $stmt->execute([
        'amount' => $amount,
        'user_id' => $user_id,
        'book_id' => $book_id
    ]);

    // Update status buku menjadi 'sold'
    $stmt = $pdo->prepare("UPDATE books SET status = 'sold' WHERE book_id = :book_id");
    $stmt->execute(['book_id' => $book_id]);

    // Redirect ke halaman laporan
    header('Location: report.php?book_id=' . $book_id);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Rincian Transaksi</title>
</head>

<body>
    <h2>Rincian Transaksi Buku</h2>
    <?php if ($book): ?>
        <p><strong>Judul:</strong> <?php echo $book['judul']; ?></p>
        <p><strong>Harga:</strong> <?php echo $book['harga']; ?></p>
        <p><strong>Pemilik:</strong> <?php echo $book['pemilik']; ?></p>
        <p><strong>Status:</strong> <?php echo $book['status']; ?></p>

        <h3>Konfirmasi Pembelian</h3>
        <form method="POST" action="">
            <button type="submit">Beli</button>
        </form>
        <a href="dashboard.php">Kembali ke Dashboard</a>
    <?php else: ?>
        <p>Buku tidak ditemukan.</p>
        <a href="dashboard.php">Kembali ke Dashboard</a>
    <?php endif; ?>
</body>

</html>