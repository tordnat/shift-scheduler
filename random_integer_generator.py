"""
Random Integer Array Generator

This module provides functions to interact with the random.org API for fetching random integers within specified ranges.
It includes functionality to request random numbers, check the remaining quota for requests, and handle various HTTP responses.
The module is designed to enforce a maximum number of integers per request and gracefully handle request failures.

Dependencies: requests
Author: Tord Natlandsmyr
Version: 1.0
"""

import requests
from typing import List

def generate_random_integer_array(number : int, min_val : int, max_val : int) -> List[int]:
    """
    Fetches a specified number (up to 10,000) of random integers within a range from random.org.

    :param number: The number of random integers to fetch.
    :param min_val: The minimum integer value in the range.
    :param max_val: The maximum integer value in the range.
    :type number: int
    :type min_val: int
    :type max_val: int
    :return: A list of random integers. Returns an empty list if the request fails.
    :rtype: List[int]
    """
    url_request = f"https://www.random.org/integers/?num={number}&min={min_val}&max={max_val}&col=1&base=10&format=plain&rnd=new"
    if number > 10000:
        print("Error: number > 10000")
        return []
    try:
        http_response = requests.get(url_request)
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return []
    
    if handle_http_response(http_response) is None:
        quota = get_random_integer_quota()
        print(f"Random number quota is {quota}")
        return [] #Return empty list

    numbers = http_response.text.split('\n') # Random number response is '\n' separated in cleartext
    return [int(x) for x in numbers if x] #Convert the split strings to integers and create a new list

    
def get_random_integer_quota() -> int:
    """
    Fetches the remaining quota for random number requests from random.org.

    :return: Remaining quota as an integer, or None if the request fails.
    :rtype: int or None
    """
    url_quota   = "https://www.random.org/quota/?format=plain"
    
    try:
        http_response = requests.get(url_quota)
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    
    if handle_http_response(http_response) is not None:
        return int(http_response.text)

    return None

def handle_http_response(response) -> requests.Response:
    """
    Handles different HTTP status codes for a given response.

    :param response: The HTTP response to be handled.
    :type response: requests.Response
    :return: The original response if status is OK, None otherwise.
    :rtype: requests.Response or None
    """
    if response.status_code == 200:
        return response
    elif response.status_code in (304, 404, 503): # Other specific status code.
        print(response.text)
    else:
        print(f"Unhandeled HTTP response status code: {response.status_code}")
    return None