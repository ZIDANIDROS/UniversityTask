import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data Tabel
file_path = 'CarPrice_Assignment.csv'
df = pd.read_csv(file_path)
df

# melihat isi tipedata tiap atribut
data_types = df.dtypes
data_types

# Heatmap
int_float_columns = df.select_dtypes(include=['int64', 'float64'])

correlation_matrix = int_float_columns.corr()

plt.figure(figsize=(10, 6))

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar=True)

plt.title('Heatmap Korelasi Antar Atribut Bertipe int dan floatn/')
plt.show()

# Pembersihan Data
# Menghapus Data yang Kotor

# 1.Cek data apakah ada yang null

null_columns = df.columns[df.isnull().any()]

if len(null_columns) > 0:
    print("Kolom yang memiliki nilai null:")
    for column in null_columns:
        print(f"- {column}")
else:
    print("Tidak ada kolom yang memiliki nilai null.")


# Pembersihan Data
# Menghapus Data yang Kotor

# 2. Outliers -------------------------------------------------------
#     2.1 cek outliers

column = 'price'  # Kolom yang ingin dicek outliers

# Fungsi untuk mendeteksi outliers menggunakan metode IQR
def detect_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identifikasi outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers


# Mendeteksi outliers pada kolom 'price'
outliers_price = detect_outliers('price')
print("Outliers pada 'price':")
outliers_price.head()

# Mendeteksi outliers pada kolom 'enginesize'
outliers_enginesize = detect_outliers('enginesize')
print("\nOutliers pada 'enginesize':")
outliers_enginesize.head()

# Pembersihan Data
# Menghapus Data yang Kotor

# 2. Outliers ------------------------------------------------------------------
#     2.2 hapus outliers

# Fungsi untuk mendeteksi dan menghapus outliers menggunakan metode IQR karena Data tidak terlalu terpengaruh oleh outliers besar, karena IQR tidak sensitif terhadap nilai ekstrim
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter untuk menghapus outliers
    df_filtered = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    print(f"Outliers dihapus dari kolom '{column}'.")
    return df_filtered

# Menghapus outliers dari kolom 'price'
df_no_outliers_price = remove_outliers(df, 'price')

# Menghapus outliers dari kolom 'enginesize'
df_inliers = remove_outliers(df_no_outliers_price, 'enginesize')

# Menampilkan hasil setelah menghapus outliers
print("\nData setelah menghapus outliers pada 'price' dan 'enginesize':")
df_inliers.head()


# Normalisasi / Transformasi Data
# Mengnormalisasikan data inlinier

# 3. Standar Devisiasi (Z-score) karena Skala yang Konsisten -------------------
#     - Mean
#     - Variance
#     - Standar Devisiasi

# Fungsi untuk standardisasi
def standardize_column(column):
    mean = column.mean()
    std_dev = column.std()
    return (column - mean) / std_dev


# Menerapkan standardisasi pada kolom 'Price' dan 'EngineSize'
df_inliers['Price_Standardized'] = standardize_column(df_inliers['price'])
df_inliers['EngineSize_Standardized'] = standardize_column(df_inliers['enginesize'])

# Menampilkan DataFrame setelah standardisasi
df_inliers.head()


if 'EngineSize_Standardized' in df_inliers.columns and 'Price_Standardized' in df_inliers.columns:
    # 1. Membuat interaksi antara EngineSize dan Price
    df_inliers['EnginePrice_Interaction'] = df_inliers['EngineSize_Standardized'] * df_inliers['Price_Standardized']
    
    # 2. Menghitung rasio antara EngineSize dan Price
    df_inliers['EnginePrice_Ratio'] = df_inliers['EngineSize_Standardized'] / (df_inliers['Price_Standardized'] + 1e-5)  # Menghindari pembagian dengan nol
    
    # 3. Menampilkan beberapa baris teratas dari DataFrame setelah feature engineering
    print(df_inliers[['EngineSize_Standardized', 'Price_Standardized', 'EnginePrice_Interaction', 'EnginePrice_Ratio']].head())
else:
    print("Kolom 'EngineSize_Standardized' dan 'Price_Standardized' tidak ditemukan dalam DataFrame.")
