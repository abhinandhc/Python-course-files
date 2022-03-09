############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################



#Hint 1: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import os
clear = lambda: os.system('cls')
from art import blackjacklogo 
def deal_cards():
  """Returns a random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def compare(user_score,comp_score):
  if user_score == comp_score:
    return "Draw"
  elif comp_score== 0:
    return "Lose,the opponent has a Blackjack"
  elif user_score == 0:
    return "You win with a Blackjack"
  elif user_score > 21:
    return "You went over,You lose"
  elif comp_score >21:
    return "Opponent went over,You Win"
  elif user_score > comp_score:
    return "You Win"
  else:
    return "You Lose"
  
#Hint 2: Deal the user and computer 2 cards each using deal_card() and append().
def play():
  print(blackjacklogo)
  user_cards = []
  computer_cards = []
  gameover=False
  
  def calculate_score(cards):
    """Take a list and returns their sum"""
    if sum(cards) == 21 and len(cards)==2 :
      return 0
  
  
    
  #Hint 2: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
    
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  
  while not gameover:
  #Hint 3: Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  
  #Hint 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  
  #Hint 5: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    
    print(f"Your cards {user_cards} and your score {user_score}")
    print(f"Dealer first card {computer_cards[0]}")
    if user_score == 0 or comp_score == 0 or user_score > 21:
      gameover=True
    #Hint 6: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    
    else:
      userip=input("Type 'y' to continue or 'n' to quit : ")
      if userip == 'y':
        user_cards.append(deal_cards())
      else:
        gameover=True
  #Hint 7: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  
  #Hint 8: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while comp_score!=0 and comp_score<17:
    computer_cards.append(deal_cards())
    comp_score=calculate_score(computer_cards)
  
  print(f"\n Your final hand {user_cards} and your final score {user_score}")
  print(f"\n Computer final hand {comp_score} and Computer final score {comp_score}")
  print(compare(user_score, comp_score))
#Hint 9: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 10: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  while input("Type 'y' to play Black Jack or 'n' to Quit  ")=='y':
    clear()
    play()
