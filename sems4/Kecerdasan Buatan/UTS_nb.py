from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

df = pd.read_excel('data_KB.xlsx')
#print(df)

df.isnull().sum()

df.shape

df.info()

sns.countplot(x='Class',data=df)

df["Selected"].hist()

df["Class"].hist()

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
sns.histplot(df, ax=axes[0], x="Area", kde=True, color='r')
sns.histplot(df, ax=axes[1], x="AspectRation", kde=True, color='b')
sns.histplot(df, ax=axes[2], x="Perimeter", kde=True)

le = LabelEncoder()
df['Selected_Numerik'] = le.fit_transform(df['Selected'])

#print(df['Selected'].unique())

#print(df['Class'].unique())

X = df.drop(['Class', 'Selected'], axis=1,)
y = df['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=4)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#print("Accuracy:", accuracy_score(y_test, y_pred))
#print(classification_report(y_test, y_pred))

#Decision Tree

model = tree.DecisionTreeClassifier()
model.fit(x, y)

model.score(x, y)

plt.figure(figsize=(120, 80))
plot_tree(model, filled=True, feature_names=df.columns, class_names=model.classes_)
#plt.show()
