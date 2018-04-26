





i = int(input("净利润:"))
if (i <= 100000):
    r = i * 0.1
elif (i <= 200000):
    r =  100000 * 0.1 + (i - 100000) * 0.075
elif (i <= 400000):
    r = 100000 * 0.1 + (200000 - 100000) * 0.075 + (i - 200000) * 0.05
else:
    r = 0.01 * i
print(r)

#列表比较，计算
i = int(input('净利润：'))
arr = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i > arr[idx]:
        r += (i-arr[idx])*rate[idx]
        print((i-arr[idx])*rate[idx])
        i = arr[idx]
print(r)

#字典，keys & value  get(key) ,
#python 2,3的区别：3无dict.keys()的k = d.keys();k.sort(),你可以使用k = sorted(d)来代替
# 使用Views和Iterators代替Lists
#
# dict的方法dict.keys(),dict.items(),dict.values()不会再返回列表,而是返回一个易读的“views”。这样一来，像这样的语法将不再有用了:k = d.keys();k.sort(),你可以使用k = sorted(d)来代替。sorted(d)在Python2.5及以后的版本中也有用，但是Python3效率更高了。
# d = {'a': 1}
# d.keys()     # dict_keys(['a'])
# d.items()    # dict_items([('a', 1)])
# d.values()   # dict_values([1])
# k = d.keys(); k.sort()     # AttributeError: 'dict_keys' object has no attribute 'sort'
# 同样，dict.iterkeys(),dict.iteritems(),dict.itervalues()方法也不再支持。
# map()和filter()将返回iterators。如果你真的想要得到列表,list(map(...))是一个快速的方法，但是更好的方法是使用列表推导(尤其是原代码使用了lambda表达式的时候),或者重写原来的代码,改为不需要使用列表。特别是map()会给函数带来副作用，正确的方法是改为使用for循环，因为创建一个列表是非常浪费的事情。
# Python3中的range()函数跟Python2.X的xrange()函数的作用是一样的，这样可以使用任意的数字,Python3中去除了xrange()函数。
# zip()在Python3中返回的是一个迭代器。

num = int(input("please input income:"))
obj = {1000000:0.01,600000:0.015,400000:0.03,200000:0.05,100000:0.075,0:0.1}
keys = obj.keys()
print(keys)
k = list(keys)
print(k)
r = 0
for key in keys:
    if num > key:
        r += (num - key) * obj.get(key)
        num = key
print(r)



#列表生成式和生成器  generator  yield关键字构造生成器函数

a = [100,60,40,20,10,0]
b = [0.01,0.015,0.03,0.05,0.075,0.1]

def f(x):
    for i in range (len(a)):
        if n > a[i]:
            c = (a[j] - a[j+1] for j in range(i,len(a) - 1))
            break
    r = sum(map(lambda x,y:x*y,b[i:],[(n - a[i])] + list(c)))
    yield r * 10000

k = int(input("是否计算奖金？ 是：1， 否：0\n"))
while k:
    n = int(input('利润：'))
    print('应发奖金：',next(f(n),'元'))
    print()
    k = int(input("是否继续计算奖金？是：1， 否：0\n"))


