# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
num = 0


def getRabSum(m):
    if m <= 2:
        num = 1
    else:
        num = getRabSum(m - 2) + getRabSum(m - 1)
    return num


while True:
    mons = int(input('输入月份'))
    print('获得总数', getRabSum(mons))