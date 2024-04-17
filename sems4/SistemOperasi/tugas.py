class Proses:
    def __init__(self, nama, prioritas):
        self.nama = nama
        self.prioritas = prioritas

class Penjadwal:
    def __init__(self):
        self.antrian = []

    def tambah_proses(self, proses):
        self.antrian.append(proses)
        self.antrian.sort(key=lambda x: x.prioritas)

    def jalankan_proses_selanjutnya(self):
        if self.antrian:
            proses_selanjutnya = self.antrian.pop(0)
            print("Menjalankan proses:", proses_selanjutnya.nama)
        else:
            print("Tidak ada proses untuk dijalankan")

if __name__ == "__main__":
    penjadwal = Penjadwal()

    while True:
        nama = input("Masukkan nama proses (atau 'exit' untuk keluar): ")
        if nama.lower() == 'exit':
            break
        prioritas = int(input("Masukkan prioritas untuk proses tersebut: "))
        penjadwal.tambah_proses(Proses(nama, prioritas))

    print()

    for _ in range(len(penjadwal.antrian)):
        penjadwal.jalankan_proses_selanjutnya()