def is_leap(year):
    if year % 4 == 0:      #4 and 100 % == 0 True
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == True and month == 2:
      return 29
  return month_days[month - 1] #list start from zero so january will be in month_days[0]


year = int(input("Enter a year: ")) #Year
month = int(input("Enter a month: ")) #Month

days = days_in_month(year, month)
print(days)