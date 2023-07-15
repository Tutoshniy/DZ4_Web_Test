import pytest
import requests
import yaml
import logging

with open("logpass.yaml") as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['pass']
addr = data['addr']


@pytest.fixture()
def login():
    try:
        r = requests.post(addr, data={'username': name, 'password': passwd})
    except:
        logging.exception("Problem with login")
        return None
    return r.json()['token']


