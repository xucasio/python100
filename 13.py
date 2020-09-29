# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
arr = []


def getArr(min, max):
    for i in range(min, max):
        ge = i % 10
        shi = i // 10 % 10
        bai = i // 100
        if ge**3 + shi**3 + bai**3 == i:
            arr.append(i)
    return arr


print('水仙花数组', getArr(100, 1000))
