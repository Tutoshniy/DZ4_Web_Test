import requests
import yaml
import logging

with open('./logpass.yaml') as f:
    testdata = yaml.safe_load(f)
address = testdata["post_addr"]


def getpost(token):
    try:
        data = requests.get(address, params={'owner': 'notMe'}, headers={'X-Auth-Token': token})
    except:
        logging.exception("Problem with getpost")
        return None
    return [i['title'] for i in data.json()['data']]


def get_post_description(token):
    try:
        data = requests.get(address, params={}, headers={'X-Auth-Token': token})
    except:
        logging.exception("Problem with get_post_description")
        return None
    return [i['description'] for i in data.json()['data']]


def create_post(token, title, description, content):
    try:
        data = requests.post(address, params={'title': title, 'description': description, 'content': content},
                             headers={'X-Auth-Token': token})
    except:
        logging.exception("Problem with create_post")
    return description
