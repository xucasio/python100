# 暂停一秒输出，并格式化当前时间；
import time


def getNowTime():
    start = time.process_time()
    time.sleep(3)
    print('当前时间是', time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))
    print('time.localtime', time.localtime())
    print('perf_counter', time.perf_counter())  # 返回系统运行时间
    print('process_time', time.process_time())  # 返回进程运行时间
    print('时间戳', int(time.time()))
    print(
        '时间戳转字符串时间',
        time.strftime("%Y-%m-%d %H:%M:%S %a",
                      time.localtime(int(time.time()))))
    end = time.process_time()
    print('执行这段程序需要的时间1', end - start)


# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29, tm_hour=14, tm_min=25, tm_sec=53, tm_wday=1, tm_yday=273, tm_isdst=0)

start = time.process_time()
getNowTime()
# for i in range(10000):
#     print(i)
end = time.process_time()
print('执行这段程序需要的时间', end - start)
