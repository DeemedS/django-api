import requests

#endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "hello world", "method": "GET"})

print(get_response.json())
print(get_response.status_code)


