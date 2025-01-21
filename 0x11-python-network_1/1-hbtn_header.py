#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value of
the X-Request-Id variable found in the header of the response.
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    with request.urlopen(url) as response:
        headers = response.headers
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)

