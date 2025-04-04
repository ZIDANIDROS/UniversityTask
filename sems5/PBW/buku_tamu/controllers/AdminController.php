<?php
include_once __DIR__ . '/../config/Database.php';
include_once __DIR__ . '/../models/Admin.php';

class AdminController
{
    private $admin;

    public function __construct()
    {
        $database = new Database();
        $db = $database->getConnection();
        $this->admin = new Admin($db);
    }

    // Fungsi untuk login
    public function login($username, $password)
    {
        $this->admin->username = $username;
        $this->admin->password = $password;
        return $this->admin->login();
    }
}
