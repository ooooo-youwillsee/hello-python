# arr = [1, 2, 4, 5, 6]
from builtins import reversed

arr = {"name": 123, "age": 345, "password": "dgdfgd"}
# for i in arr:
#     print(i)

numList1 = [1, 2, 3, 4, 2, 4, 7]
numList2 = []
for num in numList1:
    if num not in numList2:
        numList2.append(num)

print(str(numList2))
# 对列表本身进行操作
numList2.reverse()
print(str(numList2))

# 列表中的元素不是同一类型,会报异常
numList1.sort()

# 对字典删除
del arr["name"]

string = [str(x) for x in range(0, 10)]
str1 = "-"
print(str1.join(string))
