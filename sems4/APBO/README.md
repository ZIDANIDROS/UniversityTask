Diagram class
![alt text](DiagramClass.png)

Penjelasan Kelas yang Diperbarui
Kelas Anak
Nama: nama

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Tanggal Lahir: tanggalLahir

Visibilitas: Private (-)
Tipe: Date
Multiplisitas: (satu nilai)
Default: null
Alamat: alamat

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Orang Tua: orangTua

Visibilitas: Private (-)
Tipe: OrangTuaWali
Multiplisitas: [1..1] (satu nilai)
Default: null
Kelas OrangTuaWali
Nama: nama

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Alamat: alamat

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Nomor Telepon: nomorTelepon

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Anak: anak

Visibilitas: Private (-)
Tipe: List<Anak>
Multiplisitas: [0..*] (tak terbatas)
Default: new ArrayList<>()
Kelas Staf
Nama: nama

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Posisi: posisi

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Jadwal Kerja: jadwalKerja

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Metode:

perbaruiData(): Metode untuk memperbarui data staf.
Kelas Admin (Inheritance dari Staf)
Metode:
kelolaJadwal(): Metode untuk mengelola jadwal.
kelolaDataStaf(): Metode untuk mengelola data staf.
kelolaDataOrangTua(): Metode untuk mengelola data orang tua/wali.
Kelas Jadwal
Tanggal: tanggal

Visibilitas: Private (-)
Tipe: Date
Multiplisitas: (satu nilai)
Default: null
Kegiatan: kegiatan

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Staf: staf

Visibilitas: Private (-)
Tipe: List<Staf>
Multiplisitas: [0..*] (tak terbatas)
Default: new ArrayList<>()
Kelas Laporan
Tanggal: tanggal

Visibilitas: Private (-)
Tipe: Date
Multiplisitas: (satu nilai)
Default: null
Jenis: jenis

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Isi: isi

Visibilitas: Private (-)
Tipe: String
Multiplisitas: (satu nilai)
Penjelasan Relasi
Anak dan OrangTuaWali:

Setiap Anak memiliki satu OrangTuaWali.
Setiap OrangTuaWali bisa memiliki banyak Anak.
Jadwal dan Staf:

Setiap jadwal mencakup banyak staf.
Staf dan Laporan:

Staf dapat membuat laporan.
OrangTuaWali dan Laporan:

OrangTuaWali bisa melihat laporan yang dibuat oleh staf.
