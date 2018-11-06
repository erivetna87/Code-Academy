"""
Codecademy - Learn Python
Number Guess
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("What is your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum value of sides is %d" % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "Guess is invalid. Try again."
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d" % (first_roll)
    sleep(1)
    print "The second roll is %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "result..."
    sleep(1)
    print "The total roll was %d" % (total_roll)
    if total_roll > guess:
      print "You won!"
    else:
      print "You lose!"
    
roll_dice(6)
  
  
  
