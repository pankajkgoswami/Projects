# This program will generate the list of URL's for each of the day from Times of India Archive and save it 
# as CSV file for consumption by next program
import os
import datetime
import csv

urllist=[]
d1 = datetime.date(2001, 1, 1)
site_name='http://timesofindia.indiatimes.com'
starttime=36892
#today =datetime.date(2001, 1, 20)
today = datetime.date.today()
dateval=[]

# To Get the values of Year Month and Day from datetime

# The while loop will generate the links for each day since 2001 to current day and append it
# in the list urllist
while(True):
    link=site_name+"/"+str(d1.year)+"/"+str(d1.month)+"/"+str(d1.day)+"/"+"archivelist"+"/year-"+str(d1.year)+",month-"+str(d1.month)+",starttime-"+str(starttime)+".cms"
    urllist.append(link)
    dateval.append(str(d1.year)+str(d1.month).zfill(2)+str(d1.day).zfill(2))
    d1=d1 + datetime.timedelta(days=1)
    starttime=starttime+1
    if d1 > today:
        break


targetFileName='url_list.csv'
targetFolder=os.getcwd()
# If the folder Does not exist it will be created
if os.path.exists(os.path.join( targetFolder,'data')):
    csvfilex = os.path.join( targetFolder,'data',targetFileName)
else:
    os.makedirs(os.path.join( targetFolder,'data'))
    csvfilex = os.path.join( targetFolder,'data',targetFileName)

# Saving the output in CSV File with Year_Month_day and URL Header
with open(csvfilex,'w',newline='') as csvfile:
    fieldnames=['Year_Month_Day','URL'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(urllist)):
        writer.writerow({'Year_Month_Day': dateval[i], 'URL': urllist[i]})


