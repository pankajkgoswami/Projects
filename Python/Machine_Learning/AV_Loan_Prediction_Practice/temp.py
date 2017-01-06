import pandas as pd
import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
from boto.mws.connection import dependent
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing,cross_validation

# get train & test csv files as a DataFrame
df_train = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
df_test = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')

# Dropping Loan Id as it's not useful in analysis and prediction
df_train.drop(['Loan_ID'],axis=1,inplace=True)

print(df_train.groupby(['Credit_History']).size())

df_train.info()