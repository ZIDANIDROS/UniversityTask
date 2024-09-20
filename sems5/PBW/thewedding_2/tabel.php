<?php
include 'koneksi.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Buku Tamu</title>
</head>

<body>
    <h1>Daftar Buku Tamu</h1>

    <table border="1">
        <tr>
            <th>Nama</th>
            <th>Email</th>
            <th>Komentar</th>
            <th>Tanggal</th>
        </tr>

        <?php
        $sql = "SELECT nama, email, komentar, tanggal FROM tamu ORDER BY tanggal DESC";
        $stmt = $conn->prepare($sql);
        $stmt->execute();

        if ($stmt->rowCount() > 0) {
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo "<tr>";
                echo "<td>" . htmlspecialchars($row["nama"]) . "</td>";
                echo "<td>" . htmlspecialchars($row["email"]) . "</td>";
                echo "<td>" . htmlspecialchars($row["komentar"]) . "</td>";
                echo "<td>" . $row["tanggal"] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='4'>Belum ada data tamu.</td></tr>";
        }

        $conn = null;
        ?>
    </table>

    <p><a href="index.php">Kembali ke Landing Page</a></p>
</body>

</html>