#!/usr/bin/env python
# import requests
import time
import requests
from requests.auth import HTTPBasicAuth
import re
import os
from utils import *
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed

baseUri = "https://api.github.com/repos/"
# client_id = ""
# client_secret = ""


def read_uri_from_file():
    filepath = "{}/repositories".format(os.getcwd())
    # f = open(filepath, 'r')
    urire = re.compile(r'\(https:\/\/github\.com\/(.*?)\)')
    uri_list = []
    with open(filepath, 'r') as f:
        for line in urire.findall(f.read()):
            # print(line)
            uri_list.append(line)
    return uri_list


result_list = []
fail_list = []


def spider_data(path, client_id, client_secret):
    uri = baseUri + path
    r = requests.get(uri, auth=HTTPBasicAuth(client_id, client_secret))
    # print(r.request.headers)
    if r.status_code == requests.codes.ok:
        result = r.json()
        return {
            "name": result.get("name"),
            "star": result.get("stargazers_count"),
            "uri": result.get("html_url")
        }, True
    else:
        print("\nError:\t{}".format(uri))
        return uri, False


def main():
    t1 = time.time()
    import_env()
    client_id = os.environ["client_id"]
    client_secret = os.environ["client_secret"]
    # print("{}:{}".format(client_id, client_secret))
    uris = read_uri_from_file()
    i = 0
    l = len(uris)
    printProgress(i, l, barLength=50)

    # for uri in read_uri_from_file():
    #     i += 1
    #     value, success = spider_data(uri)
    #     if success:
    #         result_list.append(value)
    #     else:
    #         fail_list.append(value)
    #     printProgress(i, l, barLength=50)

    # thread
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_tasks = [executor.submit(spider_data, url, client_id, client_secret)
                        for url in uris]
        for future in as_completed(future_tasks):
            value, success = future.result()
            i += 1
            if success:
                result_list.append(value)
            else:
                fail_list.append(value)
            printProgress(i, l, barLength=50)
    # wait(future_tasks, return_when=ALL_COMPLETED)
    t2 = time.time()
    print('Cost Time: {0:.2f}s'.format(t2-t1))
    result_list.sort(key=lambda x: x["star"], reverse=True)
    print("Success: {}\n".format(len(result_list)))
    for item in result_list:
        print("\t%s: %s\t%s" % (
            item["name"], item["star"], item["uri"]))

    print("\nFail: {}\n".format(len(fail_list)))
    for item in fail_list:
        print("\t%s" % (item))


if __name__ == "__main__":
    main()
