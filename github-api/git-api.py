import requests
import json

base_url = "https://api.github.com"
#me = requests.get(url)
#print me.json()

def api_call(url):
    print url
    resp = requests.get(url)
    data = resp.json()
    return data
    #return data[field]

# get user base info:
def userinfo(username):
    page = api_call(base_url + "/users/%s" % (username))

def repos(username):
    page = api_call(base_url + "/users/%s/repos" % (username))
    for info in page:
        print "***************************"
        print info['name']
        print info['url']
        print info['language']

#data = userinfo("smarman85")
rep = repos("smarman85")
