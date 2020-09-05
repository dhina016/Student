from datetime import datetime, date, time
'''
%a    -    Fri
%A    -    Friday
%w    -    5
%d    -    04 or 4
%b    -    Sep
%B    -    September
%m    -    09 or 9
%y    -    20
%Y    -    2020
%H    -    09 or 9 24 Hour format
%I    -    09      12 hour format   
%M    -    31
%s    -    40.1111
%p    -    AM/PM
%c    -    Fri Sep  4 09:41:40 2020
%x    -    09/04/20
%X    -    09:43:21
'''
# a = date(year, month, date)
# a.strftime('%A')
# 9 6 2019
# Wednesday, friday
# day, month, year = map(int, input().split())
# a = date(year, month, day)
# print(a.strftime('%A'))


# 1 2 3 4 5 6 7 8 9
# l
l2 = input().split()
l = list(map(int, input().split()))
print(l2, l)