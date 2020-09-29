# 题目：将一个正整数分解质因数；
# 分析：
# 若这个质数恰等于n，则说明分解质因数的过程结束，打印即可；
# 若n!=k，但n能被k整除，则应打印出k的值，并用n除以k的商，作为新的正整数n，重复执行第一步；
# 若n不能被k整除，则用k+1作为k的值,重复执行第一步；


def prime(n):
    print(str(n) + ' = ')
    if not isinstance(n, int) or n <= 0:
        print('Please input a valid number !')
        exit(0)
    elif n in [1]:
        print(n)
    while n not in [1]:
        for index in range(2, int(n + 1)):
            if n % index == 0:
                n /= index
                if n == 1:
                    print(index)
                else:
                    print(str(index) + " *", end=' ')
                break


num = input('Input the num, enter "q" to quit：')
while num != 'q':
    prime(int(num))
    num = input('Input the num：')