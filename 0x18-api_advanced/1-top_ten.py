#!/usr/bin/python3
"""
top_ten reddit API
"""
import requests


def top_ten(subreddit):
    """
    return top ten hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "Tommy Wiseau"}

    response = requests.get(url, headers=headers).json()
    data = response.get('data')
    if data is None:
        print(None)
    else:
        children = data.get('children')
        for child in children:
            print(child.get('data').get('title'))
