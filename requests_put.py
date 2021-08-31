import requests
response = requests.put("http://httpbin.org/put")
print(response.status_code)
print(response.text)