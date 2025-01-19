<?php

namespace App\Models;

use App\Observers\StoreObserver;
use App\Enums\StoreStatus;
use Illuminate\Database\Eloquent\Attributes\ObservedBy;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations;
use Illuminate\Database\Eloquent\Factories\HasFactory;

#[ObservedBy(StoreObserver::class)]
class Store extends Model
{
    use HasFactory;

    protected $fillable = [
        'logo',
        'name',
        'slug',
        'description',
        'status',
        'user_id',
    ];

    protected $casts = [
        'status' => StoreStatus::class,
    ];

    public function user(): Relations\BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function products(): Relations\HasMany
    {
        return $this->hasMany(Product::class);
    }
}