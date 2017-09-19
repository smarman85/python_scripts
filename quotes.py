import requests
import json

url = "http://quotes.rest/qod.json"
resp = requests.get(url)
data = resp.json()
print data["contents"]["quotes"][0]['quote']
