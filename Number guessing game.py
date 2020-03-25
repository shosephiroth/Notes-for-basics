import math

import random

i = random.randint(1, 20)
guess = int(input("Enter an integer from 1 to 20"))
while i != "guess":
    print
    if guess < i:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 20"))
    elif guess > i:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 20"))
    else:
        print("You guessed it!")
        break

#Got this exercise from https://www.pythonforbeginners.com/code-snippets-source-code/python-guessing-game/
#I finished my sololearn tutorial on 3/3/20. Let this file serve as a benchmark for my progress going forward1