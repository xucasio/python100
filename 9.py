# 暂停一秒输出
import time

list1 = ['1s', '2s', '3s']
for i in range(0, len(list1)):
    print(list1[i])
    time.sleep(1)