# 利用递归计算斐波那契数列，输入斐波那契数列的n位，调用递归计算出第n位的数列值；
def fib(num):
    if num <= 2:
        result = 1
    else:
        result = fib(num - 1) + fib(num - 2)
    return result


num = int(input("num = "))
print("得到的结果为", fib(num))
