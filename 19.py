# 读取网页数据，BeatifulSoup选择页面元素
from bs4 import BeautifulSoup
with open('./files/index.html', 'r', encoding='utf-8') as wb_data:
    Soup = BeautifulSoup(wb_data, 'html5lib')
    lis = Soup.select('.content>ul>li')
    for item in lis:
        print(item, item.text, sep='\n----------------\n')