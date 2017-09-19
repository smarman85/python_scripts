import json
import requests

response = requests.get("https://api.github.com/users/smarman85")
json_data = json.loads(response.text)
print json_data
print json_data['public_repos']

def repo_names(url):
    repo_resp = requests.get("%s" % url)
    info = json.loads(repo_resp.text)
    for line in info:
        print line['full_name']
    
def followers(url):
    follow_resp = requests.get("%s" % url)
    info = json.loads(follow_resp.text)
    for line in info:
        print line['login']


repos = json_data['repos_url']
followers_url = json_data['followers_url']
repo_names(repos)
followers(followers_url)
