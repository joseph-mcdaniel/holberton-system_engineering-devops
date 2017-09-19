#!/usr/bin/python3
""" Gather data from REST API """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users?id={}".format(url, sys.argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(url, sys.argv[1])).json()
    tasks = 0

    for i in range(len(todos)):
        if (todos[i].get("completed")):
            tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(users[0].get("name"),
                                                          tasks,
                                                          len(todos)))
    for j in todos:
        if j["completed"]:
            print("\t {}".format(j.get("title")))
