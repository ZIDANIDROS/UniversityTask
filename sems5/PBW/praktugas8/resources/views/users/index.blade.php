<x-app-layout title="Users">
    <x-slot name="heading">Users</x-slot>
    <div class="sm:flex sm:items-center">
        <div class="sm:flex-auto">
            <h1 class="text-base font-semibold leading-6 text-gray-900">Users</h1>
            <p class="mt-2 text-sm text-gray-700">A list of all the users in your account including their name,
                title,
                email and role.</p>
        </div>
        <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
            <button type="button"
                class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                Add user
            </button>
        </div>
    </div>
    <div class="mt-8 flow-root">
        <x-table.index>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Created At</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($users as $user )
                <tr>
                    <td>
                        {{$user->id}}
                        <!-- kalo data tidak beraturan maka seharusnya menggunakan iteriton -->
                    </td>
                    <td>
                        {{$user->name}}
                    </td>
                    <td>
                        {{$user->email}}
                    </td>
                    <td>
                        {{$user->created_at->format('d M Y')}} ||
                        {{$user->created_at->diffForHumans()}}
                    </td>
                </tr>
                @endforeach
            </tbody>
        </x-table.index>
    </div>

</x-app-layout>