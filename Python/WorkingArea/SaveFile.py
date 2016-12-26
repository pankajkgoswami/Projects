import re

urls=[]
with open("test.out",'r') as filex:
    for line in filex:
        next(filex)
        p = re.compile("<a href=(.*?)>")
        gr=p.search(line)
        links=(gr.group(0))
        urls.append((links.replace("<a href=\"","")).replace("\">",""))
        #print(links)

for i in range(len(urls)):
    print(urls[i])


thefile = open('urls.txt', 'w')
for item in urls:
    thefile.write("%s\n" % item)

