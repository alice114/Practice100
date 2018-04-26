# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
f1 = 1
f2 = 1
print('%12ld%12ld'%(f1,f2))
print('%2ld%2ld'%(f1,f2))
# for i in range(1,22):
#     print('%2ld%2ld'%(f1,f2)),
#     if(i % 3) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 +f2

for i in range(1,22):
    print('%12ld%12ld'%(f1,f2)),
    # if(i % 3) == 0:
    #     print('')
    f1 = f1 + f2
    f2 = f1 +f2

def rabbit(n):
    count = [1,0,0]
    for i in range(1,n):
        count[2] = count[0] + count[1]
        count[1] = count[0]
        count[0] = count[2]
    return count[0]+count[1] + count[2]
n = int(input("查看第几个月的兔子对数："))
rabbit_sum = rabbit(n)
print("第%d个月的兔子对数为%d"%(n,rabbit_sum))
print(rabbit(10))
print(rabbit(20))
print(rabbit(30))