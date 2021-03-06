#!/usr/bin/python3
""" Module that takes in a URL and sends a POST """
import requests
from sys import argv


def main():
    """ Method that takes URL and sends POST """
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.content.decode())

if __name__ == '__main__':
    main()
