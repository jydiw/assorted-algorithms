'''
You are given the following information, but you may prefer to do some research 
for yourself.

-   1 Jan 1900 was a Monday.
-   Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
-   A leap year occurs on any year evenly divisible by 4, but not on a century 
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
'''

import numpy as np

def days_in_year(year):
    # using the information given as an exercise
    days = np.array([31] * 12)
    days[[9, 4, 6, 11]] = 30
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days[2] = 29
    else:
        days[2] = 28
    return sum(days)


def counting_sundays(jan_year, dec_year):

    start = 1
    for y in range(1900, jan_year):
        start += days_in_year(y) % 7

    num_days = 0
    for y in range(jan_year, dec_year + 1):
        num_days += days_in_year(y)

    weeks = (num_days - (7 - start)) // 7
    
    return weeks


counting_sundays(1901, 2000)