import http.client, urllib.request, urllib.parse, urllib.error, base64
import MasterData
import json

file_name='Bing_News.json'
out_file=open(file_name,'w')

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': MasterData.Ocp_Apim_Subscription_Key,
}

# Category of news saved in a parameter
news_category='India'

params = urllib.parse.urlencode({
    # Request parameters
    'Category': news_category,
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/news/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    #json_data = json.loads(data)
    out_file.write(data.text)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
