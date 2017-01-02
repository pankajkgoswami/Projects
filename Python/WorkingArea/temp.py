import pandas as pd

url='http://economictimes.indiatimes.com/archivelist/year-2002,month-1,starttime-37257.cms'

def states_list():
    fifty_states=pd.read_html('http://economictimes.indiatimes.com/archivelist/year-2002,month-1,starttime-37257.cms')
    print(fifty_states[0])