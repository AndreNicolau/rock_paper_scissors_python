import random
import os

__LIST__ = ['ROCK', 'PAPER', 'SCISSORS']  # list of playable options
comp_play = usr_play = ''  # variables to computer and user playable options


# define global variable for computer play
# get and return random choice from __LIST__
def computer_play():
    global comp_play
    comp_play = random.choice(__LIST__)
    return comp_play


# define global variable for user play
# get and return user play variable
def user_play():
    global usr_play
    usr_play = input('Your turn: ').upper()
    return usr_play


# check who wins
def check_winner():
    if comp_play == 'ROCK' and usr_play == 'PAPER':
        print('User wins!')
    if comp_play == 'ROCK' and usr_play == 'SCISSORS':
        print('Computer wins!')
    if comp_play == 'PAPER' and usr_play == 'SCISSORS':
        print('User wins!')
    if comp_play == 'PAPER' and usr_play == 'ROCK':
        print('Computer wins!')
    if comp_play == 'SCISSORS' and usr_play == 'ROCK':
        print('User wins!')
    if comp_play == 'SCISSORS' and usr_play == 'PAPER':
        print('Computer wins!')
    elif comp_play == usr_play:
        print('It`s a tie!')


# print what computer played
# print what player played
def print_game():
    print(f'\nComputer played: {comp_play}')
    print(f'User played: {usr_play}')


def main():
    computer_play()
    user_play()
    check_winner()
    print_game()


if __name__ == '__main__':
    os.system('cls')  # clear terminal
    main()
