import requests
from agents import function_tool


@function_tool
def fetch_user_data() -> list:
    """Fetch function for user data and return list"""
    print("Data fetch")
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    return res.json()
    
# print(fetch_user_data())

@function_tool
def fetch_user_data_by_id(id:int) -> list:
    """Fetch function for user data and return list"""
    print("Data fetch by id")
    url = f"https://jsonplaceholder.typicode.com/users{id}"
    res = requests.get(url)
    return res.json()
    
