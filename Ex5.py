#list.sort()
l = []
for i in range(3):
    x = int(input('integer:'))
    l.append(x)
l.sort()
print(l)
l.sort(reverse=False)
print(l)
l.sort(reverse=True)
print(l)


#冒泡排序法写sort
def Sort(list):
    n = len(list)
    for i in range(1,n):
        for j in range(1,n - i + 1):
            if list[j-1] > list[j]:
                list[j-1],list[j] = list[j],list[j-1]
            print(list)
    for i in range(0,n):
        print(list[i])


def inputData():
    list_first = []
    while True:
        a = input("please input num:".strip())
        if len(a) == 0:
            return list_first
        else:
            list_first.append(int(a))

if __name__ == '__main__':
    lt = inputData()
    print(lt)
    Sort(lt)

