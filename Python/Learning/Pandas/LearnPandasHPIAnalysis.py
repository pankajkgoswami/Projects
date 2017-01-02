import Python.Keys as Keys
import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

API_key=Keys.Quandl_Key

# df=quandl.get('FMAC/HPI_AK',authtoken=API_key)
# print(df.head(10))

# Gets all the table contents from an HTML Page
def states_list():
    fifty_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1:]


# Prints the first table
#print(fifty_states[0])

# Prints first column of the table
#print(fifty_states[0][0])

def grab_initial_state_data():
    states = states_list()
    main_df=pd.DataFrame()

    for abbv in states:
        query=('FMAC/HPI_'+str(abbv))
        df = quandl.get(query,authtoken=API_key)
        df.rename(columns={'Value':str(abbv)}, inplace=True)
        # The line below will calculate the percentage change
        df[abbv] = (df[abbv]-df[abbv][0])/df[abbv][0] * 100.0
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    pickle_out = open('fiddy_states_n.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()
        

#grab_initial_state_data()
 
# pickle_in = open('fiddy_states_n.pickle','rb')
# HPI_data = pickle.load(pickle_in)
# print(HPI_data)
    

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA',authtoken=API_key)
    df.rename(columns={'Value':str("United States")}, inplace=True)
    # The line below will calculate the percentage change
    df["United States"] = (df["United States"]-df["United States"][0])/df["United States"][0] * 100.0
    return df


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
# 
# 
HPI_Data = pd.read_pickle('fiddy_states_n.pickle')
# benchmark = HPI_Benchmark()
# 
TX1yr = HPI_Data['TX'].resample('A')

HPI_Data['TX'].plot(ax=ax1,label='Monthly TX HPI')
TX1yr.plot(ax=ax1,label='Yearly TX HPI')
# benchmark.plot(ax=ax1,color='k',linewidth=10)

#plt.legend().remove()
plt.show()

# HPI_States_correlation = HPI_Data.corr()
# print(HPI_States_correlation)
