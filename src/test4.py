file = open("../txt/01.txt")
# line = file.readline()
# while line != "":
#     print(line, end="")
#     line = file.readline()

file.seek(0, 0)
lines = file.readlines()
for line2 in lines:
    line2 = line2.split("\n")[0]
    print(line2)
file.close()
print()
print(lines)
