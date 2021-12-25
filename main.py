import random

__LIST__ = ['ROCK', 'PAPER', 'SCISSORS']
comp_play = usr_play = ''


def computer_play():
    global comp_play
    comp_play = random.choice(__LIST__)
    return comp_play


def user_play():
    global usr_play
    usr_play = input('Your turn: ').upper()
    return usr_play


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
        print('It´s a tie!')


def print_game():
    print(f'\nComputer played: {comp_play}\nUser played: {usr_play}')


def main():
    computer_play()
    user_play()
    check_winner()
    print_game()


if __name__ == '__main__':
    main()
