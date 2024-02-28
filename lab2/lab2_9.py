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
    a=b=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year1):
        a[2]=29
    if is_leap(year2) :
        b[2]=29
    if (month1 < 1) or (month1 > 12) or (month2 < 1) or (month2 > 12) or (day1 < 1) or (day1 > a[month1]) or (day2 < 1) or (day2 > b[month2]):
        return -1
  
    else:
        if year1 == year2:
            return day_of_year(day2,month2,year2)-day_of_year(day1,month1,year1)+1
        else:
            count = day_in_year(year1)-day_of_year(day1,month1,year1)+day_of_year(day2,month2,year2)+1
            for i in range(year1+1,year2):
                count += day_in_year(i)
            return count
    

date1, date2 = input("").split()
print(date_diff(date1, date2))