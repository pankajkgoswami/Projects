import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors


df = pd.read_csv('breast-cancer-wisconsin.data')
#Replacing the missing data with -99999
df.replace('?',-99999,inplace=True)
# Dropping the id as it does not solve any purpose
df.drop(['cid'],1,inplace=True)

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])
X_Train,X_Test,y_Train,y_Test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=neighbors.KNeighborsClassifier()
clf.fit(X_Train,y_Train)

accuracy=clf.score(X_Test,y_Test)

print(accuracy)
