#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import sys


if __name__ == '__main__':
    usr = sys.argv[1]
    pswd = sys.argv[2]
    req = requests.get("https://api.github.com/user",
                       auth=(usr, pswd))
    dict_from_git = req.json()
    print(dict_from_git.get("id"))
