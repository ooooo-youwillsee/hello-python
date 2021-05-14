# coding:utf-8

# 使用装饰器实现异步


import time
import threading

def gen_coroutine(f):
    def wrapper():
        gen = f()  # 得到a()的生成器
        longio_gen =  next(gen) # 到long_io()的生成器
        def fun(ff):
            try:
                result =  next(ff)
                gen.send(result)
            except:
                pass
        threading.Thread(target=fun,args=(longio_gen,)).start()
    return wrapper

@gen_coroutine
def a():
    print("starting---a---")
    result = yield  long_io()
    print("finished---a---")
    print(result)

def b():
    print("starting---b---")
    print("finished---b---")

def long_io():
    print("starting --- long io --- ")
    time.sleep(3)
    print("finished --- long io --- ")
    yield "io result"



def main():
    a()
    b()

if __name__ == '__main__':
    main()