<?php

namespace Database\Factories;

use App\Enums\StoreStatus;
use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\User;
use Illuminate\Support\Str;

class StoreFactory extends Factory
{
    public function definition(): array
    {
        return [
            'user_id' => rand(1, 10),
            'name' => $title = str(fake()->word())->title(),
            'slug' => str($title)->slug(),
            'description' => fake()->paragraph(2, true),
            'status' => StoreStatus::ACTIVE
        ];
    }
}