import os,re 

targetFolder=os.getcwd()
input_file_name=os.path.join( targetFolder,'data','urllist_1.txt')
urls=[]
with open(input_file_name,encoding="utf8") as fn:
    for line in fn:
        p = re.search(r"<a href=(.*?)/comment", line)
        links=(p.group())
        #urls.append((links.replace("<a href=\"","")).replace("\">",""))
        print(links)
    #content = fn.read().replace("<br/><a href=","\n<br/><a href=")
    #print(content)
    
for i in range(len(urls)):
    print(urls[i])
fn.close()