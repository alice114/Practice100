# 题目：暂停一秒输出。

import time

myD = {1:'a',2:'b'}
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(5)

l = [1,2,3,4,5]
for i in range (len(l)):
    print(l[i])
    time.sleep(5)