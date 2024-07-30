#!/usr/bin/python3
""" Access an API for a given employee ID and returns information
    about his/her TODO list progress.
"""
import json
import sys
from urllib import request


def export_all_employees(base_url):
    """ Save all the todos of all the employees

    Args:
        base_url (str): Base URL of the API
    """
    all_employees = {}
    employees_response = query_url(base_url, "users")

    for employee in employees_response:
        employee_id = employee["id"]
        all_employees[employee_id] = []
        employee_username = employee["username"]

        employee_todo = query_url(base_url, f"todos?userId={employee_id}")
        for todo in employee_todo:
            all_employees[employee_id].append(
                    {"username": f"{employee_username}",
                     "task": todo["title"],
                     "completed": todo["completed"]})

    with open("todo_all_employees.json", 'w', encoding="utf8") as jsonfile:
        json.dump(all_employees, jsonfile)


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
    if len(sys.argv) != 1:
        print("Not the right format. \
                Format ./3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    export_all_employees(URL)
