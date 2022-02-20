from random import shuffle

def shufflelist(mylist):
  shuffle(mylist)
  return mylist

def playerguess():
  guess=" "
  while guess not in [0,1,2]:
    guess = input("Select a number from the list - 0, 1,2   :")
    return int(guess)


def checkg(mylist,guess):
  if mylist[guess] == "O":
    print("Correct")
  else:
    print("Wrong!")
  print(mylist)

mylist=[" ","O"," "]

mixlist=shufflelist(mylist)

guess=playerguess()

checkg(mixlist,guess)
