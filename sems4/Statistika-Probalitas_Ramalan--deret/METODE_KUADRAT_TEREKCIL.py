import pandas as pd

# 2. METODE KUADRAT TERKECIL (sudah otomatis ditect data ganjil maupun genap)

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

# Create a DataFrame
data = pd.DataFrame({'Tahun': tahun_data, 'Jumlah Pelanggan': pelanggan})

# Meminta input untuk tahun dasar
tahun_dasar = int(input("\nMasukkan tahun dasar : "))

def hitung_nilai_X(tahun_data, tahun_dasar, tahun_ramalan=None):
    if tahun_ramalan is None:
        return [tahun - tahun_dasar + 0.5 if len(tahun_data) % 2 == 0 else tahun - tahun_dasar for tahun in tahun_data]
    else:
        return tahun_ramalan - tahun_dasar + 0.5 if len(tahun_data) % 2 == 0 else tahun_ramalan - tahun_dasar


# membuat 'X' pada kolom
nilai_X = hitung_nilai_X(tahun_data, tahun_dasar)
data['X'] = nilai_X  


# Hitung sigma pelanggan sebagai Y
sigma_pelanggan = data['Jumlah Pelanggan'].sum()

# Hitung XY
data['XY'] = data['X'] * data['Jumlah Pelanggan']

# Hitung X^2
data['X^2'] = data['X'] ** 2

print("\nData setelah perhitungan:")
print(data)

# Menghitung rata-rata pelanggan untuk tahun dasar
rata_rata_pelanggan = sigma_pelanggan / len(pelanggan)

# Hitung a dan b
sigma_Y = data['Jumlah Pelanggan'].sum()
sigma_Y_bulat = round(sigma_Y, 2)
sigma_XY = data['XY'].sum()
sigma_XY_bulat = round(sigma_XY, 2)
sigma_X2 = data['X^2'].sum()

print(f"\nsigma_Y = {sigma_Y_bulat}")
print(f"sigma_XY = {sigma_XY_bulat}")
print(f"sigma_X^2 = {sigma_X2}")

a = sigma_Y_bulat / len(data)
b = sigma_XY_bulat / sigma_X2
b_bulat = round(b, 2)

# Persamaan tren
def persamaan_tren(X):
    return a + b * X

print(f"\na = {a}")
print(f"b = {b_bulat}")
print(f"Persamaan tren: Y = {a} + {b_bulat} * X")

# Tahun ramalan untuk menghitung X
tahun_ramalan = int(input("\nMasukkan tahun untuk peramalan: "))

# Menghitung nilai X untuk tahun ramalan
nilai_X_ramalan = hitung_nilai_X(tahun_data, tahun_dasar, tahun_ramalan)
print(f"Nilai X untuk tahun {tahun_ramalan}: {nilai_X_ramalan}")

Y = a + b_bulat * nilai_X_ramalan
Y_Bulat = round(Y, 2)
print(f"Y {tahun_ramalan} = {a} + {b_bulat} * {nilai_X_ramalan} = {Y_Bulat}")