# 爬取视频
import sys
import re,os
import requests
from you_get import common as you_get
from lxml import etree
import subprocess
from moviepy.editor import *
from glob import glob
import shutil
from selenium import webdriver
from pyquery import PyQuery as pq
import datetime
from time import sleep


path = './data/videos'
days = [31,28,31,30,31,30,31,31,30,31,30,31]
# cur_year = datetime.datetime.now().year
# cur_month = datetime.datetime.now().month
# cur_day = datetime.datetime.now().day
cur_year = 2021
cur_month = 6
cur_day = 25


def getVideo(html):
    # res = requests.get(url,headers=headers)  # 获取网站信息
    # res.encoding = 'utf-8'
    # 获取视频的url
    # html = etree.HTML(res.text)
    html = etree.HTML(html)
    urls = html.xpath('//div[@class="right_con01"]/ul/li/a/@href')  # 使用相对路径
    video_url = urls[0]  # 视频地址
    print('video_url:',video_url)  # 获取了视频的地址
    # 创建一个临时文件夹，用于保存该视频的所有子视频
    video_save = os.path.join(path,'temp')
    if os.path.exists(video_save):  # 要确保该目录下是空的
        shutil.rmtree(video_save)
    os.mkdir(video_save)
    # 开始下载视频
    try:
        sys.argv = ['you_get','-o',video_save,video_url]
        you_get.main() # 开始下载
    except:
        pass


# 将下载的小视频合成一个大视频
def combineVideo():
    print(os.path.join(path,'temp/*.mp4'))
    filelist = glob(os.path.join(path,'temp/*.mp4'))
    video_name = filelist[0].split('\\')[2] # 获取video name
    video_name = video_name.split('[')[0]
    filelist.sort()  # 根据文件名对视频排序
    print("filelist:", filelist)
    print('video_name:',video_name)
    video = []
    for file in filelist:
        clip = VideoFileClip(file)
        video.append(clip)
    # 视频拼接
    new_video = concatenate_videoclips(video)
    # 输出到文件
    new_video.write_videofile(path+"/"+video_name+".mp4")



if __name__ == '__main__':
    url = 'https://tv.cctv.com/lm/xwlb/?spm=C94212.P4YnMod9m2uD.EfOoEZcMXuiv.1'
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54',
    #     'cookie': 'BIDUPSID=517516CBF0261FA0AF6B039EAFEDF39C; PSTM=1589624436; BAIDUID=517516CBF0261FA090A0395C8BF0F31A:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PC_TAB_LOG=haokan_website_page; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1592530622,1592545903; H_PS_PSSID=31906_1444_31671_21118_31254_32045_30823_32111; delPer=0; PSINO=2; yjs_js_security_passport=d270bf2526b634428ea81932e213c285b8e7cf21_1592546748_js; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1592550475; reptileData=%7B%22data%22%3A%22e3b78a008f54876b4fc19fe55faea5fb1ae054d9580474b00db252837ba6a6554cbfde0ada4567b9cad2322c5d972031cb300664e248e8f4a7b27fd91a479f4e02a1e7eceffa642289eba12075334687515e1451aa72eced7ac42e3fbb88a87139c95727da119f5dd9b85d281d98d4d98b943f43a06c3f13e6b63b812c5c40ce%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%2243b164d6%22%7D'
    # }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    # 创建Chrome浏览器对象，在电脑上打开一个浏览器窗口
    browser = webdriver.Chrome()
    browser.get(url) # 进入相关网站
    html = browser.page_source  # 获取网站源码
    # print("html:",html)
    # data = str(pq(html)) # pq(html) 解析网页源码
    day_num = cur_day-1
    month = browser.find_element_by_class_name("nr_left")  # 点击上个月按钮
    month.click()
    month = browser.find_element_by_class_name("nr_left")  # 点击上个月按钮
    month.click() # 从6月开始
    count = 0
    while cur_year > 0:
        while cur_month > 0:
            while day_num > 0:
                # 点击year-month-day str(day_num)
                element = browser.find_element_by_xpath("//td[not(@class='otherday')]/a[text()='"+str(day_num)+"']")
                element.click()
                # print("element:",element.text)
                # 根据日历不断重定向到新的页面，改变url的值
                html = browser.page_source
                getVideo(html)
                combineVideo()
                count = count+1
                if count >= 100:
                    exit(0)
                # element.click()
                sleep(3)
                day_num = day_num - 1
            cur_month = cur_month - 1
            month = browser.find_element_by_class_name("nr_left") # 点击上个月按钮
            month.click()
            day_num = days[cur_month - 1]
        cur_year = cur_year - 1
        cur_month = 12
