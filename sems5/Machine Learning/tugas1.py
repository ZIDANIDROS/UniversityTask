import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('healthcare-dataset-stroke-data.csv')

data_info = data.info()
data_head = data.head()


data_info
print('\n')
data_head