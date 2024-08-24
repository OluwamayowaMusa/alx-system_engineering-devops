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
    response = requests.get(request_url).json()
    return response.get("data", {}).get("subscribers", 0)
