# 爬取百度贴吧图片  urllib+re
import urllib  # Python内置的HTTP请求库
import urllib.request
import re  # 正则表达式

# 根据url获取网页html内容
def getHtmlContent(url):
    page = urllib.request.urlopen(url) # 最基本的页面抓取
    html = page.read()
    html = html.decode('utf-8')
    return html

'''
从html中解析出所有jpg图片的url
百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
'''
def getJPGs(html):
    # 解析jpg图片url的正则表达式
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width') # width 提高匹配精度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg,html)
    return jpgs

# 用图片url下载图片并保存成指定文件名
def downloadJPG(imgUrl,fileName):
    urllib.request.urlretrieve(imgUrl,fileName)

# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls,path = './data/imgs/'):
    count = 1
    for url in imgUrls:
        downloadJPG(url,''.join([path,'{0}.jpg'.format(count)]))
        count = count + 1

# 封装: 从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    print("html",html)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)

if __name__ == "__main__":
    main()