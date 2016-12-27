# This program will collect the News data from Bing and will save it in a file
import requests
import json
Ocp_Apim_Subscription_Key ='e29bd984ac1b4029881a8d4a36713466'
def bing_search(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    # query string parameters
    payload = {'q': query}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key}
    # make GET request
    r = requests.get(url, params=payload, headers=headers)
    # get JSON response
    return r.json()
 
j = bing_search('TCS')
print(j.get('webPages', {}).get('value', {}))


with open('TCS.txt', 'w') as f:
    json.dump(j, f, ensure_ascii=False)