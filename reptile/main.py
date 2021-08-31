import requests
import os

# 思路：you-get下载，然后再合成
# MP4文件无法播放？
if __name__=="__main__":
    for i in range(270):
        url = "https://hls.cntv.baishancdnx.cn/asp/hls/1200/0303000a/3/default/46c6c76d679340d5bb1df3a87573c952/"+str(i+1)+".mp4"

        root = "data/videos/"
        path = root +str(i+1) +".mp4"              #抓取文件起的名字
        try:
            if not os.path.exists(root):
                os.mkdir(root)                  #如果该目录不存在就创建它
            if not os.path.exists(path):
                r = requests.get(url)           #获取到目标视频的所有信息
                with open(path, 'wb') as f:     #以二进制写的方式将r的二进制内容写入path
                    f.write(r.content)
                    f.close()
                    print("文件"+path+" 保存成功!")
            else:
                print("文件已存在")
        except:
            print("爬取失败")
