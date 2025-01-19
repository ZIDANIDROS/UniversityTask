<x-app-layout>
    @slot('title','Stores')

    <x-slot name="header">
        <h2 class="font-semibold text-xl leading-tight">
            {{ __('Stores') }}
        </h2>
    </x-slot>

    <x-container>
        <div class="grid grid-cols-4 gap-6">
            @foreach ($stores as $store)

            <x-card class="relative p-4 bg-gray-100 rounded-lg shadow-lg">
                <a href="{{ route('stores.show', $store) }}" class="absolute inset-0 w-full h-full"></a>
                <div class="pb-4">
                    @if ($store->logo)
                    <img src="{{ Storage::url($store->logo) }}" alt="{{ $store->name }}" class="rounded-lg w-full">
                    @else
                    <div class="h-16 w-16 rounded-lg bg-zinc-600"></div>
                    @endif
                </div>

                <x-card.header>
                    <x-card.title class="text-xl font-semibold">{{ $store->name }}</x-card.title>
                    <x-card.description class="text-gray-500">
                        {{ str($store->description)->limit(10) }}
                    </x-card.description>

                    @auth
                    @if ($store->user_id === auth()->user()->id)
                    <a href="{{route('stores.edit', $store)}}" class="underline text-blue-600">
                        Edit
                    </a>
                    @endif
                    @endauth
                </x-card.header>
            </x-card>
            @endforeach
        </div>
    </x-container>
</x-app-layout>