<?php

namespace App\Http\Controllers;

use App\Enums\StoreStatus;
use App\Mail\StorePublished;
use App\Models\Store;
use App\Models\User;
use App\Traits\HasRoles;
use Illuminate\Auth\Middleware\Authenticate;
use Illuminate\Http\Request;
use App\Http\Requests\StoreRequest;
use Illuminate\Routing\Controllers;
use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\Storage;
use App\Policies\StorePolicy;
use Illuminate\Http\RedirectResponse;
use Illuminate\View\View;
use Illuminate\Contracts\View\Factory;

class StoreController extends Controller
{

    public function list(): Factory|View
    {
        $stores = Store::query()
            ->with('user:id,name')
            ->withCount('products')
            // ->with('user', fn($query) => $query->select(['id', 'name']))
            ->latest()
            ->paginate(8);

        return view('stores.list', [
            'stores' => $stores,
            'isAdmin' => auth()->user()->isAdmin(),
        ]);
    }

    public function approve(Store $store): RedirectResponse
    {
        $store->status = StoreStatus::ACTIVE;
        $store->save;

        Mail::to($store->user)->send(new StorePublished($store));

        return back();
    }
    /**
     * Display a listing of the resource.
     */
    public function mine(Request $request): Factory|View
    {
        $stores = Store::query()->where('user_id', $request->user()->id)->latest()->paginate(8);

        return view('stores.mine', [
            'stores' => $stores,
        ]);
    }

    public function index(): Factory|View
    {

        $stores = Store::query()
            ->where('status', StoreStatus::ACTIVE)
            ->latest()
            ->get();

        return view('stores.index', [
            'stores' => $stores,
        ]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create(): Factory|View
    {
        return view('stores.form', [
            'store' => new Store(),
            'page_meta' => [
                'title' => 'Create store',
                'description' => 'Create new for yours',
                'method' => 'post',
                'url' => route('stores.store')
            ]
        ]);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreRequest $request): RedirectResponse
    {
        $file = $request->file('logo');

        $request->user()->stores()->create([
            ...$request->validated(),
            ...['logo' => $file->store('images/stores')]
        ]);

        return to_route('stores.index');
    }

    /**
     * Display the specified resource.
     */
    public function show(Store $store): Factory|View
    {
        return view('stores.show', [
            'store' => $store->loadCount('products'),
            'products' => $store->products()->latest()->paginate(10),
        ]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Request $request, Store $store): Factory|View
    {

        Gate::authorize('update', $store);

        // abort_if($request->user()->isNot($store->user), 401);
        return view('stores.form', [
            'store' => $store,
            'page_meta' => [
                'title' => 'Edit store',
                'description' => 'Edit store:' . $store->name,
                'method' => 'put',
                'url' => route('stores.update', $store)
            ]
        ]);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(StoreRequest $request, Store $store): RedirectResponse
    {
        if ($request->hashFile('logo')) {
            Storage::delete($store->logo);
            $file = $request->file('logo')->store('images/stores');
        } else {
            $file = $store->logo;
        }

        $store->update([
            'name' => $request->name,
            'description' => $request->description,
            'logo' => $file,
        ]);

        return to_route('stores.index');
    }

    /**
     * Remove the specified resource from storage.
     */
}