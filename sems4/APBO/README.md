## Penjelasan Diagram Kelas Daycare

![alt text](DiagramClass.png)
</br>

Diagram ini menggambarkan struktur kelas untuk sistem daycare dengan beberapa entitas utama: `Anak`, `wali`, `Staf`, `Jadwal`, dan `Laporan`.

### Kelas dan Atribut

- **Anak**

  - `nama: String` - Nama anak
  - `tanggalLahir: Date` - Tanggal lahir anak (default: `null`)
  - `alamat: String` - Alamat anak
  - `orangTua: wali [1..1]` - Orang tua/wali dari anak (multiplisitas 1..1)
  - Metode:
    - `daftarAnak()`
    - `perbaruiData()`

- **wali**

  - `nama: String` - Nama wali
  - `alamat: String` - Alamat wali
  - `nomorTelepon: String` - Nomor telepon wali
  - `anak: List<Anak> [0..*]` - Daftar anak-anak (multiplisitas 0..\*)
  - Metode:
    - `daftarOrangTua()`
    - `perbaruiData()`

- **Staf**

  - `nama: String` - Nama staf
  - `posisi: String` - Posisi staf
  - `jadwalKerja: String` - Jadwal kerja staf
  - Metode:
    - `perbaruiData()`
    - `kelolaJadwal()`
    - `kelolaDataStaf()`
    - `kelolaDataOrangTua()`

- **Jadwal**

  - `tanggal: Date` - Tanggal kegiatan (default: `null`)
  - `kegiatan: String` - Nama kegiatan
  - `staf: List<Staf> [0..*]` - Daftar staf yang terlibat (multiplisitas 0..\*)
  - Metode:
    - `kelolaJadwal()`

- **Laporan**
  - `tanggal: Date` - Tanggal laporan (default: `null`)
  - `jenis: String` - Jenis laporan
  - `isi: String` - Isi laporan
  - Metode:
    - `lihatLaporan()`

### Relasi

![alt text](ERD.png)

- **Anak** memiliki **wali** dengan multiplisitas `1..1`.
- **wali** dapat memiliki banyak **Anak** dengan multiplisitas `0..*`.
- **Jadwal** melibatkan banyak **Staf** dengan multiplisitas `0..*`.
- **Staf** mengelola banyak **Jadwal** dengan multiplisitas `0..*`.
- **Staf** mengelola banyak **Staf** lain dengan multiplisitas `0..*`.
- **Staf** mengelola banyak **wali** dengan multiplisitas `0..*`.
- **Staf** membuat banyak **Laporan** dengan multiplisitas `0..*`.
- **wali** dapat melihat banyak **Laporan** dengan multiplisitas `0..*`.

Diagram ini memodelkan interaksi dan relasi antara entitas dalam sistem daycare, menggambarkan bagaimana data dikelola dan dihubungkan dalam sistem.

# Daycare System - Entity-Relationship Diagram (ERD)

This UML diagram represents the Entity-Relationship Diagram (ERD) for a daycare system. It outlines the entities involved in the system and their relationships.

## Entities:

### 1. Anak

- Attributes:
  - nama: String
  - tanggalLahir: Date
  - alamat: String
- Relationships:
  - Belongs to one Wali

### 2. Wali

- Attributes:
  - id: int
  - nama: String
  - alamat: String
  - nomorTelepon: String
- Relationships:
  - Has one or more Anak

### 3. Staf

- Attributes:
  - id: int
  - nama: String
  - posisi: String
  - jadwalKerja: String
- Relationships:
  - Manages zero or more Jadwal
  - Can have subordinate Staf
  - Creates zero or more Laporan

### 4. Jadwal

- Attributes:
  - id: int
  - tanggal: Date
  - kegiatan: String
- Relationships:
  - Assigned to by one or more Staf

### 5. Laporan

- Attributes:
  - id: int
  - tanggal: Date
  - jenis: String
  - isi: String
- Relationships:
  - Created by zero or more Staf

## Relationships:

- Anak and Wali have a one-to-one relationship.
- Staf and Jadwal have a one-to-many relationship.
- Staf and Staf have a many-to-many relationship (Atasan).
- Staf and Laporan have a many-to-many relationship (Membuat).
