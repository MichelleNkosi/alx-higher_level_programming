#!/usr/bin/python3
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")

