# coding:utf-8

# 实现python的类字典对象

class Person(dict):


    def __init__(self, name,age):
        super().__init__()
        self.name = name
        self.age = age

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value


person = Person("zhangsan", 15)
print(person.name)
print(person['name'])
