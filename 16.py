# 输出指定格式的日期
import datetime
# 只有当脚本执行才会是main，被引用不会
if __name__ == '__main__':
    # 输出当前日期
    print(datetime.date.today())

    # 创建日期对象
    Z_Birth = datetime.date(1994, 11, 12)
    print(Z_Birth)

    # 指定格式输出
    print(Z_Birth.strftime('%m/%d/%Y'))

    # 日期替换
    # 时间的改动，重点
    Z_Birth = Z_Birth.replace(year=Z_Birth.year + 1)
    print(Z_Birth)

    # 日期运算
    Next_Z_Birth = Z_Birth + datetime.timedelta(days=366)
    print(Next_Z_Birth)