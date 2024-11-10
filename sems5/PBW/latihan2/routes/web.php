<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Models\Product;
use App\Models\Pesanan;
use App\Http\Controllers\ProductController;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\PesananController;
use App\Http\Controllers\TransaksiController;
use App\Http\Controllers\CheckinController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dashboard', function () {
    $products = Product::getFilteredProducts(request('departure_location'));
    return view('dashboard', compact('products'));
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// routes/web.php
Route::middleware(['auth', 'verified'])->group(function () {

    Route::get('/pesanan/dashboard/{product_id}', [PesananController::class, 'index'])->name('pesanan.dashboard');

    Route::post('/pesanan/create/{product_id}', [PesananController::class, 'create'])->name('pesanan.create');

    Route::post('/transaksi/store', [TransaksiController::class, 'store'])->name('transaksi.store');

    Route::get('/transaksi/dashboard/{transaksi_id}', [TransaksiController::class, 'dashboard'])->name('transaksi.dashboard');
});

Route::middleware(['auth', 'admin'])->group(function () {
    Route::get('admin/dashboard', [HomeController::class, 'index'])->name('admin/dashboard');
    Route::get('/admin/products', [ProductController::class, 'index'])->name('admin/products');
    Route::get('/admin/products/create', [ProductController::class, 'create'])->name('admin/products/create');
    Route::post('/admin/products/save', [ProductController::class, 'save'])->name('admin/products/save');
    Route::get('/admin/products/edit/{id}', [ProductController::class, 'edit'])->name('admin/products/edit');
    Route::put('/admin/products/edit/{id}', [ProductController::class, 'update'])->name('admin/products/update');
    Route::get('/admin/products/delete/{id}', [ProductController::class, 'delete'])->name('admin/products/delete');
});

require __DIR__ . '/auth.php';
