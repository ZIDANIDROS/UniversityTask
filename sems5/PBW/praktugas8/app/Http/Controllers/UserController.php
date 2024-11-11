<?php

namespace App\Http\Controllers;

use \App\Models\User;
use Illuminate\Support\Facades\DB;

class UserController extends Controller
{
    // public function index()
    // {
    //     $users = User::query()->get();

    //     return view('users.index', [
    //         'users' => $users,
    //     ]);
    // }
    public function index()
    {
        $users = User::query()->get();

        return view('users.index', compact('users'));
    }
}
