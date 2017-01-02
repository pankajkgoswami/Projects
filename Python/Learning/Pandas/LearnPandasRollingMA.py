import Python.Keys as Keys
import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

API_key=Keys.Quandl_Key

fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)
 
# 
HPI_Data = pd.read_pickle('fiddy_states_n.pickle')
# 
HPI_Data['TX12MA'] = pd.rolling_mean(HPI_Data['TX'],12) 
HPI_Data['TX12STD'] = pd.rolling_std(HPI_Data['TX'],12)

print(HPI_Data[['TX','TX12MA','TX12STD']].head())

HPI_Data[['TX','TX12MA']].plot(ax=ax1)
HPI_Data['TX12STD'].plot(ax=ax2)

plt.legend(loc=4)
plt.show()
