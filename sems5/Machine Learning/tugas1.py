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