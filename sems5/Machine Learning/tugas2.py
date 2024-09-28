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
