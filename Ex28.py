# 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

# 问题：递归 +print，在函数里print怎么print？

# 正向
def age(age1,n):
    for i in range(1,n):
        age1 += 2
    print(age1)



# 递归
def age_m1(age1,n):
    if n == 1:
        return age1
    return age_m1(age1+2,n-1)


# 递归 +print
def age_m2(age1,n):
    if n == 1:
        return age1
    return age_m1(age1+2,n-1)
# print(age_m1)



if __name__ == '__main__':
    age(10,8)
    age(10,5)
    print(age_m1(10,8))
    print(age_m1(10,4))