#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first ten hot posts in a subreddit
    Args:
        subreddit(str): Given subreddit
    """
    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(request_url, params, allow_redirects=False).json()
    posts = response.get("data", {}).get("children", None)
    if posts is None:
        print(None)
    else:
        posts.pop(0)
        for post in posts:
            print(post.get("data").get("title"))
