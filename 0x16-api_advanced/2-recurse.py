#!/usr/bin/python3
""" Queries Reddit API"""
import requests


def recurse(subreddit, hotlist=[]):
    """ Get the list of hot articles in a given subreddit

    Args:
        subreddit(str): Given Subreddit

    Returns:
        List of articles
    """

    request_url = "https://www.reddit.com/r/{}/hot".format(subreddit)

