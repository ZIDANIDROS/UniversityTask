<?php

namespace App\Http\Controllers;

use \App\Models\User;
use Illuminate\Http\Request;
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
        $users = User::query()->latest()->get();

        return view('users.index', compact('users'));
    }

    public function create()
    {
        return view('users.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => ['required', 'min:3', 'max:255', 'string'],
            'email' => ['required', 'email'],
            'password' => ['required', 'min:8']
        ]);

        // dd($request->only('name', 'email', 'password'));
        User::create($validated);
        return redirect('/users');
    }

    public function show($id)
    {
        $user = User::findOrFail($id);
        // $user = User::where('username',$id)->first();
        abort_if(!$user, 404);
        return view('users/show', compact('user'));
    }
}