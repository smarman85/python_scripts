import requests
from requests.auth import HTTPBasicAuth
import os
import json
from pprint import pprint

commits = ["0d4ff85e0fbec35f9e8e188807c2ebcad902afe7", "c2284980f416619bf40568214e671ce7892cd5cd"]

endpoint = "https://github.{{ company }}.com/api/v3/repos/{{ company }}/{{ repo_name }}/commits/"
auth_key = os.environ['AUTH_KEY']

def api_call(url, commit):
    resp = requests.get(url + commit, headers={'Authorization': 'token {0}'.format(auth_key)})
    return resp.json()['files']

def save_output(hostname):
    with open('removed-hosts.yml', 'a') as outputfile:
        outputfile.write("{0}\n".format(hostname))

def file_name_only(path_file):
    save_output(path_file.split('/')[-1])

def get_filename(payload):
    for file in payload:
        if file['status'] == 'removed':
            if 'host_vars' in file['filename']:
                file_name_only(file['filename'])

for commit in commits:
    files = api_call(endpoint, commit)
    get_filename(files)
