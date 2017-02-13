import requests
from bs4 import BeautifulSoup

def URLExtract(url):
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(page.content, 'html.parser')
    g_data=soup.find_all('a')
    for i in range(37,66,3):
        newsall =(g_data[i])
        print(newsall)


urllist=['http://www.aiotestking.com/cloudera/category/exam-cca-505-cloudera-certified-administrator-for-apache-hadoop-ccah-cdh5-upgrade-exam/page/5/'
]

for url in urllist:
    URLExtract(url)
    