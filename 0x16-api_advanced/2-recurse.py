#!/usr/bin/python3
""" Queries Reddit API"""
import requests


def recurse(subreddit, hotlist=[], after="", count=0):
    """ Get the list of hot articles in a given subreddit

    Args:
        subreddit(str): Given Subreddit

    Returns:
        List of articles
    """
    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "count": count, "limit": 100}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                             AppleWebKit/537.36 (KHTML, like Gecko)\
                             Chrome/50.0.2661.102 Safari/537.36"}
    response = requests.get(request_url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return 200

    response = response.json()
    after = response.get("data").get("after")
    count += response.get("data").get("dist")

    for article in response.get("data").get("children"):
        hotlist.append(article.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hotlist, after, count)

    return hotlist
