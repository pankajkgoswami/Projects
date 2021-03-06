# This program will scrape the data from Times of India and will save the final output in URL.txt file
import requests
from bs4 import BeautifulSoup
import sys,os
import re

def generateFile(url):
    # URL from where the data needs to be scraped
    toi_url='http://timesofindia.indiatimes.com/2016/1/3/archivelist/year-2016,month-1,starttime-42372.cms'
    r=requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')

    # Intermediate file to save the HTML data
    fname = "URL_DATA_INTERMEDIATE.out"

    # Get the data from tag table
    g_data = soup.find_all("table")    
    newsall =(g_data[1].contents[1])

    newslist=[]
    for t in newsall:
        #print(t) 
        newslist.append(t)

    # Saves the output generated from last step in file
    f = open(fname, 'w')
    sys.stdout = f
    print(newslist[2])

    # Extracts the data generated in last step into lines, for each link
    newcontent=[]
    with open(fname) as fn:
        content = fn.read().replace("<br/><a href=","\n<br/><a href=")
        print(content)
    f.close()

    # The steps below will remove the first line. Though this is memory intensive step as 
    # the entire contents of the file are saves in the memory
    with open(fname, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fname, 'w') as fout:
        fout.writelines(data[1:])

    # Deleting the Intermediate file
    #os.remove(fname)

#new_url='http://timesofindia.indiatimes.com/2016/1/3/archivelist/year-2016,month-1,starttime-42372.cms'
urllist=["http://timesofindia.indiatimes.com//2003/10/2/archivelist/year-2003,month-10,starttime-37896.cms"]

for new_url in urllist:
    generateFile(new_url)