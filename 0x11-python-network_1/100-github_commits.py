#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
"""


from requests import get
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    repo_owner = sys.argv[2]
    req = get("https://api.github.com/repos/{}/{}/commits"
              .format(repo_owner, repo))
    json_response = req.json()

    counter = 0

    if json_response:
        for i in range(0, len(json_response)):
            if counter < 10:
                sha = json_response[i].get("sha")
                author = json_response[i].get(
                    "commit").get("author").get("name")
                print("{}: {}".format(sha, author))
                counter += 1
