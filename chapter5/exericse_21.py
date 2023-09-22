#File: exercise_21.py
#Description: paper sciccors and rock game
#Assignment Number: chapter4-21
#Kevin Liu
#Github<barbqueen>

import random
gesture = input('Please enter paper scissors or rock:')
number = random.randint(1,3)

if gesture == 'paper':
    if number == 1:
        print('You win!!!')
    elif number == 2:
        print('Try again.')
    else:
        print('You lose, good lukc next time.')

elif gesture == 'scissors':
    if number == 1:
        print('You lose, good lukc next time.')
    elif number == 2:
        print('You win!!!')
    else:
        print('Try again')

elif gesture == 'rock':
    if number == 1:
        print('Try again')
    elif number == 2:
        print('You lose, good luck next time.')
    else:
        print('You win!!!')
else:
    print('Only type in rock, scissors ,and rock.')

if number == 1:
    choice = 'rock'
elif number == 2:
    choice = 'paper'
else:
    choice = 'scissors'

print("The computer's choice is", choice)