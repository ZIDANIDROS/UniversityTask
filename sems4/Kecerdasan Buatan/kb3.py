from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv('/content/drive/MyDrive/placement.csv')
print(df)

df.isnull().sum()

df.shape

df.info()

import seaborn as sns
sns.countplot(x='status',data=df)

import seaborn as sns
sns.countplot(x='status',hue='gender',data=df)