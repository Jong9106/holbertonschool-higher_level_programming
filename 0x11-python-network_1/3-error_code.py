#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as urlresponse:
            print(urlresponse.read().decode('utf8'))

    except HTTPError as e:
        print('Error code:', e.code)
