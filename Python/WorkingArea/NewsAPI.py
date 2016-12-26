import urllib.request
import requests


#f=urllib.request.urlopen("https://newsapi.org/v1/sources?language=en")
r = requests.get("https://newsapi.org/v1/sources?language=en")
type(r)
print(r.text)
#text=f.read()
#print(text)
with open('News_APIData.txt', 'w') as outfile:
    outfile.write(r.text)