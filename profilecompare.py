from art import logo,vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')



def data_selector():
  """Returns a random choice from the data"""
  return random.choice(data)

def details(person):
  """Printing the Account details"""
  name=person['name']
  desc=person['description']
  country=person['country']
  return f"{name} a {desc},from {country}"

  
def follower_checker(guess,a_follower,b_follower):
  """Compares the followers and returns the result"""
  if a_follower > b_follower:
    return guess == "a"
  else :
    return guess == "b"


def game():
  """Game begins"""
  print(logo)
  score = 0
  game_comtinue=True
  a_person=data_selector()
  b_person=data_selector()

  while game_comtinue:
    a_person = b_person
    b_person=data_selector()
    
    while a_person == b_person:
      b_person = data_selector()

      print(f"Compare A: {details(a_person)}.")
      print(vs)
      print(f"Against B: {details(b_person)}.")

      guess= input("Who must have most followers? A or B : ").lower()
      a_follower=a_person['follower_count']
      b_follower=b_person['follower_count']

      result=follower_checker(guess, a_follower, b_follower)

      clear()
      print(logo)
      if result:
        score += 1
        print(f"You're right! Current score: {score}.")
      else:
        game_comtinue = False
        print(f"Sorry, that's wrong. Final score: {score}")

game()
      
