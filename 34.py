# 爬取某个地址的小说
import re
import urllib.request
import time
import os


# 定义一个爬取网络小说的函数
def getNovelContent():
    html = urllib.request.urlopen(
        "http://www.quanshuwang.com/book/44/44683").read()
    html = html.decode("gbk")  # 转成该网址的格式
    # <li><a href="http://www.quanshuwang.com/book/44/44683/15379609.html" title="引子 穿越的唐家三少，共2744字">引子 穿越的唐家三少</a></li>  # 参考
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'  # 正则表达的匹配
    reg = re.compile(reg)  # 可添加可不添加，增加效率
    urls = re.findall(reg, html)
    bookname = 'douhundalu'
    folder_path = './' + bookname
    if os.path.exists(folder_path) is False:
        os.makedirs(folder_path)
    retval = os.getcwd()
    os.chdir(retval + '\\' + bookname)
    for url in urls:
        # print(url)
        time.sleep(10)
        chapter_url = url[0]  # 章节的超链接
        chapter_title = url[1]  # 章节的名字
        # print(chapter_title)
        chapter_html = urllib.request.urlopen(chapter_url).read()  # 正文内容源代码
        chapter_html = chapter_html.decode("gbk")
        chapter_reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;.*?<br />(.*?)<script type="text/javascript">'
        chapter_reg = re.compile(chapter_reg, re.S)
        chapter_content = re.findall(chapter_reg, chapter_html)
        for content in chapter_content:
            content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")
            content = content.replace("<br />", "")

            f = open('{}.txt'.format(chapter_title), 'w')
            f.write(content)
            time.sleep(1)


getNovelContent()
