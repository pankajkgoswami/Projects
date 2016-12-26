import csv,os
from NewsCapture.TOI_URL_COLLECTOR import TOI_URL_COLLECTOR

targetFolder=os.getcwd()
file_name=os.path.join( targetFolder,'data','url_list.csv')

def getData(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            date_ =row[0]
            url = row[1]
            fname=(date_[0:4]+".csv")
            #print(fname,url)
            URLCollector(url,fname)
            
    return

#URLCollector(toi_url,'urls.csv')

getData(file_name)