# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


# summary:
# reverse return nono:
# 原来这个reverse函数，针对列表的操作，其结果是直接改变列表本身（为了节省空间），
# 所以，直接就把原先的list改为你所想要的reversed后的结果了，而返回值，是空的，不返回任何值。
# 对于List等Sequence等类型的变量，比如此处的List变量，其内置函数reverse，是直接操作变量本身，
# 调用reverse后，变量本身的值就是reverse后的值了

# convert to list,then compare
def isPalindrome(n):
    s = str(n)
    length = len(s)
    l,l_rev = [],[]
    for i in range(length):
        l.append(s[i])
    for i in range(length):
        l_rev.append(s[i])
    l_rev.reverse()
    # print(l)
    # print(l_rev)
    if (l == l_rev):
        return True
    return False

if __name__ == '__main__':
    print(isPalindrome(1012))
    print(isPalindrome(101))
    print(isPalindrome(3456543))
    print(isPalindrome(1))


# for int compare