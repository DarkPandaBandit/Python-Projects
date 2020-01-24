#Author : Shaun Gaffney
#Date : 17-10-19
#Version: 1.0
#Guess the random number Game
#one player vs. the computer

import random
minguess = 1
maxguess = 6

#Ask the user for their name and thier Guess
name = input('What is your name? ')
print('Hi ' + name)
print('Enter a number between: ' + str(minguess), "and " + str(maxguess))
guess = int(input('What is your Guess? '))

#Generate a random number and tell the use if they won
secretnumber = random.randint(minguess, maxguess)
if (guess == secretnumber):
    print('Congratulations, you got it right')
else:
    print('You lose - the number was', str(secretnumber))
print('Thank you for playing Guess the Number.')
