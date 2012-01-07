"""
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
  Thirty days has September,
  April, June and November.
* All the rest have thirty-one,
* Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from collections import OrderedDict

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
months = OrderedDict([
        ('january', 31), 
        ('february', 28),
        ('march', 31),
        ('april', 30),
        ('may', 31),
        ('june', 30), 
        ('july', 31),
        ('august', 31), 
        ('september', 30), 
        ('october', 31), 
        ('november', 30), 
        ('december', 31), 
])

def the_jumping_technique():
    # the first day of 1901 is tuesday
    day = 1
    
    # the initialization of variables
    start_year = 1901
    end_year = 2000
    counter = 0
    
    # for each year in the century
    for year in range(start_year, end_year + 1):
        # for each month in the year
        for month, num_days in months.iteritems():
            # adding the extra day for february, given the conditions
            if (month == "february" and year % 4 == 0) or \
               (month == "february" and year % 400 == 0 and year % 100 == 0):
                t_num_days = num_days + 1
            else:
                t_num_days = num_days
            
            # the magic formula !! its obvious actually to add the 
            # number of days in the month and take remainder with
            # the number of days in the week
            day = (day + t_num_days) % len(days)
            
            if day == 6: # sunday
                counter = counter + 1
    
    return counter
    
print "Answer by usual method:", the_jumping_technique()
