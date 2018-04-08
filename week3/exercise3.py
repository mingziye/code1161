"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    "return ""You got it!"""

if __name__ == "__main__":
    advancedGuessingGame()

print ("Welcome to the guessing game!")
x=input("Set a lower bound: ")
while True:
    try:
        x= int(x)
        break
    except ValueError:
        x=input('Set a lower bound again: ')
        continue
y=input("Set a higher bound: ")
while True:
    try:
        y = int(y)
        while True:
            if int(y)>int(x):
              break
            else:
              y=input("The number should bigger than the low bound, try again: ")
        break
    except ValueError:
        y=input('Set a higher bound again: ')
        continue
print ("Now, guess a number between "+str(x)+" and "+str(y))
actualNumber = random.randint(int(x), int(y))
guessed = False
while not guessed:
    guessedNumber = input("guess a number: ")
    while True:
        try: 
            guessedNumber=int(guessedNumber)
            break
        except ValueError:
            guessedNumber=input('You should enter a number to guess: ')
            continue
    print("you guessed {},".format(guessedNumber),)
    if int(guessedNumber) == int(actualNumber):
        print("you got it! It was {}".format(actualNumber))
        guessed = True
    elif int(guessedNumber) < int(actualNumber):
        print("too small, try again ")
    else:
        print("too big, try again  ")  
if __name__ == "__main__":
    advancedGuessingGame()
