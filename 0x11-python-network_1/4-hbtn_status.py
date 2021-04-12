#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = requests.get('https://intranet.hbtn.io/status')
    rsp = url.text
    print('Body response:')
    print('\t- type: {}'.format(type(rsp)))
    print('\t- content: {}'.format(rsp))
