# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

#Summary: [int] directly convert to [string] , traversal to [list]

# i = input("input integer:")
# s = list[i]
def output(i):
    s = str(i)
    n = len(s)
    if n>5:
        return print('please input corret number:')
    l = []
    for i in range(n):
        l.append(s[i])
    l.reverse()
    print('the digitnum is {}, the reverse num is {}'.format(n, l))

if __name__ == '__main__':
    i = int(input("input integer:"))
    output(i)


# print in main? how to return?
# def output(i):
#     s = str(i)
#     n = len(s)
#     l = []
#     for i in range(n):
#         l.append(s[i])
#     l.reverse()
#     return n,l
#
# if __name__ == '__main__':
#     i = input("input integer:")
#     output(i)
#     print('the digitnum is {}, the reverse num is {}'.format(n, l))

# i input default to string, not int. convert to list how to test i = string/int?
def output(i):
    s = list(i)
    n = len(s)
    s.reverse()
    print('the digitnum is {}, the reverse num is {}'.format(n, s))

if __name__ == '__main__':
    i = int(input("input integer no more than 5 digits:"))
    output(i)