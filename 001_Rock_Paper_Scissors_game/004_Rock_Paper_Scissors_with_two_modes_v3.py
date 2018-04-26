import getpass
import random
import pdb
#pdb.set_trace()
def one_player_mode(player_one, player_two, name_one, name_two):
    if player_one == player_two:
        return 'Match Draw!!'
    elif player_one == "Rock":
        if player_two == "Paper":
            return '%s wins!!' %(name_two)
        if player_two == "Scissors":
            return '%s wins!!' %(name_one)
    elif player_one == "Paper":
        if player_two == "Rock":
            return '%s wins!!' %(name_one)
        if player_two == "Scissors":
            return '%s wins!!' %(name_two)
    elif player_one == "Scissors":
        if player_two == "Rock":
            return '%s wins!!' %(name_two)
        if player_two == "Paper":
            return '%s wins!!' %(name_one)
    else:
        return 'Something went wrong!!'

if __name__ == '__main__':
    print('*' * 20 + 'Rock' + '*' * 20)
    print('*' * 20 + 'Paper' + '*' * 19)
    print('*' * 18 + 'Scissors' + '*' * 18)
    print('Choose Game Mode')
    print('Enter 1 for one player game')
    print('Enter 2 for two player game')
    mode = int(input('Game Mode: '))
    if mode == 1:
        player_one = getpass.getpass("Enter Your choice: ").capitalize()
	computer = random.choice(['Rock', 'Paper', 'Scissors'])
        print(player_one)
	print(computer)
	player_name = 'You'
	computer_name = 'Computer'
	result = one_player_mode(player_one, computer, player_name, computer_name)
        print(result)
    elif mode == 2:
        player_one = getpass.getpass("Enter player one's choice: ").capitalize()
        player_two = getpass.getpass("Enter player two's choice: ").capitalize()
        print(player_one)
        print(player_two)
	player_one_name = 'Player one'
	player_two_name = 'Player two'
        result = one_player_mode(player_one, player_two, player_one_name, player_two_name)
        print(result)
    else:
        print('Please choose the correct game mode!!')
