# pip install requests
import requests
import json
 
url = 'https://api.foursquare.com/v2/users/self/checkins?limit=250&oauth_token={}&v=20131026&offset={}'
 
# Visit https://developer.foursquare.com/docs/explore to generate an OAuth token. Paste that token below.
oauth_token = "5QCFUOK2COFUI1P2QTUPPLB2Q3DD5ZU0RTKCRYLWMGKWPGEW&v=20160805"
offset = 0
data = []
 
with open("/tmp/checkins.json", 'w') as f:
  while True:
    response = requests.get(url.format(oauth_token, offset))
    if len(response.json()['response']['checkins']['items']) == 0:
      break
    data.append(response.json())
    offset += 250
  f.write(json.dumps(data))
