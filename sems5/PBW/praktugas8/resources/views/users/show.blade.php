<x-app-layout title="Users">
    <x-slot name="heading">{{ $user->name}}</x-slot>

    <div>{{$user->email}}</div>
    <div>{{$user->created_at->diffForHumans()}}</div>

</x-app-layout>