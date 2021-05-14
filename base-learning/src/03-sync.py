# coding:utf-8

import time
import datetime

def a():
    print("starting---a---")
    print(datetime.datetime.now().strftime("%F %X"))
    result =  long_io()
    print("finished---a---")
    print(result)

def b():
    print("starting---b---")
    print("finished---b---")

def long_io():
    print("starting --- long io --- ")
    time.sleep(3)
    print("finished --- long io --- ")
    return "io result"

def main():
    a()
    b()

if __name__ == '__main__':
    main()