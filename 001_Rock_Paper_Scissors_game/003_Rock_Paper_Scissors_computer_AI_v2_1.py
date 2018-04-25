import getpass
import random
import string

print("please choose your choice in Rock, Paper or Scissors")
player = string.capitalize(getpass.getpass("Enter Your choice: "))
computer = random.choice(['Rock', 'Paper', 'Scissors'])
print("Your choice is: %s" %(player))
print("Computer choice is: %s" %(computer))
if player == computer:
    print("Match Draw!!")
elif player == "Rock":
   if computer == "Paper":
        print('Computer Won The Game')
   if computer == "Scissors":
        print('You Won The Game')
elif player == "Paper":
    if computer == "Rock":
        print('You Won The Game')
    if computer == "Scissors":
        print('Computer Won The Game')
elif player == "Scissors":
    if computer == "Rock":
        print('Computer Won The Game')
    if computer == "Paper":
        print('You Won The Game')
else:
    print("Something went wrong!!!")

