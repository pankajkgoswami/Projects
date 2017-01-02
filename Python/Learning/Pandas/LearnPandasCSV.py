import pandas as pd

df=pd.read_csv('ZILL-Z95126_LPC.csv',index_col=0)

# Renames the Columns
df.columns=['San Diego HPI']

#df.set_index('Date', inplace=True)
print(df.head())

# To save Dataframe in CSV . If no header is requierd header=False
df.to_csv('NewCsv1.csv',header=False)

df1=pd.read_csv('NewCsv1.csv',names=['Date','SD HPI'],index_col=0)
print(df1.head(5))

df1.to_json('new.json')