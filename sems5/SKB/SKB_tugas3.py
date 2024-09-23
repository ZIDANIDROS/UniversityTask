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

# ------------------------------------------------------------

# Mengubah hasil kembali ke DataFrame jika diperlukan
normalized_data = pd.DataFrame(normalized_data, columns=data.select_dtypes(include=[np.number]).columns)

# print("Data setelah penanganan outliers:")
# print(data,'\n')

# print("Data setelah standarisasi:")
# print(standardized_data,'\n')
# print("Data setelah normalisasi:")
# print(normalized_data,'\n')

# ------------------------------------------------------------

# Mengonversi kolom Date_reported menjadi tipe datetime
# data['Date_reported'] = pd.to_datetime(data['Date_reported'], format='%d/%m/%Y')

# Membuat fitur baru berdasarkan tanggal
data['Year'] = data['Date_reported'].dt.year
data['Month'] = data['Date_reported'].dt.month
data['Day_of_week'] = data['Date_reported'].dt.dayofweek  # 0 = Monday, 6 = Sunday
data['Is_weekend'] = data['Day_of_week'].apply(lambda x: 1 if x >= 5 else 0)  # 1 = weekend, 0 = weekday

# Cek hasilnya
# data[['Date_reported', 'Year', 'Month', 'Day_of_week', 'Is_weekend']].head()


# ------------------------------------------------------------

# Transformasi logaritmik pada kolom yang mengandung nilai positif
import numpy as np

# Hindari log(0) dengan menambahkan 1 untuk data yang tidak nol
data['Log_New_cases'] = np.log1p(data['New_cases'].fillna(0))
data['Log_Cumulative_cases'] = np.log1p(data['Cumulative_cases'].fillna(0))
data['Log_New_deaths'] = np.log1p(data['New_deaths'].fillna(0))
data['Log_Cumulative_deaths'] = np.log1p(data['Cumulative_deaths'].fillna(0))

# Cek hasil
# data[['New_cases', 'Log_New_cases', 'Cumulative_cases', 'Log_Cumulative_cases']].head()

# ------------------------------------------------------------

# Menghitung death rate (jika New_cases > 0)
data['Death_rate'] = np.where(data['New_cases'] > 0, data['New_deaths'] / data['New_cases'], 0)

# Cek hasil
data[['New_cases', 'New_deaths', 'Death_rate']].head()

# ------------------------------------------------------------

# Membuat lagging untuk kolom kasus dan kematian
data['Lag_1_day_cases'] = data['New_cases'].shift(1)
data['Lag_1_day_deaths'] = data['New_deaths'].shift(1)

# Cek hasil
# data[['Date_reported', 'New_cases', 'Lag_1_day_cases', 'New_deaths', 'Lag_1_day_deaths']].head()

# ------------------------------------------------------------

# One-hot encoding untuk WHO_region
data_encoded = pd.get_dummies(data, columns=['WHO_region'])

# Cek hasil
# data_encoded.head()