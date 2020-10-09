# 多线程 利用Event类模拟红绿灯
# 详细的线程看这个 https://www.cnblogs.com/luyuze95/p/11289143.html
import threading
import time


def run(n):
    print("task", n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1", ))
    t2 = threading.Thread(target=run, args=("t2", ))
    t1.start()
    time.sleep(0.1)
    t2.start()
