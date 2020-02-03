# coding=utf-8

import os
import multiprocessing
import queue



# fork_id = os.fork()
# if fork_id == 0:
#     print("我是子进程%s" % fork_id)
# else:
#     print("我是父进程%s" % fork_id)

def check(name, age):
    print(multiprocessing.current_process().name, end="")
    print("检查~~~")


process1 = multiprocessing.Process(target=check, args=("tom", 18), name="1号")
process2 = multiprocessing.Process(target=check, args=("jerry", 20), name="2号")
process1.start()
process2.start()

queue = queue.Queue(3)
queue.put("1")
queue.put("2")
queue.put("3")
# queue.put("4")

print(queue.get())
