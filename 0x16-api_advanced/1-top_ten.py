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
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                             AppleWebKit/537.36 (KHTML, like Gecko)\
                             Chrome/50.0.2661.102 Safari/537.36"}
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
