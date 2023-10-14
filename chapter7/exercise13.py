#File: exercise_13.py
#Description: maic 8 ball
#Assignment Number: chapter7-13
#Kevin Liu
#Github<barbqueen>

import random

infile = open('responses.txt','r')
answers = infile.readlines()
infile.close()
index = 0

while index < len(answers):
    answers[index] = answers[index]. rstrip('\n')
    index += 1

while True:
    x = input('Please enter a yes or no question(enter quit to quit):')
    y = random.randint(0,11)
    if x != 'quit':
        print(answers[y])
    else:
        break

print('You quit the game')



