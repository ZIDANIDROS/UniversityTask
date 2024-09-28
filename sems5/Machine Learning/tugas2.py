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
