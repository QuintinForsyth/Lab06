import random

def get_top(message, bottom_range):
  """
  Gets top range as an integer and gets top range higher than bottom
  """
  try:
    x = int(input(message))
    if (x > bottom_range):
      return(x)
    else:
      print("Provide a number greater than "+bottom_range)
      get_top(message,bottom_range)
  except:
    print("Please provide an integer")
    get_top(message, bottom_range)
    
  try:
    x = int(input(message))
    return(x)
  except:
    print("Please provide an integer")
    get_int(message)
    
def get_int(message):
  """
  Gets an integer
  """

  try:
    x = int(input(message))
    return(x)
  except:
    print("Please provide an integer")
    get_int(message)

def again():
  """
  Asks if user wants to play again
  """
  again = input("Correct!\nwould you like to play again (Y or N)?")
  if (again == "yes" or again == "Yes" or again == "Y" or again == "y"):
      print("\n"*150)
      print("Reseting random number")
      play_game()
  else:
    print("bye );")

def guess_number(random_number, top_range, minimum_range):
  """
  Main Guessing interface 
  """
  guess = int(input("Guess a number between "+str(minimum_range)+" and "+str(top_range)))
  
  if (guess == random_number):
     return 
  if (guess < random_number):
    response = "Higher"
  else:
    response = "Lower"
  print(response+", try again!")
  guess_number(random_number, top_range, minimum_range)


  

def play_game():
  """
  Runs code to play game
  """
  minimum_range = get_int("Enter the minimum number")
  top_range = get_top("Enter the maximum number",minimum_range)
  random_number = random.randint(minimum_range, top_range)
  guess_number(random_number, top_range, minimum_range) 
  again()
  

play_game()
