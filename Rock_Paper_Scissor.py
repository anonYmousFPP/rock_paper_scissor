import random

playAgain = 'yes'

while (playAgain != 'no'):

    choices = ['rock', 'paper', 'scissor']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Choose one- rock, paper, or scissor ? ').lower()

    if player == computer:
        print('computer: ', computer)
        print('Player: ', player)
        print('Tie!')
    elif (computer == 'rock' and player == 'paper') or (computer == 'paper' and player == 'scissor') or (computer == 'scissor' and player == 'rock'):
        print('computer: ', computer)
        print('Player:', player)
        print('You Win👍')

    else:
        print('computer: ',computer)
        print('Player:', player)
        print('You Loose😢')

    playAgain = input('Wanna Play Again? (Type No for quit)').lower()
    if playAgain == 'no':
        break

print('You Played Well')