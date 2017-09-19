#!/usr/bin/python
""" export to csv """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users?id={}".format(url, uid)).json()
    todos = requests.get("{}/todos?userId={}".format(url, uid)).json()

    with open('{}.csv'.format(uid), "w", newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([uid,
                            users[0].get("username"),
                            i.get("completed"),
                            i.get("title")])
