<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Role;
use App\Models\User;

class RoleSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */


    public function run(): void
    {
        $user = User::create([
            'name' => 'Husein',
            'email' => 'Husein@gmail.com',
            'password' => bcrypt('password'),
        ]);

        User::factory(10)->create();

        collect([
            ['name' => 'admin'],
            ['name' => 'partner'],
        ])->each(fn($role) => Role::create($role));

        $user2 = User::find(2);

        $user->assignRole(Role::find(1));
        $user2->assignRole(Role::find(2));
    }
}
