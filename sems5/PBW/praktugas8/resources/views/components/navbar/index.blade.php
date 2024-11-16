<nav class="bg-gray-800">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="relative flex h-16 items-center justify-between">
            <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
                <button type="button"
                    class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                    aria-controls="mobile-menu" aria-expanded="false">
                    <span class="sr-only">Open main menu</span>
                    <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                        aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                    </svg>
                </button>
            </div>
            <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                <div class="flex shrink-0 items-center">
                    <img class="h-8 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=500"
                        alt="Your Company">
                </div>
                <div class="hidden sm:ml-6 sm:block">
                    <div class="flex space-x-4">
                        <x-navbar.link href="/">
                            Menu
                        </x-navbar.link>
                        <x-navbar.link href="{{ route('about') }}">
                            About
                        </x-navbar.link>
                        <x-navbar.link href="{{ route('contact') }}">
                            Contact
                        </x-navbar.link>
                        <x-navbar.link href="{{ route('gallery') }}">
                            Gallery
                        </x-navbar.link>

                        @auth
                        <x-navbar.link href="{{ route('users.index') }}">
                            User
                        </x-navbar.link>

                        <x-navbar.link href="#">
                            {{Auth::user()->email}}
                        </x-navbar.link>

                        <form action="{{ route('logout') }}" method="POST">
                            @csrf
                            <x-button type="submit">
                                Log Out
                            </x-button>
                        </form>
                        @else
                        <x-navbar.link href="{{ route('login') }}">
                            Login
                        </x-navbar.link>
                        @endauth

                    </div>

                </div>
            </div>
        </div>
    </div>

    <div class="sm:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pb-3 pt-2">
            <x-navbar.dropdown-item href="/">
                Menu</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="{{ route('about') }}">
                About</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="{{ route('contact') }}">
                Contact</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="{{ route('gallery') }}">
                Gallery</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="{{ route('users.index') }}">
                User</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="{{ route('login') }}">
                Login</x-navbar.dropdown-item>
        </div>
    </div>
</nav>