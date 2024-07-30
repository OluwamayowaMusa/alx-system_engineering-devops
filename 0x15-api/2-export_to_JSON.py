#!/usr/bin/python3
""" Access an API for a given employee ID and returns information
    about his/her TODO list progress.
"""
import json
import sys
from urllib import request


def export_to_json(data):
    """ Save data in json format

    Args:
        data (list): List of dict containing info about userId, username
                     task_title
    """
    employee_info = data["EmployeeInfo"]
    todo_list = data["TodosData"]

    employee_dict = {f"{employee_info['id']}": []}

    for todo in todo_list:
        employee_dict[f"{employee_info['id']}"].append(
                {"task": todo["title"],
                 "completed": todo["completed"],
                 "username": employee_info["username"]})

    with open(f"{employee_info['id']}.json", 'w', encoding="utf8") as jsonfile:
        json.dump(employee_dict, jsonfile)


def gather_data_from_api(base_url, employee_id):
    """ Access the url and retrieve information about the
        employee TODO list

    Args:
        url (str): API URL
        employee_id (int): ID of employee

    Returns:
        Dictionary containing Info about employee and
        todos
    """
    employee_response = query_url(base_url, f"users/{employee_id}")
    total_todos = query_url(base_url, f"todos?userId={employee_id}")

    data = {"EmployeeInfo": employee_response, "TodosData": total_todos}

    return data


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
    employee_data = gather_data_from_api(URL, id_)
    export_to_json(employee_data)
