import math

def is_int(check):
  """
  checks if int only
  """
  return math.floor(check)==check
  
def is_leapyear(year):
  """
  checks if year is an integer
  """
  
  check_year = isinstance(year, int)
  year_by_one_hun = year/100
  year_by_one_hun =is_int(year_by_one_hun)
  year_by_four_hun = year/400
  year_by_four_hun =is_int(year_by_four_hun)
  year_by_four = year/4
  year_by_four =is_int(year_by_four)
  """
  checks if year is valid then checks if the year is divisible by four, then checks if it is a 100 and 400 year or just a 4 leap year
  """
  if (check_year == True):
    if(year_by_four == True):
      if(year_by_one_hun == True and year_by_four_hun == True):
         return True
      elif(year_by_one_hun != True and year_by_four_hun != True):
        return True
      else:
        return False
    else: 
      return False
  else:
    return False

print(is_leapyear(1752))
