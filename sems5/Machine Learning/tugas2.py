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
