# 使用you-get下载视频
#Autor: 房廷飞
#Data:  2019.2.11

import requests
import os
global a
import time
a=0

def downts(path,url,i):
    global a
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        response=requests.get(url,headers=header,timeout=5)
        if response.status_code==200:
            ret=response.content
            with open(path+'/%03d.ts'%i,'wb')as f:
                f.write(ret)
                print(url+'下载完成！')
        else:
            print(url)
            print(response.status_code)
            a=a+1
            if a==3:                                 #连续三次连接不到资源地址，说明所有小ts文件都已经下载完，结束程序。
                exit('预计已结束，程序自动退出')
    except Exception as e:
        print(e)
        
def main(URL):
    path="C:/Users/user/Desktop/python测试/2"         #下载地址
    for i in range(10000):                           #设置资源数量
        url=URL+"%d.ts"%i                            #拼接ts文件的URL地址，通常有“%d”和“%03d”两种
        if not os.path.exists(path+'/%03d.ts'%i):
            downts(path,url,i)
            time.sleep(0)                            #设置延时处

def getURL():   #输入拼接资源URL,最后变化之外的部分
    URL="http://asp.cntv.qingcdn.com/asp/hls/2000/0303000a/3/default/b70ddc511cc44f92be0fb3c398473fbc/"
    main(URL)
    
getURL()

            #本程序可以作为下载未加密m3u8格式文件的模板，其他URL文件只需更改getURL函数中的URL即可！
            #另外大文件可以通过使用进程池加快下载速度！