import json
import requests

#url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=KID_LIFE_CRISIS"
data = requests.get("http://api.twitter.com/1/statuses/user_timeline.json?screen_name=meltingpies")
print(data.status_code)
