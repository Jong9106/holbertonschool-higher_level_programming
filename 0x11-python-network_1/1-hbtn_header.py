#!/usr/bin/python3
"""
Python script that print https://intranet.hbtn.io/status
"""

import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as urlresponse:
        id_rsp = urlresponse.info()['X-Request-Id']
        print(id_rsp)
