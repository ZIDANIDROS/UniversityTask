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

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------