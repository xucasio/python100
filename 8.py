# 输出 9*9 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        # end的作用是下个print不换行 print 默认是换行的
        print('%d * %d = %d\t' % (i, j, i * j), end='')
    print()  # 换行
