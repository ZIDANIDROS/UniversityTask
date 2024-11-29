<x-app-layout>

    @slot('title','Create a store')

    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            {{ __('Create a store') }}
        </h2>
    </x-slot>

    <x-container>
        <x-card>
            <x-card.header>
                <x-card.title>Create new store</x-card.title>
                <x-card.description>
                    you can create up to 5 stores.
                </x-card.description>
            </x-card.header>

            <x-card.content>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum, minus nesciunt? Esse modi velit
                aperiam,
                eius rerum deserunt assumenda vitae! Ut dolores provident architecto similique ab labore. Qui, aliquam.
                Minima!
            </x-card.content>
        </x-card>
    </x-container>

</x-app-layout>