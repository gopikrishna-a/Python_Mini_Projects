import getpass

print "please choose your choice in Rock, Paper or Scissors"
player_one = getpass.getpass("Enter player one's choice: ")
player_two = getpass.getpass("Enter player two's choice: ")
print player_one
print player_two

if player_one == "Rock" and player_two == "Rock":
    print("Match Draw!!")
elif player_one == "Rock" and player_two == "Paper":
    print("player two wins!!")
elif player_one == "Rock" and player_two == "Scissors":
    print("player one wins!!")
elif player_one == "Paper" and player_two == "Paper":
    print("Match Draw!!")
elif player_one == "Paper" and player_two == "Rock":
    print("player one wins!!")
elif player_one == "Paper" and player_two == "Scissors":
    print("player two wins!!")
elif player_one == "Scissors" and player_two == "Scissors":
    print("Match Draw!!")
elif player_one == "Scissors" and player_two == "Rock":
    print("player two wins!!")
elif player_one == "Scissors" and player_two == "Paper":
    print("player one wins!!")
else:
    print("Something went wrong!!!")
