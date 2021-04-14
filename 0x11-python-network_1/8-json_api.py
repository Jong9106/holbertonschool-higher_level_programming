#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    q = ""

    if len(argv) > 1:
        q = argv[1]

    data = {'q': q}

    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        json = response.json()
        if not json:
            print('No result')
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print('Not a valid JSON')
