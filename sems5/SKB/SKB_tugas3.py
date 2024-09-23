import pandas as pd

data = pd.read_csv('WHO-COVID-19-global-data.csv', sep=';')

data_info = data.info()
data_head = data.head()


# data_info
# print('\n')
# data_head

# ------------------------------------------------------------

# print(data.isnull().sum())

# ------------------------------------------------------------
# data.isnull().sum()
# ------------------------------------------------------------
# Penanganan Outliers
# Outliers dapat mengganggu perhitungan statistik, model prediksi, dan visualisasi.
def wisker(col):
    q1, q3 = np.percentile(col, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    return lower_bound, upper_bound

# data.columns

# ------------------------------------------------------------

# Menampilkan dataframe setelah menghapus outliers
# print("\nData setelah menghapus outliers:")
# print(data.describe())

# ------------------------------------------------------------

# Identifikasi Data terduplikat
print("Jumlah Data Terduplikat : ",data.duplicated().sum())

# ------------------------------------------------------------

import numpy as np
from sklearn.preprocessing import StandardScaler

# Mengganti nilai tak terhingga dengan NaN
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Mengisi nilai NaN pada kolom numerik dengan rata-rata
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols].fillna(data[numeric_cols].mean(), inplace=True)

# Periksa kembali apakah masih ada nilai NaN
if data[numeric_cols].isnull().values.any():
    print("Masih ada nilai NaN setelah pengisian.")
else:
    print("Semua nilai NaN sudah diisi.")

# Standardisasi data untuk kolom numerik
scaler_standard = StandardScaler()
standardized_data = scaler_standard.fit_transform(data[numeric_cols])

# Jika ingin mengubah hasil standar menjadi DataFrame
standardized_df = pd.DataFrame(standardized_data, columns=numeric_cols)

# Menggabungkan kembali kolom yang sudah distandarisasi dengan kolom non-numerik
non_numeric_cols = data.select_dtypes(exclude=[np.number]).columns
final_df = pd.concat([standardized_df, data[non_numeric_cols].reset_index(drop=True)], axis=1)

# Menampilkan deskripsi dari data final
# print(final_df.describe())


# ------------------------------------------------------------

from sklearn.preprocessing import MinMaxScaler

# Pertama, lakukan standardisasi
scaler_standard = StandardScaler()
standardized_data = scaler_standard.fit_transform(data[numeric_cols])

# Buat DataFrame untuk data yang sudah distandarisasi
standardized_df = pd.DataFrame(standardized_data, columns=numeric_cols)

# Lalu, lakukan normalisasi
scaler_minmax = MinMaxScaler()
normalized_data = scaler_minmax.fit_transform(standardized_df)

# Buat DataFrame untuk data yang sudah dinormalisasi
normalized_df = pd.DataFrame(normalized_data, columns=numeric_cols)

# Gabungkan kembali kolom yang sudah dinormalisasi dengan kolom non-numerik
final_df = pd.concat([normalized_df, data[non_numeric_cols].reset_index(drop=True)], axis=1)

# Menampilkan deskripsi dari data final
# print(final_df.describe())