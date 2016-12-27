import requests
from bs4 import BeautifulSoup
import sys,os,csv
import re

targetFolder=os.getcwd()
input_file_name=os.path.join( targetFolder,'data','url_list.csv')
Error_File_Name=os.path.join( targetFolder,'data','Erroneous_links_list.csv')

def errorFile(url,error_fname):
    with open(error_fname, 'a') as err_fname:
        err_fname.writelines(url)
        err_fname.write('\n')
    err_fname.close()

def URLCollector(url,out_file_name,error_fname):
    # URL from where the data needs to be scraped
    r=requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
 
    # Intermediate file to save the HTML data
    int_fname = "URL_DATA_INTERMEDIATE.out"

    # Get the data from tag table
    g_data = soup.find_all("table")    
    newsall =(g_data[1].contents[1])

    newslist=[]
    for t in newsall:
        #print(t) 
        newslist.append(t)

    # Saves the output generated from last step in file
    f = open(int_fname, 'w')
    sys.stdout = f
    print(newslist[2].encode("utf-8"))

    # Extracts the data generated in last step into lines, for each link
    newcontent=[]
    with open(int_fname) as fn:
        content = fn.read().replace("<br/><a href=","\n<br/><a href=")
        print(content)
    f.close()

    # The steps below will remove the first line. Though this is memory intensive step as 
    # the entire contents of the file are saves in the memory
    with open(int_fname, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(int_fname, 'w') as fout:
        fout.writelines(data[1:])

    urls=[]
    with open(int_fname,'r') as filex:
        for line in filex:
            p = re.search(r"<a href=(.*?)>", line)
            if p:
                links=(p.group())
                urls.append((links.replace("<a href=\"","")).replace("\">",""))
            else:
                errorFile(url,error_fname)
 
    # Save the output file in data folder
    urlfile = out_file_name

    finalFile = open(urlfile, 'a')
    for item in urls:
        finalFile.write("%s\n" % item)

    # Deleting the Intermediate file
    os.remove(int_fname)

def getData(filename,Error_File_Name):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.DictReader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            date_ =row['Year_Month_Day']
            #print(date_)
            url = row['URL']
            fname=(date_[0:4]+".csv")
            #print(fname,url)
            URLCollector(url,fname,Error_File_Name)
            
    return

#URLCollector(url,input_file_name,Error_File_Name)

getData(input_file_name,Error_File_Name)