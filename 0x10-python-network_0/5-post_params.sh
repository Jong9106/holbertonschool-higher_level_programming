#!/bin/bash
# script that takes in a URL as an argument, sends a GET
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
