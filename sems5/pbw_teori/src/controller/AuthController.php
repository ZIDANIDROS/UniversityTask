<?php
class AuthController
{
    private $userModel;

    public function __construct($userModel)
    {
        $this->userModel = $userModel;
    }

    public function login($username, $password)
    {
        $user = $this->userModel->findByUsername($username);

        if (!$user) {
            return ['success' => false, 'message' => 'Username tidak ditemukan.'];
        }

        // Cek password (pastikan password disimpan dengan metode hashing di database)
        if ($user['password'] === $password) {
            $_SESSION['user_id'] = $user['id']; // Simpan ID pengguna di sesi
            return ['success' => true, 'message' => 'Login berhasil!'];
        } else {
            return ['success' => false, 'message' => 'Password salah.'];
        }
    }
}
