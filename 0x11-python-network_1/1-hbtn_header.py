#!/usr/bin/python3
"""
Module that takes a URL, sends a request and displays a value
of the X-Reques-Id
"""
import urllib.request
from sys import argv


def main():
    """ Method that sends request and prints value """
    html = urllib.request.Request(argv[1])
    with urllib.request.urlopen(html) as response:
        h = response.getheaders()
        for x in h:
            if 'X-Request-Id' in x:
                print(x[1])

if __name__ == '__main__':
    main()
