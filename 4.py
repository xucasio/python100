# 题目：输入某年某月某日，判断这一天是这一年的第几天？
list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("请输入年"))
month = int(input("请输入月"))
day = int(input("请输入日"))
print('输入结果为%d年%d月%d日' % (year, month, day))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    count = 0
    for i in range(1, month - 1):
        count += list1[i]
    count += day
    print('这一天是这一年的第%d天' % count)
else:
    count = 0
    for i in range(1, month - 1):
        count += list2[i]
    count += day
    print('这一天是这一年的第%d天' % count)
