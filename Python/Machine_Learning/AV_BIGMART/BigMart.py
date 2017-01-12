import pandas as pd
import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
from boto.mws.connection import dependent
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing,cross_validation

# get train & test csv files as a DataFrame

df_train = pd.read_csv('Train_UWu5bXk.csv')
df_test = pd.read_csv('Test_u94Q5KV.csv')


#print(df_train.groupby(['Gender']).size())

df_train.info()