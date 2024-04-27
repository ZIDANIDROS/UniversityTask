import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#-------------------------------------

df.isnull().sum()

#-------------------------------------

df.info()

#-------------------------------------

import seaborn as sns
sns.countplot(x='status',data=df)

#-------------------------------------

le=LabelEncoder()
df['sl_no_n']=le.fit_transform(df['sl_no'])
df['gender_n']=le.fit_transform(df['gender'])
df['ssc_p_n']=le.fit_transform(df['ssc_p'])
df['ssc_b_n']=le.fit_transform(df['ssc_b'])
df['hsc_p_n']=le.fit_transform(df['hsc_p'])
df['hsc_b_n']=le.fit_transform(df['hsc_b'])
df['hsc_s_n']=le.fit_transform(df['hsc_s'])
df['degree_p_n']=le.fit_transform(df['degree_p'])
df['degree_t_n']=le.fit_transform(df['degree_t'])
df['workex_n']=le.fit_transform(df['workex'])
df['etest_p_n']=le.fit_transform(df['etest_p'])
df['specialisation_n']=le.fit_transform(df['specialisation'])
df['mba_p_n']=le.fit_transform(df['mba_p'])
df['status_n']=le.fit_transform(df['status'])

#-------------------------------------

df.drop(['sl_no','sl_no_n','gender','ssc_p','hsc_p','hsc_b', 'ssc_b', 'hsc_s', 'degree_p', 'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p', 'status'], axis=1, inplace=True)
df

#-------------------------------------

X = df.iloc[:, :12].values
y = df.iloc[:, 12].values

#-------------------------------------

X

#-------------------------------------

y

#-------------------------------------

X_train, X_test, y_train, y_test= train_test_split(X, y , test_size=0.3, random_state=4)

#-------------------------------------

from sklearn.preprocessing import StandardScaler

#-------------------------------------
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#-------------------------------------

from sklearn.naive_bayes import GaussianNB

#-------------------------------------

# Mengubah X_test menjadi bentuk yang diharapkan
# Ubah X_test menjadi bentuk yang diharapkan oleh model Gaussian Naive Bayes dengan menggunakan reshape(-1, 1).
# 1. Gunakan model untuk melakukan prediksi pada X_test_reshaped.
# 2. Buat DataFrame yang berisi nilai aktual (y_test) dan nilai prediksi (y_pred).
# 3. X_test_reshaped = X_test.values.reshape(-1, 1)
X_test_reshaped = X_test.values.reshape(-1, 1)

# Melakukan prediksi menggunakan model
y_pred = model.predict(X_test_reshaped)

# Membuat DataFrame untuk membandingkan nilai aktual dan prediksi
df1 = pd.DataFrame({'Actual Status': y_test, 'Predicted Status': y_pred})

#-------------------------------------

df1

#-------------------------------------

print(classification_report(y_test, y_pred))

#-------------------------------------

print(confusion_matrix(y_test, y_pred))

#-------------------------------------

print(accuracy_score(y_test, y_pred)*100)
