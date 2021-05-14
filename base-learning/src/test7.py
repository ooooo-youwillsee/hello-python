# 异常

try:
    a = 1 / 0
    # a = 1 / 2
    print(a)
except Exception as result:

    print("异常了。。。。"+str(result))
else:
    print("没有发生异常，就会执行这一句")
finally:
    print("不管有没有异常，都会执行这一句")

