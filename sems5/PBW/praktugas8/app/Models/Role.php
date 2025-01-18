<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\belongsToMany;

class Role extends Model
{
    protected $fillable = ['name'];

    public function users(): belongsToMany
    {
        return $this->belongsToMany(User::class, 'user_role');
    }
}
