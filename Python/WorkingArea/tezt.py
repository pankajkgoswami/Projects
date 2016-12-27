import os
import re

targetFileName='curated.txt'
targetFolder=os.getcwd()
# If the folder Does not exist it will be created
if os.path.exists(os.path.join( targetFolder,'data')):
    urlfile = os.path.join( targetFolder,'data',targetFileName)
else:
    os.makedirs(os.path.join( targetFolder,'data'))
    urlfile = os.path.join( targetFolder,'data',targetFileName)

fname='URL_DATA_INTERMEDIATE.out'

urls=[]

with open(fname,'r') as filex:
    for line in filex:
        match=re.search(r"<a href=(.*?)>", line)
        #p = re.compile(r"<a href=(.*?)>")
        if match:
            urls.append((match.group().replace("<a href=\"","")).replace("\">",""))
        else:
            continue
            
        #gr=p.search(line)
        #links=(gr.group(0))
        

print(urls)
