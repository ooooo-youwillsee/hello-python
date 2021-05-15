# 单例模式


class Person(object):
    __getInstance = None
    __init = False

    def __new__(cls, *args, **kwargs):
        if cls.__getInstance is None:
            cls.__getInstance = object.__new__(cls)
            return cls.__getInstance
        else:
            return cls.__getInstance

    def __init__(self, name, age):
        if self.__init is False:
            self.name = name
            self.age = age
            self.__init = True

    def __str__(self):
        return self.name + "-->" + str(self.age)


if __name__ == '__main__':
    p1 = Person("Hello", 21)
    print(id(p1))
    print(p1)
    p2 = Person("World", 25)
    print(id(p2))
    print(p2)
