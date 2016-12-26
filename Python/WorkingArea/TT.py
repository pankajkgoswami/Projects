import newspaper
#livemint = newspaper.build('http://timesofindia.indiatimes.com/')
TOI= newspaper.build('http://www.thehindu.com/news/national/')

for article in TOI.articles:
    print(article.url)