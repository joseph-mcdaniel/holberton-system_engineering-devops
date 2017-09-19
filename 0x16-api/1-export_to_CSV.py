#!/usr/bin/python
""" export to csv """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users?id={}".format(url, sys.argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(url, sys.argv[1])).json()

    with open('{}.csv'.format(sys.argv[1]), "w", newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([sys.argv[1],
                            users[0].get("username"),
                            i.get("completed"),
                            i.get("title")])
