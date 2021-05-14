# coding:utf-8

import datetime
import time
import threading


def a():
    print("starting---a---")
    print(datetime.datetime.now().strftime("%F %X"))
    long_io(on_finish)
    print("finished---a---")


def b():
    print("starting---b---")
    print("finished---b---")


def long_io(f):
    def fn(func):
        print("starting --- long io --- ")
        time.sleep(3)
        print("finished --- long io --- ")
        func("io result")
    threading.Thread(target=fn, args=(f,)).start()


def on_finish(s):
    print("开始执行回调函数")
    print("回调函数结果 %s" % s)
    print("结束执行回调函数")


def main():
    a()
    b()


if __name__ == '__main__':
    main()
