import json
import urllib.request
urlData = "https://api.github.com/users/smarman85"
webUrl = urllib.request.urlopen(urlData)
#print(webUrl) # <http.client.HTTPResponse object at 0x101f8f278>
data = webUrl.read() # datat is bytes at this moment, still needs to be decoded
encoding = webUrl.info().get_content_charset('utf-8')
jdata = json.loads(data.decode(encoding))
# print(jdata) # json dump
# print(type(jdata)) # show type of dump, dict
print(jdata['name'])
