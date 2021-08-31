import requests
response_get = requests.get("http://httpbin.org/get")  # https://www.baidu.com/
print("状态码：",response_get.status_code)
print(response_get.text)

response_post = requests.post("http://httpbin.org/post")  # 获得的信息相比于get()更多一点
print("状态码：",response_post.status_code)
print(response_post.text)
