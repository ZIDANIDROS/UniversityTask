<x-app-layout title="Users">
    <x-slot name="heading">{{ $user->name}}</x-slot>

    <div>{{$user->email}}</div>
    <div>{{$user->created_at->diffForHumans()}}</div>

    <form action="/users/{{ $user->id }}" class="mt-6" method="POST">
        @method('DELETE')
        @csrf
        <x-button type="submit">
            Delete
        </x-button>
    </form>

</x-app-layout>