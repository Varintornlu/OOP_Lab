day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

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
  if is_leap(year)  == True:
    day_in_month[2] = 29

  day_of_year = sum(day_in_month[:month]) + day 
  return day_of_year
  

day_input = int(input(""))
month_input = int(input(""))
year_input = int(input(""))

day_number = day_of_year(day_input, month_input, year_input)
print(day_number)
