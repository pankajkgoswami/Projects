import Python.Keys as Keys
import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


pickle_in = open('fiddy_states_n.pickle','rb')
HPI_data = pickle.load(pickle_in)

HPI_data.plot()
plt.legend().remove()
plt.show()
