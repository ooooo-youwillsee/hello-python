# coding=utf-8
class Base(object):
    def test(self):
        print('----base test----')


class A(Base):
    def test(self):
        print('----A test----')


# 定义一个父类
class B(Base):
    def test(self):
        print('----B test----')


# 定义一个子类，继承自A、B
class C(A, B):
    pass


obj_C = C()
obj_C.test()

print(C.__mro__)  # 可以查看C类的对象搜索方法时的先后顺序
