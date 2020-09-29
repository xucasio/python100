# 题目：判断101-200之间有多少个素数，并输出所有素数；
import math

flag = False
count = 0
for i in range(101, 201):
    for j in range(2, int(math.sqrt(i + 1)) + 1):
        if i % j == 0:
            flag = True
            break
    if flag is False:
        count += 1
        print(i, end='\t')
        if count % 5 == 0:
            print()
    flag = False
