import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from matplotlib import style
style.use('ggplot')


df = pd.read_csv("Dataset_Bank.csv")

# dropping V2 - Number of houses as it has no correlation on the Target

df.drop(['V2'],axis=1,inplace=True)

# To check grouping of a particular column's relation
#print(df.groupby(['V10','Target']).size())

#sns.factorplot('Target',col='V10',kind='count', data=df[df.V10.notnull()],size=4,aspect=3)

X=np.array(df.drop(['Target'],1))

X=preprocessing.scale(X)
y=np.array(df['Target'])

X_Train,X_Test,y_Train,y_Test= cross_validation.train_test_split(X,y,test_size=0.1)

random_forest = RandomForestClassifier(n_estimators=100)

random_forest.fit(X_Train, y_Train)

accuracy = random_forest.score(X_Train, y_Train)

print(accuracy)

#plt.show()
# print(df1.head(6))

# Get the counts of each value for a column
# print(df['V1'].value_counts())