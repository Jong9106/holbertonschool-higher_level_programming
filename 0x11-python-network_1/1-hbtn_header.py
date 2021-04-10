#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as urlresponse:
    id_rsp = urlresponse.info()['X-Request-Id']
    print(id_rsp)
