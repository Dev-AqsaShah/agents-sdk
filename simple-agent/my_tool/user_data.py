import requests
from agents import function_tool


@function_tool
def fetch_user_data() -> list:
    """Fetch function for user data and return list"""
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    return res.json()
    
# print(fetch_user_data())