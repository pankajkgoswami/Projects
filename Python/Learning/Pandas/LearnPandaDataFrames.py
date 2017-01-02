import pandas as pd
import numpy as np

web_data = {'Days':[1,2,3,4,5,6],'Visitors':[20,32,23,44,43,22],'Bounce_Rate':[65,56,77,34,66,72]}
df =pd.DataFrame(web_data)

#Prints all the data
#print(df)

# Prints the number of records from top . Default is 5
#print(df.head(3))

# Prints the number of records from bottom . Default is 5
#print(df.tail(3))

df.set_index('Days',inplace=True)
# TO print one element
#print(df['Visitors'])
#print(df.Visitors)

#To print multiple elements
#print(df[['Visitors','Bounce_Rate']])

print(df.Visitors.tolist())

# To convert lists within lists we need to use numpy

print(np.array(df[['Visitors','Bounce_Rate']]))