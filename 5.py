# 题目：输入三个整数x,y,z，请把这三个数由小到大输出
while True:
    arr = []
    for i in range(1, 4):
        item = int(input('请依次输入三个整数'))
        arr.append(item)
    brr = arr.reverse()
    print('排序后的数组', arr, brr)