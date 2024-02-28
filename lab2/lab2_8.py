day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def day_of_year(day, month, year):
    count = 0
    if is_leap(year)  == True:
      day_in_month[2] = 29
    for i in range (month):
       count += day_in_month[i]
    day_in_month[2] = 28
    return count+day

def day_in_year(year):
    if is_leap(year) == True:
      return 366
    else:
      return 365

def date_diff(date1, date2):
    day1, month1, year1 = [int(i) for i in date1.split('-')]
    day2, month2, year2 = [int(i) for i in date2.split('-')]
    """
    first_year_day = day_in_year(year1)-(sum(day_in_month[:month1]) + day1 )+1
    second_year_day = (sum(day_in_month[:month2]) + day2 ) 
    range_year = 0
    if year2-year1 > 0:
      for i in range (year1+1,year2):
        if is_leap(i) ==True:
          range_year += day_in_year(i)
        else:
          range_year += day_in_year(i)   
    ##else:
      ##second_year_day += 1

    date_diff = first_year_day + second_year_day + range_year 
    if year2-year1 == 0:
      first_year_day = day_in_year(year1)-(sum(day_in_month[:month1]) + day1 )+1
      second_year_day = day_in_year(year2)-(sum(day_in_month[:month2]) + day2 )
      date_diff = first_year_day - second_year_day
    elif year1 % 4 == 0 and year1 % 100 == 0 and year1 % 400 != 0 and is_leap(year2) == True:
      date_diff = first_year_day + second_year_day + range_year +1
    return (date_diff)
    """
    if year1 == year2:
       return day_of_year(day2,month2,year2)-day_of_year(day1,month1,year1)+1
    else:
       count = day_in_year(year1)-day_of_year(day1,month1,year1)+day_of_year(day2,month2,year2)+1
       for i in range(year1+1,year2):
          count += day_in_year(i)
       return count

date1, date2 = input("").split()
print(date_diff(date1, date2))
"""
day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    pass
def day_of_year(day, month, year):
    pass
def day_in_year(year):
    pass
def date_diff(date1, date2):
    pass
"""