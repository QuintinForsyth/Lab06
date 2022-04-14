import math
import Question1

def hypotenuse(a, b):
  """
  check if number if true goes into the if statement for the hypotenuse
  """
  check_a = Question1.is_numeric(a)
  check_b = Question1.is_numeric(b)
  
  if(check_a == False or check_b == False):
    raise AssertionError ("Both a and b must be numeric")
  elif (a > 0 and b > 0):
    if (check_a == True and check_b == True):
      return(math.sqrt(a**2+b**2))
  else:
    raise AssertionError ("Both a and b must be Greater than 0")

