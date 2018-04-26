#原始计数，print数字
num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j) and (j != k):
                print(100*i+10*j+k)
                num += 1
print(num)

#构建列表 d = [] ，添加列表项 d.append()，列表长度 len(d)
d = []
for a in range (1,5):
    for b in range (1,5):
        for c in range (1,5):
            if (a != b) and (b != c) and (a != c):
                d.append([a,b,c])
print("总数量：",len(d))
print(d)




list_num = [1,2,3,4]
list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num
        if (i != j) and (i != k) and (j != k)]
print(list)
print(len(list))