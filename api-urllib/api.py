from urllib.request import Request, urlopen
import os
import json
from pprint import pprint

req = Request('https://github.{{ company }}.com/api/v3/repos/{{ company }}/{{ repo_nam }}/commits/{{ commit }}')
req.add_header('Authorization', "token {0}".format(os.environ['AUTH_KEY']))
data = urlopen(req).read()
jdata = json.loads(data)
pprint(jdata['files'])
