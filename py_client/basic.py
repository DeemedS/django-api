import requests

#endpoint = "http://httpbin.org/status/200"
#endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "hello world", "method": "GET"})

print(get_response.json()["message"])
#print(get_response.status_code)


