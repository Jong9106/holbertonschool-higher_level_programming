#!/bin/bash
# script that sends a request and display status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
