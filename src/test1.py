import sys


class Map(object):
    def __init__(self):

        self.obj = {}

    def put(self, key, value):
        self.obj[key] = value

    def size(self):
        count = 0
        for attr in self.obj:
            # print(attr)
            count += 1
        return count

    def get(self, key):
        return self.obj[key]

    def each(self, fn):
        for attr in self.obj:
            fn(attr, self.obj[attr])

    # def __new__(cls):
    #     return object.__new__(cls)
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)




def xx(key, value):
    print("%s+....+%s" % (key, value))


if __name__ == '__main__':
    result = Map()
    result.put("01.txt", "0002")
    result.put("02", "000002")
    print(result.size())


    # print(math.ceil(2.3))
    # result.each(xx)
