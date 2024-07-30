#!/usr/bin/python3
""" Access an API for a given employee ID and returns information
    about his/her TODO list progress.
"""
from urllib import request
import sys
import json


def gather_data_from_api(base_url, employee_id):
    """ Access the url and retrieve information about the
        employee TODO list

    Args:
        url (str): API URL
        employee_id (int): ID of employee
    """
    employee_response = query_url(base_url, f"users/{employee_id}")
    employee_name = employee_response["name"]

    total_todos = query_url(base_url, f"todos?userId={employee_id}")
    completed_todos = query_url(base_url,
                                f"todos?userId={employee_id}&completed=true")

    print(f"Employee {employee_name} is done"
          f" with tasks {len(completed_todos)}/{len(total_todos)}")

    for todos in completed_todos:
        print(f"\t {todos['title']}")


def query_url(base_url, path):
    """ Query the complete url (base URL and path)
        and return the response.

    Args:
        base_url (str): Base URL of the API
        path (str): Path of the data required

    Returns:
        Deserialized body
    """
    request_url = request.urljoin(base_url, path)
    with request.urlopen(request_url) as response:
        body = json.load(response)

    return body


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) != 2:
        print("Not the right format. \
                Format ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    id_ = int(sys.argv[1])
    gather_data_from_api(URL, id_)
