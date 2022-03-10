#Number Guessing Game Objectives:
# Include an ASCII art logo.
import random
from art import guessgame
print(guessgame)
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
Easyturns=10
Hardturns=5

def checking(user_guess,system_choice,turns):
  """Checkng the user guess to the system choice and returning the remaining turns"""
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  if user_guess > system_choice:
    print("Too High")
    return turns -1
  elif user_guess < system_choice:
    print("Too Low")
    return turns -1
  # If they got the answer correct, show the actual answer to the player.
  else:
    print(f"Correct!!\nThe actual number is {system_choice}")
    return

def modeselection():
  """Function for selecting the mode"""
  mode=input("Type 'easy' for Easy mode or 'hard' for Hard mode  : ")
  if mode=='easy':
    return Easyturns
  elif mode== 'hard':
    return Hardturns  
  else:
    print("Invalid input")

def guessgame():  
  print("Welocme to the Guess the number game\nIam thinking of a number btw 1 and 100")
  system_choice=random.randint(1,100)
  turns=modeselection()
  # Track the number of turns remaining.
  user_guess = 0
  while user_guess != system_choice:
    print(f"You have {turns} number of turns")
    user_guess=int(input("Guess a number between 1 and 100  :"))
    # Allow the player to submit a guess for a number between 1 and 100.
    turns=checking(user_guess, system_choice,turns)
    
  # If they run out of turns, provide feedback to the player. 
    if turns == 0:
      print("You ran out of turns,You Lose")
      return
guessgame()
