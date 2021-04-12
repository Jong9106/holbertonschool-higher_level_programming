#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    rsp = requests.get(url)
    id_rsp = rsp.headers.get('x-Request-Id')
    print(id_rsp)
