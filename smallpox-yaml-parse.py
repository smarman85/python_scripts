import os
import json
import yaml
import time
import requests
from glob import glob
from pprint import pprint
from socket import gethostbyname

home = os.environ['HOME']
source_dir = "{0}/Documents/repos/configuration-management/ansible/group_vars/".format(home)
files = glob(source_dir + "*-sandbox")

def print_shit(shortcode, filename, curlid, url):
    with open("bought_the_farm.yaml", "a") as outfile:
        outfile.write("{0} {1} {2} {3}\n".format(shortcode, filename, curlid, url))

def run_curl(url):
    full_url = "https://{0}-dev.{name}.com/v3/ping".format(url)
    resp = requests.get(full_url)
    return resp.json()['id']

def curl_check(payload):
    try:
        curl_server = run_curl(payload['partner_name'])
        if payload["partner"] not in curl_server:
            print_shit(payload['partner'], payload["shortname_db"], curl_server, payload['partner_name'])
    except Exception:
        print("{0} error".format(payload['partner_name']))
    except UnboundLocalError:
        print("{0} may not be a host".format(payload['partner_name']))
    except NameError as exc:
        print("name error")

def  read_yaml(filename):
    with open(filename, "r") as stream:
        try:
            payload = yaml.load(stream)
            curl_check(payload)
        except yaml.YAMLError as exc:
            print(exc)
        except KeyError as exc:
            print("{0} can't find partner name".format(filename))

for file in files:
    filename = file.split('/')[-1]
    if ( filename.startswith('zion')
            or 'hsm' in filename
            or 'dna' in filename
            or 'diva' in filename
            or 'cert' in filename
            or 'mongo' in filename
            or 'widgets' in filename
            or 'tungsten' in filename
            or 'webhooks' in filename
            or filename.startswith('old')
            or 'pre-migration' in filename
       ):
       pass
    else:
        read_yaml(file)
