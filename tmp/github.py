import requests
import json
import re # imprts regex

username = 'smarman85'
url      = 'https://api.github.com'

class User(object):
    origin_site = 'github'

    def __init__(self, name, repo_url, repo_numbers, avatar, created):
        self.name = name
        self.repo_url = repo_url
        self.repo_numbers = repo_numbers
        self.avatar = avatar
        self.created = created

    def info_dump(self):
        string = "%s has %s repos which can be found at %s. %s has been active since %s. This information comes from: %s." 
        return string % (self.name, self.repo_numbers, self.repo_url, self.name, self.created, self.origin_site)

    def show_repos(self):
        repos = requests.get(self.repo_url).json()
        for i in range(1, len(repos)):
            # account for null in description with "None"
            if str(repos[i]['description']) != "None":
                print repos[i]['name'] + " : " + repos[i]['description']
            else:
                print repos[i]['name'] + " : " + "No Description"

def human_readable(date):
    regex = re.search(r'(\d{4}-\d{2}-\d{2})', date)
    return regex.group()

def filter(data):
    name = data['name']
    url  = data['repos_url']
    repo = data['public_repos']
    avatar = data['avatar_url']
    created = human_readable(data['created_at'])
    new_users = User(name, url, repo, avatar, created)
    print new_users.info_dump()
    print new_users.show_repos()

def get_api_info(url, user):
    # with auth
    # call = requests.get("%s/users/%s" % (url, user), auth=('smarman85', 'PASSWORD'))
    call = requests.get("%s/users/%s" % (url, user)).json()
    filter(call)


print get_api_info(url, username)
