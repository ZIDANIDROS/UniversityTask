import pandas as pd

# 1. DENGAN MENGGUNAKAN ANALISIS TREN METODE SEMI RATA-RATA (sudah otomatis ditect data ganjil maupun genap)

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
a2 = sum(pelanggan_k2) / len(pelanggan_k2)

# Menghitung nilai b
b = (a2 - a1) / (tahun_dasar_2 - tahun_dasar_1)

# Cetak nilai a1, a2, dan b
print("\nNilai a1:", a1)
print("Nilai a2:", a2)
print("Nilai b:", b)

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

# 3. METODE KUADRATIS (sudah otomatis ditect data ganjil maupun genap)

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

# Hitung XY
data['X^2*Y'] = data['X'] ** 2 * data['Jumlah Pelanggan']

# Hitung X^2
data['X^4'] = data['X'] ** 2 * data['X^2']

print("\nData setelah perhitungan:")
print(data)

# Menghitung rata-rata pelanggan untuk tahun dasar
rata_rata_pelanggan = sigma_pelanggan / len(pelanggan)

# Hitung pembulatan
sigma_Y = data['Jumlah Pelanggan'].sum()
sigma_Y_bulat = round(sigma_Y, 2)

sigma_XY = data['XY'].sum()
sigma_XY_bulat = round(sigma_XY, 2)

sigma_X2 = data['X^2'].sum()
sigma_X2_bulat = round(sigma_X2, 2)

sigma_X2Y = data['X^2*Y'].sum()
sigma_X2Y_bulat = round(sigma_X2Y, 2)

sigma_X4 = data['X^4'].sum()
sigma_X4_bulat = round(sigma_X4, 2)

print(f"\nsigma_Y = {sigma_Y_bulat}")
print(f"sigma_XY  = {sigma_XY_bulat}")
print(f"sigma_X^2 = {sigma_X2_bulat}")
print(f"sigma_X2Y = {sigma_X2Y_bulat}")
print(f"sigma_X4  = {sigma_X4_bulat}")

# Mencari nilai A B C untuk menjadi persamaan
a = ( (sigma_Y_bulat * sigma_X4_bulat) - (sigma_X2Y_bulat * sigma_X2_bulat) ) / ( (num_columns * sigma_X4_bulat) - (sigma_X2_bulat) )
a_bulat = round(a, 2)
print(f"\na = {sigma_Y_bulat} * {sigma_X4_bulat} - {sigma_X2Y_bulat} * {sigma_X2_bulat} / {num_columns} * {sigma_X4_bulat} - {sigma_X2_bulat} = {a_bulat}")

b = sigma_XY_bulat / sigma_X2_bulat
b_bulat = round(b, 2)
print(f"b = {sigma_XY_bulat} / {sigma_X2_bulat} = {b_bulat}")

c = ( ( num_columns * sigma_X2Y_bulat ) - (sigma_X2_bulat * sigma_Y_bulat) ) / ( ( num_columns * sigma_X4_bulat ) - (sigma_X2_bulat) )
print(f"c = ( {num_columns} * {sigma_X2Y_bulat} - {sigma_X2_bulat} * {sigma_Y_bulat}) / ({num_columns} * {sigma_X4_bulat} - {sigma_X2_bulat} ) = {c}")

# Tahun ramalan untuk menghitung X
tahun_ramalan = int(input("\nMasukkan tahun untuk peramalan: "))

# Menghitung nilai X untuk tahun ramalan
nilai_X_ramalan = hitung_nilai_X(tahun_data, tahun_dasar, tahun_ramalan)
print(f"Nilai X untuk tahun {tahun_ramalan}: {nilai_X_ramalan}")

# Menghitung nilai persamaan Y
Y = a_bulat + ( b_bulat * nilai_X_ramalan ) + ( c * nilai_X_ramalan*nilai_X_ramalan )
Y_Bulat = round(Y, 2)
print(f"Y {tahun_ramalan} = {a_bulat} + ( {b_bulat} * {nilai_X_ramalan} ) + ( {c} * {nilai_X_ramalan}^2 ) = {Y_Bulat}")