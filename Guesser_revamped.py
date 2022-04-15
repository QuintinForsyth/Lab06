import random


def get_int(message):
  """
  Gets an integer
  """
  x = input(message)
  check_x = isinstance(x, int)
  print(check_x,x)
  if (check_x == True):
    return(x)
  else:
    # raise AssertionError ("That is not an integer.")
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
  top_range = get_int("Enter the maximum number")
  random_number = random.randint(minimum_range, top_range)
  guess_number(random_number, top_range, minimum_range) 
  again()
  

play_game()
