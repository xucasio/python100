# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 分析：通过三层循环，将个、十、百位上的数分别循环一次，当其中任意两位相同时，则跳过，当各位上的数都不同时，输出
count = 0
arr = range(1, 5)
for i in arr:
    for j in arr:
        for k in arr:
            if i != j and j != k and k != i:
                count += 1
print('结果：', count)
