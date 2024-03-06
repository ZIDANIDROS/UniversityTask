import pandas as pd
import numpy as np

# 4. METODE TREND EKSPONENSIAL (sudah otomatis ditect data ganjil maupun genap)

# Data contoh
num_columns = 5
tahun_data = [1997, 1998, 1999, 2000, 2001]
pelanggan = [5.0, 5.6, 6.1, 6.7, 7.2]

print("\nData pelanggan PT Telkom:")
print("Tahun:", tahun_data)
print("Jumlah Pelanggan:", pelanggan)

# Membuat DataFrame
data = pd.DataFrame({'Tahun': tahun_data, 'Jumlah Pelanggan': pelanggan})

# Memasukkan tahun dasar
tahun_dasar = int(input("\nMasukkan tahun dasar : "))

# Menghitung nilai X
def hitung_nilai_X(tahun_data, tahun_dasar, tahun_ramalan=None):
    if tahun_ramalan is None:
        return [tahun - tahun_dasar + 0.5 if len(tahun_data) % 2 == 0 else tahun - tahun_dasar for tahun in tahun_data]
    else:
        return tahun_ramalan - tahun_dasar + 0.5 if len(tahun_data) % 2 == 0 else tahun_ramalan - tahun_dasar

nilai_X = hitung_nilai_X(tahun_data, tahun_dasar)
data['X'] = nilai_X  

# Menghitung nilai X^2
data['X^2'] = data['X'] ** 2

# Menghitung logaritma alami dan produknya
data['Ln Jumlah Pelanggan'] = np.log(data['Jumlah Pelanggan'])
data['X * Ln Jumlah Pelanggan'] = data['X'] * data['Ln Jumlah Pelanggan']

# Menghitung jumlah dari X^2, Ln Jumlah Pelanggan, dan X * Ln Jumlah Pelanggan
sigma_X2 = data['X^2'].sum()
sigma_X_Ln_pelanggan = data['X * Ln Jumlah Pelanggan'].sum()

print("\nData setelah perhitungan:")
print(data)

print(f"\nsigma_X^2 = {sigma_X2}")
print(f"sigma X * Ln Jumlah Pelanggan = {sigma_X_Ln_pelanggan}")

# Menghitung 'a' dan 'b'
num_rows = len(data)
a = np.exp(sigma_X_Ln_pelanggan / num_rows)
b = (np.exp(sigma_X_Ln_pelanggan) - a) / sigma_X2

print(f"a = {a}")
print(f"b = {b}")

# Memasukkan tahun untuk peramalan
tahun_ramalan = int(input("\nMasukkan tahun untuk peramalan: "))

# Menghitung nilai X untuk tahun peramalan
nilai_X_ramalan = hitung_nilai_X(tahun_data, tahun_dasar, tahun_ramalan)
print(f"Nilai X untuk tahun {tahun_ramalan}: {nilai_X_ramalan}")

# Menghitung 'Y' berdasarkan 'a', 'b', dan 'nilai_X_ramalan'
Y = a * np.exp(b * nilai_X_ramalan)
print(f"Persamaan Y untuk tahun {tahun_ramalan}: {Y}")