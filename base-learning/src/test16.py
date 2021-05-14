# coding=utf-8

import threading

#  多线程

num = 0
threading.Lock().acquire(blocking=True)
threading.local()


def xx(x: str) -> bool: ...


def incr1():
    global num
    for i in range(0, 10000):
        num += 1
    print("%s~~~ num=%s" % (threading.current_thread().name, num))


def incr2():
    global num
    for i in range(0, 10000):
        num += 1
    print("%s~~~ num=%s" % (threading.current_thread().name, num))


thread1 = threading.Thread(target=incr1, name="111")
thread2 = threading.Thread(target=incr2, name="222")
thread1.start()
thread2.start()
