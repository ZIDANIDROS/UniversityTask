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
                        <x-navbar.link href="/about">
                            About
                        </x-navbar.link>
                        <x-navbar.link href="/contact">
                            Contact
                        </x-navbar.link>
                        <x-navbar.link href="/gallery">
                            Gallery
                        </x-navbar.link>
                        <x-navbar.link href="/users">
                            User
                        </x-navbar.link>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <div class="sm:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pb-3 pt-2">
            <x-navbar.dropdown-item href="/">
                Menu</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="/about">
                About</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="/contact">
                Contact</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="/gallery">
                Gallery</x-navbar.dropdown-item>
            <x-navbar.dropdown-item href="/users">
                User</x-navbar.dropdown-item>
        </div>
    </div>
</nav>