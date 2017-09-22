#!/usr/bin/python3
"""
show sub count
"""
import requests


def number_of_subscribers(subreddit):
    """
    return subcount of subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Tommy Wiseau"}

    response = requests.get(url, headers=headers).json()
    data = response.get('data')
    if data is None:
        return 0
    else:
        subcount = data.get('subscribers')
    return subcount
