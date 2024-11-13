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
        return view('users.form', [
            'user' => new User(),
            'page_meta' => [
                'title' => 'Create new user',
                'method' => 'post',
                'url' => '/users',
                'submit_text' => 'Create'
            ]
        ]);
    }

    public function store(Request $request)
    {
        User::create($request->validate($this->requestValidate()));

        // dd($request->only('name', 'email', 'password'));

        return redirect('/users');
    }

    public function show($id)
    {
        $user = User::findOrFail($id);
        // $user = User::where('username',$id)->first();
        abort_if(!$user, 404);
        return view('users/show', compact('user'));
    }

    public static function edit(User $user)
    {
        return view('users.form', [
            'user' => new User(),
            'page_meta' => [
                'title' => 'Edit user : ' . $user->name,
                'method' => 'put',
                'url' => '/users/' . $user->id,
                'submit_text' => 'Update'
            ]
        ]);
    }
    public function update(Request $request, User $user)
    {
        $user->update($request->validate($this->requestValidate()));

        // dd($request->only('name', 'email', 'password'));

        return redirect('/users');
    }

    protected function requestValidate()
    {
        return [
            'name' => ['required', 'min:3', 'max:255', 'string'],
            'email' => ['required', 'email'],
            'password' => ['required', 'min:8']
        ];
    }
}
