#!/usr/bin/python3
"""A script that:
- take a URL and an email address
- sends a POST request to the passed URL with email as parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
