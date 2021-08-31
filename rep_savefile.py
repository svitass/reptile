# 爬取一个html并保存
import requests

url = "http://www.baidu.com"
response = requests.get(url)
response.encoding = "utf-8" # 设置接收编码格式
print("类型：",str(type(response)))
print("状态码：",response.status_code)
print("头部信息:",response.headers)
print("响应内容:\n",response.text)

# 保存文件
path = "./data/baidu.html"
file = open(path,"w",encoding="utf")
file.write(response.text)
file.close()

# 爬取图片到本地
response = requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif") # get方法得到图片响应
file = open("./data/baidu_logo.gif","wb") # 用二进制格式写入文件
print("res content:",response.content)
file.write(response.content)
file.close()
