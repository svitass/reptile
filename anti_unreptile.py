# 绕过反爬机制 以知乎为例
import requests
response = requests.get("http://www.zhihu.com")  # 访问知乎，不设置头部信息
print("不设置头部信息，状态码："+str(response.status_code)) # 状态码：403 Forbidden
# 设置头部信息，伪装浏览器
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
response = requests.get("http://www.zhihu.com",headers=headers)
print(response.status_code)
print(response.text)