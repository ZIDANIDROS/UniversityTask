<?php
class User
{
    private $pdo;

    // Konstruktor untuk menginisialisasi koneksi PDO
    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    // Fungsi untuk mendaftarkan pengguna baru
    public function register($username, $email, $password, $role)
    {
        if (empty($username) || empty($email) || empty($password) || empty($role)) {
            return ['success' => false, 'message' => 'Semua field harus diisi.'];
        }

        // Simpan password langsung tanpa hashing untuk implementasi sederhana
        $stmt = $this->pdo->prepare("INSERT INTO users (username, email, password, role) VALUES (:username, :email, :password, :role)");

        try {
            $stmt->execute([
                'username' => $username,
                'email'    => $email,
                'password' => $password,
                'role'     => $role
            ]);
            return ['success' => true, 'message' => 'Registrasi berhasil.'];
        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                return ['success' => false, 'message' => 'Username atau email sudah terdaftar.'];
            }
            return ['success' => false, 'message' => 'Terjadi kesalahan: ' . $e->getMessage()];
        }
    }

    // Fungsi untuk mencari pengguna berdasarkan username
    public function findByUsername($username)
    {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        return $stmt->fetch(PDO::FETCH_ASSOC); // Mengembalikan hasil sebagai array asosiatif
    }
}
