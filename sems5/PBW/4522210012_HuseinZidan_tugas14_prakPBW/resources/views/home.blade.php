<x-app-layout>
    @slot('title','Home')
    <x-slot name="header">
        <h2 class="font-semibold text-xl leading-tight">
            {{ __('Dashboard') }}
        </h2>
    </x-slot>



</x-app-layout>