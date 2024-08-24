#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first ten hot posts in a subreddit

    Args:
        subreddit(str): Given subreddit

    """
    request_url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    response = requests.get(request_url).json()
    posts = response.get("data", {}).get("children", None)

    if posts is None:
        print(None)
    else:
        for post in posts:
            print(post.get("data").get("title"))
