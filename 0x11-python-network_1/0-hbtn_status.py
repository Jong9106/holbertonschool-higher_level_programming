#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    h = type(html)
    print("Body response:")
    print("    - type: {}".format(h))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode()))
