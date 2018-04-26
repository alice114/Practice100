# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。



# method 1：？print none? 5crwqNone  ?怎么实现循环输入？但程序不结束
for i in range(1):
    i = input("Please input:")
    l = len(i)

    def output(i,l):
        if l == 0:
            return i[0]

        print(i[l - 1],end="")
        output(i, l - 1)


    #
    if __name__ == '__main__':
        print(output(i,l))


# method 2：
def desc_output(s):
    if(len(s) > 0):
        print(s[-1])            # python 负数下标
        desc_output(s[0:-1])

s = input('Input a string:')
desc_output(s)


# method 3： list append, remove

def stringoutput(s):
    t = []
    l = list(s)
    while(len(s)>0):
        t.append(s[-1])
        l.remove(l[-1])
    print(t)

if __name__ == '__main__':
    s = input("input string")
    stringoutput(s)

