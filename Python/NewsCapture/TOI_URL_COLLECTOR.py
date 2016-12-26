# This program will scrape the data from Times of India and will save the final output in URL.txt file
import requests
from bs4 import BeautifulSoup
import sys,os
import re

class TOI_URL_COLLECTOR():
    # URL from where the data needs to be scraped
    toi_url='http://timesofindia.indiatimes.com/2016/1/3/archivelist/year-2016,month-1,starttime-42372.cms'

    def URLCollector(url,file_name):
        r=requests.get(toi_url)
        soup = BeautifulSoup(r.content,'lxml')
        # Intermediate file to save the HTML data
        fname = "URL_DATA_INTERMEDIATE.out"

        # Get the data from tag table
        g_data = soup.find_all("table")    
        newsall =(g_data[1].contents[1])
    
        newslist=[]
        for t in newsall:
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

        urls=[]
        with open(fname,'r') as filex:
            for line in filex:
                p = re.compile("<a href=(.*?)>")
                gr=p.search(line)
                links=(gr.group(0))
                urls.append((links.replace("<a href=\"","")).replace("\">",""))
        

        # Save the output file url.txt in data folder
        targetFileName=file_name
        targetFolder=os.getcwd()
        # If the folder Does not exist it will be created
        if os.path.exists(os.path.join( targetFolder,'data')):
            urlfile = os.path.join( targetFolder,'data',targetFileName)
        else:
            os.makedirs(os.path.join( targetFolder,'data'))
            urlfile = os.path.join( targetFolder,'data',targetFileName)

        finalFile = open(urlfile, 'a')
        for item in urls:
            finalFile.write("%s\n" % item)
        
    
        # Deleting the Intermediate file
        os.remove(fname)
    


#URLCollector(toi_url,'urls.csv')



