<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers;
use App\Models\Article;

Route::get('/', [Controllers\HomeController::class, 'index']);
Route::get('/about', [Controllers\AboutController::class, 'index'])->name('about');
Route::get('/contact', [Controllers\ContactController::class, 'index'])->name('contact');
Route::get('/gallery', [Controllers\GalleryController::class, 'index'])->name('gallery');

Route::resource('users', Controllers\UserController::class);

// Route::get('/users', [Controllers\UserController::class, 'index'])->name('users.index');
// Route::get('/users/create', [Controllers\UserController::class, 'create']);
// Route::post('/users', [Controllers\UserController::class, 'store']);
// Route::get('/users/{user:id}', [Controllers\UserController::class, 'show']);
// Route::get('/users/{user:id}/edit', [Controllers\UserController::class, 'edit']);
// Route::put('/users/{user:id}', [Controllers\UserController::class, 'update']);
// Route::delete('/users/{user:id}', [Controllers\UserController::class, 'destroy']);