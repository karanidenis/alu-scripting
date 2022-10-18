#!/usr/bin/python3

"""
module that returns number of subscribers from Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = requests.get.utils.default_headers()
    headers.update({'user-Agent': 'My User Agent 1.0'})

    get_subs = requests.get(api_url, headers=headers).json()
    subs = get_subs.get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
