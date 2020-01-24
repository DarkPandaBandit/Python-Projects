#Author : Shaun Gaffney
#Date :
#Version: 1.0
#
#Rock Paper Scissors Game
#Two player

print('Welcome to Rock, Paper, Scissors!')
print("Let's Begin ...")
name1 = input("Player 1: What's your name? ")
name2 = input("Player 2: What's your name? ")

print("Hello", str(name1), "and", str(name2))
print(str(name2) + ": Close your eyes")

#The input for Players choices
choice1 = input(str(name1) + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + str(name2), "to choose.\n\n\n")
choice2 = input(str(name2) + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

#The Outcome of the players choices.
if (choice1 == 'r' and choice2 == 'p') or (choice1 =='p' and choice2 =='s') or (choice1 == 's' and choice2 == 'r'):
    print(name2, "Wins The Game")
elif (choice1 == 'p' and choice2 == 'r') or (choice1 =='s' and choice2 =='p') or (choice1 == 'r' and choice2 == 's'):
    print(name1, "Wins The Game")
elif (choice2 == 'p' and choice1 == 'r') or (choice2 =='s' and choice1 =='p') or (choice2 == 'r' and choice1 == 's'):
    print(name1, "Wins The Game")
elif (choice2 == 'r' and choice1 == 'p') or (choice2 =='p' and choice1 =='s') or (choice2 == 's' and choice1 == 'r'):
    print(name2, "Wins The Game")
elif choice2 == choice1:
    print("It's a tie try again\n\n ")

print("Thanks for playing Rock, Paper, Scissors")
