# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for num in range(100,1000):
    a = int(num / 100)
    b = int(num % 100 / 10)
    c = int(num % 10)
    # print(a,b,c)
    if num == a * a * a + b * b * b + c * c * c:
        print(num)


for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print (n)

for i in range (100,1000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    # print(a,b,c)
    # print(a**3,b**3,c**3)
    if i == a**3 + b ** 3 + c ** 3:
        print(i)


# for x in range(1,10):
#      for y in range(0,10):
#         for z in range(0,10):
#             s1=x*100+y*10+z
#             s2=pow(x,3)+pow(y,3)+pow(z,3)
#             if s1==s2:
#                 print("水仙花数有：%7ld" %(s1))
#