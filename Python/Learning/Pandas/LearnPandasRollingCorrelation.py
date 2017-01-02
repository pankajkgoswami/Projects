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
 
HPI_Data = pd.read_pickle('fiddy_states_n.pickle')

TX_AK_Corr = pd.rolling_corr(HPI_Data['TX'],HPI_Data['AK'],12) 

HPI_Data['TX'].plot(ax=ax1,label='TX HPI')
HPI_Data['AK'].plot(ax=ax1,label='AK HPI')

TX_AK_Corr.plot(ax=ax2,label='TX_AK_Corr')

plt.legend(loc=4)
plt.show()
