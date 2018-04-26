# 将一个正因数分解 90 = 2 * 3 * 3 * 5

def factor(n):
    l = [n]
    for i in range(2,n):
        while (n % i == 0):
            l.append(i)
            n = n / i
            # print(i)
            # print(l)
            # break
    return l
print(factor(81))

# for i in range(1,len(l)):
#     print(l[0] = )

