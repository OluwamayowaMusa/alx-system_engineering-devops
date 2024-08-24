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
    headers = {"User-Agent": "Musa"}
    response = requests.get(request_url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", None)
    posts.pop(0)
    [print(post.get("data").get("title")) for post in posts]
