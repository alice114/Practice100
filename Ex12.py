# 题目：判断101-200之间有多少个素数，并输出所有素数。

l = []
for i in range(101,201):
    for j in range(2,i-1):
        if(i % j == 0):
            break
    else:
        l.append(i)

print(l)
print("总数为：%d"%len(l))


l = []
for i in range(101,201):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        l.append(i)

print(l)
print("总数为：%d"%len(l))

# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
h = 0
leap = 1
from math import sqrt
# from sys import stdout
for m in range(100,201):
    k = int(sqrt(m+1))
    for i in range(2,k+1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d'%m)
        h += 1
        # if h % 10 == 0:
        #     print('')
    leap = 1
print('The total is %d'%h)

#切片排除法
import math
m = list(range(101,201))
print(m)
p = list(m[:])
print(p)
for i in range(101,201):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            m.remove(i)
            break
print(m)
print("num sushu%d"%len(m))



#切片排除法
import math
m = list(range(100,201))
p = m[:]
for i in range(101,201):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            p.remove(i)
            break
print(p)
print("num sushu%d"%len(p))

#生成器
L = list(filter(lambda x: x not in set([i for i in range(101,201) for j in range(2,i) if not i % j]),range(101,201)))
print('一共有{}个素数，这些素数分别是：{}'.format(len(L),L))