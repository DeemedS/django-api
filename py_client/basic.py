import requests

#endpoint = "http://httpbin.org/status/200"
#endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"abc": "cba"}, json={"query": "hello world"})

#print(get_response.text)
#print(get_response.status_code)

#print(get_response.json()["message"])
print(get_response.json())



