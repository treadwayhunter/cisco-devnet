"""
When doing these labs, I make a few of my own edits into the code.
The lab has me recreating some of the same functions repeatedly, so
I take time to make it more modular. There is plenty of room for more
modularization, but I do not feel it necessary.
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from dnac_config import *
from get_auth_token import get_auth_token

urllib3.disable_warnings()

def get_commands(token, host=DNAC_IP, port=DNAC_PORT):
    url = f"https://{host}:{port}/api/v1/network-device-poller/cli/legit-reads"
    headers = {
        "X-Auth-Token": token
        }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    print("Exec commands supported:")
    print(json.dumps(response.json()['response'], indent=4))

if __name__ == '__main__':
    token = get_auth_token()
    get_commands(token)