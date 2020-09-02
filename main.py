#!/usr/bin/env python
import requests
import re
import os


def read_uri_from_file():
    filepath = "{}/repositories".format(os.getcwd())
    # f = open(filepath, 'r')
    urire = re.compile(r'\((https:\/\/github.*?)\)')
    uri_list = []
    with open(filepath, 'r') as f:
        for line in urire.findall(f.read()):
            # print(line)
            uri_list.append(line)
    return uri_list


def spider_data(uri):
    r = requests.get(uri)
    print("{} -> {}".format(uri, r.status_code))
    print(r.json())



def main():
    uris = read_uri_from_file()
    spider_data("https://api.github.com/repos/ratiw/vuetable-2")
    # for uri in read_uri_from_file():
    #     spider_data(uri)


if __name__ == "__main__":
    main()
