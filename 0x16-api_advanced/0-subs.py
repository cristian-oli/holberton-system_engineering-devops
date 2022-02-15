#!/bin/usr/python3
"""
Module for number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit
    API and returns the number of
    subscribers
    """
    try:
        user_agent = {'User-agent': 'Mozilla/5.0'}
        resp = requests.get(
            'https://www.reddit.com/r/' + subreddit
            + '/about.json', headers=user_agent
            )
        if resp.status_code == 200:
            data = resp.json()
            return data.get('data').get('subscribers')
        return 0
    except Exception:
        return 0