# coding=utf-8


## 单例模式

class SingleTon:
    __instance = None
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        if self.__obj is None:
            self.__name = name
            self.__age = age
            self.__obj = self

    def __str__(self):
        return "name:%s,age:%s" % (self.__name, self.__age)


obj1 = SingleTon("haha", 12)
print(obj1)
obj2 = SingleTon("xixi", 12)
print(obj2)


class XX:

    def __init__(self,name):
        self.__name = name

