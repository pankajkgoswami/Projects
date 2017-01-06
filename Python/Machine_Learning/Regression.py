import pandas as pd
import quandl,math,datetime
import Python.Keys as Keys
import numpy as np
import pickle
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

API_key=Keys.Quandl_Key
df = quandl.get('WIKI/GOOGL',authtoken=API_key)
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
# High to Low Percentage
df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low'] * 100
# Percentage Change
df['PCT_Change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100

df =df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

df.fillna(-99999,inplace=True)
forecast_col = 'Adj. Close'
forecase_out = int(math.ceil(0.1*len(df)))

# Using Shift keyword will shift the data and will show the future data
df['label']=df[forecast_col].shift(-forecase_out)

X=np.array(df.drop(['label'],1))

X=preprocessing.scale(X)
X_lately = X[-forecase_out:]
X = X[:-forecase_out]


df.dropna(inplace=True)
y=np.array(df['label'])

X_Train,X_Test,y_Train,y_Test= cross_validation.train_test_split(X,y,test_size=0.2)

# For Linear Regression
clf=LinearRegression()

# For SVM Regression
#clf=svm.SVR(kernel='poly')


clf.fit(X_Train,y_Train)

with open('linearregression.pickle','wb') as f:
    pickle.dump(clf,f) 

pickle_in1 = open('linearregression.pickle','rb')

clf=pickle.load(pickle_in1)

accuracy = clf.score(X_Test,y_Test)

# print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set,accuracy,forecase_out)

df['Forecast']=np.nan

last_date=df.iloc[-1].name
last_unix = last_date.timestamp()
one_day=86400
next_unix=last_unix+one_day

for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()









