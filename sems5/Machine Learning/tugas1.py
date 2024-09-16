import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('healthcare-dataset-stroke-data.csv')

data_info = data.info()
data_head = data.head()


# data_info
# print('\n')
# data_head

# ----------------------------------------------------

duplicates = data.duplicated().sum()
data_cleaned = data.drop_duplicates()

# print(f"Jumlah duplikat yang dihapus: {duplicates}")
# print('\n')

# print(data_cleaned.head())

#  ----------------------------------------------------

# membuat grafiknya terlebih dahulu
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
sns.boxplot(y=data['age'])
plt.title('Boxplot for Age')

plt.subplot(1, 3, 2)
sns.boxplot(y=data['avg_glucose_level'])
plt.title('Boxplot for Avg Glucose Level')

plt.subplot(1, 3, 3)
sns.boxplot(y=data['bmi'])
plt.title('Boxplot for BMI')

# plt.tight_layout()
# plt.show()

#  ---------------------------------------------------

Q1 = data[['age', 'avg_glucose_level', 'bmi']].quantile(0.25)
Q3 = data[['age', 'avg_glucose_level', 'bmi']].quantile(0.75)
IQR = Q3 - Q1

# Define outliers as any data point outside 1.5 * IQR
outliers = ((data[['age', 'avg_glucose_level', 'bmi']] < (Q1 - 1.5 * IQR)) |
            (data[['age', 'avg_glucose_level', 'bmi']] > (Q3 + 1.5 * IQR))).any(axis=1)

outliers_jumlah = outliers.sum()
data_dibersihkan = data[~outliers]

#  ---------------------------------------------------

# print(f"\nJumlah outlier yang dihapus: {outliers_jumlah}")
# print('\n')
# print("Data setelah menghapus outlier:")
# print(data_dibersihkan.head())

#  ---------------------------------------------------

sebelum = data_cleaned.isnull().sum()
data_cleaned['bmi'].fillna(data_cleaned['bmi'].median(), inplace=True)
setelah = data_cleaned.isnull().sum()

# print(f"\nMissing values sebelum: {sebelum['bmi']}")
# print('\n')
# print(f"Missing values setelah: {setelah['bmi']}")
# print('\n')
# print("Data setelah menangani missing values:")
# print(data_cleaned.head())

#  ---------------------------------------------------

hanyaSatuNilai = [col for col in data_cleaned.columns if data_cleaned[col].nunique() == 1]
databersih = data_cleaned.drop(columns=hanyaSatuNilai)

# print(f"\nKolom dengan satu nilai unik yang dihapus: {hanyaSatuNilai}")
# print('\n')
# print("Data setelah menghapus kolom dengan satu nilai:")
# print(databersih.head())

#  ---------------------------------------------------

non_representative_columns = ['id']

data_cleaned = data_cleaned.drop(columns=non_representative_columns)

# print(f"\nKolom yang tidak representatif yang dihapus: {non_representative_columns}")
# print('\n')
# print("Data setelah menghapus kolom yang tidak representatif:")
# print(data_cleaned.head())
