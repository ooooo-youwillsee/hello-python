# coding:utf-8

# 装饰器

def test1(fn):
    print("----test1---")
    def test2():
        print("----test2---")
        fn()

    return test2

@test1
def test():
    print("----test---")

if __name__ == '__main__':
    test()


