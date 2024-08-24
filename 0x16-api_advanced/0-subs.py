#!/usr/bin/python3
"""Queries the reddit API """
import requests


def number_of_subscribers(subreddit):
    """
        Get the number of subscribers for a given subreddit


    Args:
        subreddit(str): Given subreddit

    Returns: Number of subscribers
    """
    request_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(request_url)

    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
