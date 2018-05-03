import json
import urllib.request
import os

urlData = urllib.request.Request('https://github.{{ company }}.com/api/v3/repos/{{ company }}/{{ repo_name }}/commits/{{ commit }}')
urlData.add_header('Authorization', "token {0}".format(os.environ['AUTH_KEY']))
req = urllib.request.urlopen(urlData).read()
jdata = json.loads(req)
print(jdata)
