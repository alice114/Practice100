# 题目：将一个列表的数据复制到另一个列表中。

a = [1,2,3]
b = a.copy()
print(b)

c = b[:]
print(c)

#列表生成式
d = [i for i in a]
print(a)

#循环列表
e = []
for i in range(len(a)):
    e.append(a[i])
print(e)



# 补充一个深拷贝与浅拷贝的问题
import copy
a = [1,2,3,4,5]
b = ["A","B",a]

#浅拷贝
c = b[:]
print(c)

a[0] = 11
print(c)

#深拷贝
c = copy.deepcopy(b)

a[0] = 111
print(a)

print(c)
#此时c中数据不受a影响