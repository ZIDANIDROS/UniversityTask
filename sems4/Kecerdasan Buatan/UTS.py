from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

df = pd.read_excel('data_KB.xlsx')
#print(df)

df.isnull().sum()

df.shape

df.info()

sns.countplot(x='Class',data=df)
