#!/usr/bin/python3
"""
Module for recurse function
"""
import json
import requests


def recurse(subreddit, hot_list=[], idx=0, response=None, aftr=''):
    """
    Queries the Reddit API and returns a
    list containing the titles of all hot
    articles for a given subreddit. If no
    results are found for the given
    subreddit,the function should return None
    """
    if idx == 0:
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = 'https://www.reddit.com/r/{}/hot.json{}'.format(subreddit, aftr)
        response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code == 200:
        info = response.json()
        if info.get('error', 200) == 404:
            return None
        if idx >= len(info.get('data').get('children')):
            if info['data']['after'] is not None:
                aftr = '?after=' + info.get('data').get('after')
                idx = 0
                return recurse(subreddit, hot_list, idx, response, aftr)
            else:
                return hot_list
        hot_list.append(
            info.get('data').get('children')[idx].get('data').get('title')
            )
        idx += 1
        return recurse(subreddit, hot_list, idx, response, aftr)
    return None
