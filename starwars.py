import requests
import pprint
import json
from requests.auth import HTTPBasicAuth

search = input("What can I help you with today Master? ")

def api_call(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()

def spec_info(data):
    pprint.pprint(data)

def ships(data):
    pprint.pprint(data)

def name(data):
    pprint.pprint(data['name'])

def ship_info(data):
    pprint.pprint(data)

def gather_info(data):
    char_name = name(data)
    homeworld = name(api_call(data['homeworld']))
    ships = ship_info(api_call(data['starships']))

if search != "":
    url = "https://swapi.co/api/{0}/".format(search)
    data = api_call(url)
    gather_info(data)
