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
