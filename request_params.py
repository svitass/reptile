# 爬取百度页面
import requests

# response = requests.get("https://www.baidu.com/")  # 生成一个response对象
# response.encoding = response.apparent_encoding  # 设置编码格式
# print("状态码："+str(response.status_code)) # 打印状态码
# print(response.text) # 输出爬取的信息

'''
常见的HTTP状态码
(1) 200 请求成功
(2) 301 资源(网页等)被永久转移到其他URL（3** 重定向，需要进一步的操作以完成请求）
(3) 404 请求的资源（网页等）不存在
(4) 500 内部服务器错误
'''

# get传参1： 多个参数间用&连接
# response = requests.get("http://httpbin.org/get?name=hezhi&age=20") # get传参


# get传参2: params用字典传多个参数
data = {
    "name":"hezhi",
    "age":20
}
# response = requests.get("http://httpbin.org/get",params=data)

# post传参
response = requests.post("http://httpbin.org/post",params=data)

print( response.status_code ) #状态码
print( response.text )

