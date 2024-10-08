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
