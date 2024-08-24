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
    request_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(request_url).json()

    return response.get("data", {}).get("subscribers", 0)
