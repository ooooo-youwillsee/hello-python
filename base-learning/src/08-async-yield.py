# coding:utf-8

import time
import threading

gen = None
def a():
    print("starting---a---")
    result = yield long_io()
    print("finished---a---")
    print(result)

def b():
    print("starting---b---")
    print("finished---b---")

def long_io():
    def fun():
        global gen
        print("starting --- long io --- ")
        time.sleep(3)
        try:
            gen.send("io result")
        except:
            pass
        print("finished --- long io --- ")
    threading.Thread(target=fun).start()

def main():
    global gen
    gen =  a()
    next(gen)
    b()

if __name__ == '__main__':
    main()