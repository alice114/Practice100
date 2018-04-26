# 题目：暂停一秒输出，并格式化当前时间。

import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(1)
print(time.time())

print(time.gmtime())
print(time.struct_time)

import calendar
cal = calendar.month(2018,4)
print(cal)

import datetime
print(datetime.datetime.now())