# coding=utf-8

import threading
import time

def threadRun():
    print("---执行线程开始---")
    time.sleep(10)
    print("---执行线程结束---")


def main():
    print("---主线程开始---")
    thread = threading.Thread(target=threadRun)
    thread.start()
    print("---主线程结束---")


if __name__ == '__main__':
    main()