import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv('market_basket_2.csv')

# Mengisi nilai NaN dengan 0
data_filled = data.fillna(0)

data_bool = data_filled.astype(bool)

# Menghitung support count untuk setiap item (C1)
C1 = data_bool.sum().reset_index()
C1.columns = ['item', 'support']

# Menghitung total jumlah transaksi
total_transaksi = len(data_bool)

# Menetapkan minimum support count berdasarkan min_support = 0.02 (2%)
min_support_count = 0.02 * total_transaksi

# Membuat L1 dengan filter support count yang memenuhi syarat minimum support
L1 = C1[C1['support'] >= min_support_count]

# Menjalankan algoritma Apriori untuk menemukan frequent itemsets
# Akan menghitung L2, L3, dst. secara otomatis
frequent_itemsets = apriori(data_bool, min_support=0.02, use_colnames=True)
