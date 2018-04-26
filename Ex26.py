# 题目：利用递归方法求5!。

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)




#改进  ?什么时候return？ 递归return多个返回值占空间？
def fac(n):
    if(n == 1):
        return 1
    else:
        fn = n * fac(n-1)
        return fn

if __name__ == '__main__':
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(5))
    print(factorial(7))
    print(fac(7))