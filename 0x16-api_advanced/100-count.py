#!/usr/bin/python3
""" Queries Reddit API """
import requests


def count_words(subreddit, word_list, after="", count=0, store={}):
    """ Print a sorted count of keywords in titles

    Args:
        subreddit(str): Given subreddit
        word_list(list): List of keywords

    """
    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "count": count}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                             AppleWebKit/537.36 (KHTML, like Gecko)\
                             Chrome/50.0.2661.102 Safari/537.36"}
    response = requests.get(request_url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    response = response.json().get("data")
    after = response.get("after")
    count = response.get("dist")

    word_list = list(map(str.lower, word_list))
    store = store_words_count(word_list, response.get("children"), store)

    if after is not None:
        count_words(subreddit, word_list, after, count, store)
        return
    print_in_correct_format(store)


def store_words_count(word_list, titles_list, store):
    """Store the words count in a dict <key>: <count>

    Args:
        word_list(list): list of words
        titles_list(list): list of titles
        store(dict): Collection of words and count

    Return:
        Collection of words and count
    """

    for title in titles_list:
        for word in word_list:
            count = title.get("data"). \
                    get("title").lower().split(' ').count(word)

            if word in store:
                store[word] += count
            elif count != 0:
                store[word] = count

    return store


def print_in_correct_format(store):
    """ Print the words and count in the correct format

    Args:
        store(dict): Dictionary count of words
    """
    words = list(store.keys())
    count = list(store.values())

    print_list = []

    while len(count) > 0 and len(words) > 0:
        max_count = max(count)
        index_max = count.index(max_count)
        word = words[index_max]

        word_count = WordCount(word, max_count)
        print_list = WordCount.insert_in_list(print_list, word_count)
        count.remove(max_count)
        words.remove(word)

    for word_count in print_list:
        print("{}: {}".format(word_count.word, word_count.count))


class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    @staticmethod
    def insert_in_list(word_count_list, new_word_count):
        for index, word_count in enumerate(word_count_list):
            if new_word_count.count > word_count.count:
                word_count_list.insert(0, new_word_count)
                break
            elif new_word_count.count == word_count.count:
                if new_word_count.word > word_count.word:
                    word_count_list.insert(index + 1, new_word_count)
                    break

        else:
            word_count_list.append(new_word_count)

        return word_count_list
