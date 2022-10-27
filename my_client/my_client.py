import requests

BASEURL = "https://httpbin.org/anything"
URL = "https://httpbin.org/status/200"
LOCAL = "http://localhost:8000/"

get_response = requests.get(LOCAL, json={"query": "hello"})

print(get_response.text)
