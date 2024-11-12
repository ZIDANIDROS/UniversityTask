<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Baris Bahasa Validasi
    |--------------------------------------------------------------------------
    |
    | Baris bahasa berikut berisi pesan kesalahan default yang digunakan oleh
    | kelas validator. Beberapa aturan memiliki beberapa versi seperti aturan
    | ukuran. Jangan ragu untuk mengubah pesan-pesan ini di sini.
    |
    */

    'accepted' => 'kolom :attribute harus diterima.',
    'accepted_if' => 'kolom :attribute harus diterima ketika :other adalah :value.',
    'active_url' => 'kolom :attribute bukan URL yang valid.',
    'after' => 'kolom :attribute harus berupa tanggal setelah :date.',
    'after_or_equal' => 'kolom :attribute harus berupa tanggal setelah atau sama dengan :date.',
    'alpha' => 'kolom :attribute hanya boleh berisi huruf.',
    'alpha_dash' => 'kolom :attribute hanya boleh berisi huruf, angka, tanda hubung, dan garis bawah.',
    'alpha_num' => 'kolom :attribute hanya boleh berisi huruf dan angka.',
    'array' => 'kolom :attribute harus berupa array.',
    'ascii' => 'kolom :attribute hanya boleh berisi karakter alfanumerik satu byte dan simbol.',
    'before' => 'kolom :attribute harus berupa tanggal sebelum :date.',
    'before_or_equal' => 'kolom :attribute harus berupa tanggal sebelum atau sama dengan :date.',
    'between' => [
        'array' => 'kolom :attribute harus memiliki antara :min dan :max item.',
        'file' => 'kolom :attribute harus antara :min dan :max kilobyte.',
        'numeric' => 'kolom :attribute harus antara :min dan :max.',
        'string' => 'kolom :attribute harus antara :min dan :max karakter.',
    ],
    'boolean' => 'kolom :attribute harus bernilai true atau false.',
    'can' => 'kolom :attribute berisi nilai yang tidak diizinkan.',
    'confirmed' => 'Konfirmasi :attribute tidak cocok.',
    'contains' => 'kolom :attribute harus berisi nilai yang diharuskan.',
    'current_password' => 'Kata sandi salah.',
    'date' => 'kolom :attribute bukan tanggal yang valid.',
    'date_equals' => 'kolom :attribute harus berupa tanggal yang sama dengan :date.',
    'date_format' => 'kolom :attribute tidak sesuai dengan format :format.',
    'decimal' => 'kolom :attribute harus memiliki :decimal tempat desimal.',
    'declined' => 'kolom :attribute harus ditolak.',
    'declined_if' => 'kolom :attribute harus ditolak ketika :other adalah :value.',
    'different' => 'kolom :attribute dan :other harus berbeda.',
    'digits' => 'kolom :attribute harus berupa :digits digit.',
    'digits_between' => 'kolom :attribute harus antara :min dan :max digit.',
    'dimensions' => 'kolom :attribute memiliki dimensi gambar yang tidak valid.',
    'distinct' => 'kolom :attribute memiliki nilai duplikat.',
    'doesnt_end_with' => 'kolom :attribute tidak boleh diakhiri dengan salah satu dari berikut: :values.',
    'doesnt_start_with' => 'kolom :attribute tidak boleh dimulai dengan salah satu dari berikut: :values.',
    'email' => 'kolom :attribute harus berupa alamat email yang valid.',
    'ends_with' => 'kolom :attribute harus diakhiri dengan salah satu dari berikut: :values.',
    'enum' => ':attribute yang dipilih tidak valid.',
    'exists' => ':attribute yang dipilih tidak valid.',
    'extensions' => 'kolom :attribute harus memiliki salah satu ekstensi berikut: :values.',
    'file' => 'kolom :attribute harus berupa file.',
    'filled' => 'kolom :attribute harus memiliki nilai.',
    'gt' => [
        'array' => 'kolom :attribute harus memiliki lebih dari :value item.',
        'file' => 'kolom :attribute harus lebih besar dari :value kilobyte.',
        'numeric' => 'kolom :attribute harus lebih besar dari :value.',
        'string' => 'kolom :attribute harus lebih besar dari :value karakter.',
    ],
    'gte' => [
        'array' => 'kolom :attribute harus memiliki :value item atau lebih.',
        'file' => 'kolom :attribute harus lebih besar atau sama dengan :value kilobyte.',
        'numeric' => 'kolom :attribute harus lebih besar atau sama dengan :value.',
        'string' => 'kolom :attribute harus lebih besar atau sama dengan :value karakter.',
    ],
    'hex_color' => 'kolom :attribute harus berupa warna heksadesimal yang valid.',
    'image' => 'kolom :attribute harus berupa gambar.',
    'in' => ':attribute yang dipilih tidak valid.',
    'in_array' => 'kolom :attribute harus ada di :other.',
    'integer' => 'kolom :attribute harus berupa bilangan bulat.',
    'ip' => 'kolom :attribute harus berupa alamat IP yang valid.',
    'ipv4' => 'kolom :attribute harus berupa alamat IPv4 yang valid.',
    'ipv6' => 'kolom :attribute harus berupa alamat IPv6 yang valid.',
    'json' => 'kolom :attribute harus berupa string JSON yang valid.',
    'list' => 'kolom :attribute harus berupa daftar.',
    'lowercase' => 'kolom :attribute harus berupa huruf kecil.',
    'lt' => [
        'array' => 'kolom :attribute harus memiliki kurang dari :value item.',
        'file' => 'kolom :attribute harus kurang dari :value kilobyte.',
        'numeric' => 'kolom :attribute harus kurang dari :value.',
        'string' => 'kolom :attribute harus kurang dari :value karakter.',
    ],
    'lte' => [
        'array' => 'kolom :attribute tidak boleh memiliki lebih dari :value item.',
        'file' => 'kolom :attribute harus kurang atau sama dengan :value kilobyte.',
        'numeric' => 'kolom :attribute harus kurang atau sama dengan :value.',
        'string' => 'kolom :attribute harus kurang atau sama dengan :value karakter.',
    ],
    'mac_address' => 'kolom :attribute harus berupa alamat MAC yang valid.',
    'max' => [
        'array' => 'kolom :attribute tidak boleh memiliki lebih dari :max item.',
        'file' => 'kolom :attribute tidak boleh lebih dari :max kilobyte.',
        'numeric' => 'kolom :attribute tidak boleh lebih dari :max.',
        'string' => 'kolom :attribute tidak boleh lebih dari :max karakter.',
    ],
    'max_digits' => 'kolom :attribute tidak boleh memiliki lebih dari :max digit.',
    'mimes' => 'kolom :attribute harus berupa file dengan tipe: :values.',
    'mimetypes' => 'kolom :attribute harus berupa file dengan tipe: :values.',
    'min' => [
        'array' => 'kolom :attribute harus memiliki setidaknya :min item.',
        'file' => 'kolom :attribute harus setidaknya :min kilobyte.',
        'numeric' => 'kolom :attribute harus setidaknya :min.',
        'string' => 'kolom :attribute harus setidaknya :min karakter.',
    ],
    'min_digits' => 'kolom :attribute harus memiliki setidaknya :min digit.',
    'missing' => 'kolom :attribute harus tidak ada.',
    'missing_if' => 'kolom :attribute harus tidak ada ketika :other adalah :value.',
    'missing_unless' => 'kolom :attribute harus tidak ada kecuali :other adalah :value.',
    'missing_with' => 'kolom :attribute harus tidak ada ketika :values ada.',
    'missing_with_all' => 'kolom :attribute harus tidak ada ketika :values ada.',
    'multiple_of' => 'kolom :attribute harus merupakan kelipatan dari :value.',
    'not_in' => ':attribute yang dipilih tidak valid.',
    'not_regex' => 'Format kolom :attribute tidak valid.',
    'numeric' => 'kolom :attribute harus berupa angka.',
    'password' => [
        'letters' => 'kolom :attribute harus mengandung setidaknya satu huruf.',
        'mixed' => 'kolom :attribute harus mengandung setidaknya satu huruf besar dan satu huruf kecil.',
        'numbers' => 'kolom :attribute harus mengandung setidaknya satu angka.',
        'symbols' => 'kolom :attribute harus mengandung setidaknya satu simbol.',
        'uncompromised' => ':attribute yang diberikan telah muncul dalam kebocoran data. Silakan pilih :attribute yang berbeda.',
    ],
    'present' => 'kolom :attribute harus ada.',
    'prohibited' => 'kolom :attribute dilarang.',
    'prohibited_if' => 'kolom :attribute dilarang ketika :other adalah :value.',
    'prohibited_unless' => 'kolom :attribute dilarang kecuali :other ada di :values.',
    'prohibits' => 'kolom :attribute melarang :other dari hadir.',
    'regex' => 'Format kolom :attribute tidak valid.',
    'required' => 'kolom :attribute wajib diisi.',
    'required_array_keys' => 'kolom :attribute harus berisi entri untuk: :values.',
    'required_if' => 'kolom :attribute wajib diisi ketika :other adalah :value.',
    'required_unless' => 'kolom :attribute wajib diisi kecuali :other ada di :values.',
    'required_with' => 'kolom :attribute wajib diisi ketika :values ada.',
    'required_with_all' => 'kolom :attribute wajib diisi ketika :values ada.',
    'required_without' => 'kolom :attribute wajib diisi ketika :values tidak ada.',
    'required_without_all' => 'kolom :attribute wajib diisi ketika tidak ada :values yang ada.',
    'same' => 'kolom :attribute harus cocok dengan :other.',
    'size' => [
        'array' => 'kolom :attribute harus berisi :size item.',
        'file' => 'kolom :attribute harus :size kilobyte.',
        'numeric' => 'kolom :attribute harus :size.',
        'string' => 'kolom :attribute harus :size karakter.',
    ],
    'starts_with' => 'kolom :attribute harus dimulai dengan salah satu dari berikut: :values.',
    'string' => 'kolom :attribute harus berupa string.',
    'timezone' => 'kolom :attribute harus berupa zona waktu yang valid.',
    'unique' => ':attribute sudah digunakan.',
    'uploaded' => 'kolom :attribute gagal diunggah.',
    'uppercase' => 'kolom :attribute harus berupa huruf besar.',
    'url' => 'kolom :attribute harus berupa URL yang valid.',
    'ulid' => 'kolom :attribute harus berupa ULID yang valid.',
    'uuid' => 'kolom :attribute harus berupa UUID yang valid.',

    /*
    |--------------------------------------------------------------------------
    | Baris Bahasa Validasi Kustom
    |--------------------------------------------------------------------------
    |
    | Di sini Anda dapat menentukan pesan validasi kustom untuk atribut menggunakan
    | konvensi "attribute.rule" untuk memberi nama baris. Ini memungkinkan Anda untuk
    | menentukan pesan khusus untuk aturan atribut tertentu.
    |
    */

    'custom' => [
        'attribute-name' => [
            'rule-name' => 'pesan-kustom',
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Atribut Validasi Kustom
    |--------------------------------------------------------------------------
    |
    | Baris bahasa berikut digunakan untuk mengganti placeholder atribut kami
    | dengan sesuatu yang lebih ramah pembaca seperti "Alamat Email" sebagai
    | pengganti "email". Ini hanya membantu membuat pesan kami lebih ekspresif.
    |
    */

    'attributes' => [],

];