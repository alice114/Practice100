# 斐波那契数列

def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) +fib(n-2)

print(fib(10))


def fib(n):
    if (n == 1):
        return [1]
    if (n == 2):
        return [1,1]
    fibs = [1, 1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fib(10))