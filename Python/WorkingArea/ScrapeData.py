# This program will scrape the data from Times of India and will save the final output in URL.txt file
import requests
from bs4 import BeautifulSoup

# URL from where the data needs to be scraped
toi_url='http://timesofindia.indiatimes.com/2016/1/3/archivelist/year-2016,month-1,starttime-42372.cms'

r=requests.get(toi_url)
soup=BeautifulSoup(r.text,"lxml")

Newslist=[]

for tablerow in soup.select('.cnt tr'):
    table_cells = tablerow.findAll('td')
    print(table_cells)
    
    if len(table_cells) > 0:
        relative_link_table_det = table_cells[0].find('a')['href']
        print(relative_link_table_det)



#print(soup.prettify())

