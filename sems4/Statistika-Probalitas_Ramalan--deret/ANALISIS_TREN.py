import pandas as pd

# 1. ANALISIS TREN (sudah otomatis ditect data ganjil maupun genap)

# Meminta input untuk jumlah data
num_columns = int(input("Masukkan jumlah data yang ingin dimasukkan: "))

# Inisialisasi list untuk tahun dan pelanggan
tahun_data = []
pelanggan = []

# Meminta input untuk tahun dan jumlah pelanggan sesuai dengan jumlah data yang diminta
for i in range(num_columns):
    tahun = int(input(f"Masukkan tahun ke-{i+1}: "))
    jumlah_pelanggan = float(input(f"Masukkan jumlah pelanggan untuk tahun {tahun}: "))
    tahun_data.append(tahun)
    pelanggan.append(jumlah_pelanggan)

print("\nData pelanggan PT Telkom:")
print("Tahun:", tahun_data)
print("Jumlah Pelanggan:", pelanggan)

# Meminta input untuk dua tahun dasar
tahun_dasar_1 = int(input("\nMasukkan tahun dasar ke-1 : "))
tahun_dasar_2 = int(input("Masukkan tahun dasar ke-2 : "))

# Fungsi untuk menghitung nilai X
def hitung_nilai_X(tahun_data, tahun_dasar):
    return [tahun - tahun_dasar for tahun in tahun_data]

# Program memilah menjadi 2 tabel yaitu K1 dan K2 
index_split = tahun_data.index(tahun_dasar_2)

tahun_data_k1 = tahun_data[:index_split - 1:]
pelanggan_k1 = pelanggan[:index_split - 1:]

num_columns = len(tahun_data)
if num_columns % 2 != 0: # DATA GANJIL
    tahun_data_k2 = tahun_data[index_split - 2:]
    pelanggan_k2 = pelanggan[index_split - 2:]
else: # DATA GENAP
    tahun_data_k2 = tahun_data[index_split - 1:]
    pelanggan_k2 = pelanggan[index_split - 1:]

# Membuat DataFrames untuk K1 dan K2
k1 = pd.DataFrame({'Tahun': tahun_data_k1, 'Jumlah Pelanggan': pelanggan_k1})
k2 = pd.DataFrame({'Tahun': tahun_data_k2, 'Jumlah Pelanggan': pelanggan_k2})

print("K1:")
print(k1.to_string(index=False))

print("\nK2:")
print(k2.to_string(index=False))

# Menampilkan nilai X untuk dua tahun dasar
nilai_X_1 = hitung_nilai_X(tahun_data, tahun_dasar_1)
print("\nTahun dasar ke-1:")
print("Tahun:", tahun_data)
print("Jumlah Pelanggan:", pelanggan)
print("X :", nilai_X_1)

nilai_X_2 = hitung_nilai_X(tahun_data, tahun_dasar_2)
print("\nTahun dasar ke-2:")
print("Tahun:", tahun_data)
print("Jumlah Pelanggan:", pelanggan)
print("X :", nilai_X_2)

# Menghitung rata-rata K1 dan K2
a1 = sum(pelanggan_k1) / len(pelanggan_k1)
a1_bulat = round(a1, 2)
a2 = sum(pelanggan_k2) / len(pelanggan_k2)
a2_bulat = round(a2, 2)

# Menghitung nilai b
b = (a2 - a1) / (tahun_dasar_2 - tahun_dasar_1)
b_bulat = round(b, 2)

# Cetak nilai a1, a2, dan b
print("\nNilai a1:", a1_bulat)
print("Nilai a2:", a2_bulat)
print("Nilai b:", b_bulat)

# Persamaan tren untuk tahun dasar ke-1
def persamaan_tren_1(X):
    return a1 + b * X

# Persamaan tren untuk tahun dasar ke-2
def persamaan_tren_2(X):
    return a2 + b * X

# Prediksi untuk tahun dasar ke-1
tahun_ramalan = int(input("\nMasukkan tahun untuk peramalan: ")) 

# Prediksi untuk tahun dasar ke-1
X_tahun_ramalan_1 = tahun_ramalan - tahun_dasar_1
prediksi_tahun_1 = persamaan_tren_1(X_tahun_ramalan_1)
print(f"Prediksi untuk tahun dasar ke-1 ({tahun_dasar_1}) pada tahun {tahun_ramalan}: {prediksi_tahun_1} juta pelanggan")

# Prediksi untuk tahun dasar ke-2
X_tahun_ramalan_2 = tahun_ramalan - tahun_dasar_2
prediksi_tahun_2 = persamaan_tren_2(X_tahun_ramalan_2)
print(f"Prediksi untuk tahun dasar ke-2 ({tahun_dasar_2}) pada tahun {tahun_ramalan}: {prediksi_tahun_2} juta pelanggan")