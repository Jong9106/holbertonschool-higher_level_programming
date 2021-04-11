#!/bin/bash
# script that takes in a URL as an argument, sends a GET
curl -so /dev/null -w "%{http_code}" "$1"
