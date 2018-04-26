# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if (0 < month <= 12):
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100) != 0):
    leap = 1
if (leap ==1) and (month > 2):
    sum += 1
print('it is the %dth days.'%sum)


#dict
def isLeapYear(a):
    if (a % 400 == 0) or ((a % 4 == 0) and (a % 100) != 0):
        return 1
    else:
        return 0
dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
m = 0
k = isLeapYear(year)
for i in range(1,month):
    m = m + dict[i]
m = m + isLeapYear(year) + day
print(m)

#list  ? not correct   'int' object is not callable
a = int(input('year:'))
b = int(input('month:'))
c = int(input('day:'))
dt = [31,28,31,30,31,30,31,31,30,31,30,31]
if(isLeapYear(a)):
    dt[1] += 1
now = sum(dt[0:b-1])+ c
print(now)


#import class
import time
date = input("输入年月日(yyyy-mm-dd):")
day = time.strptime(date,"%Y-%m-%d")
print(day)
print(day.tm_yday)
