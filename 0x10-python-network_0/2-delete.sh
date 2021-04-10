#!/bin/bash
# script that takes in a URL, sends a DELETE
curl -sX "DELETE" "$1"
