#File: exercise_6.py
#Description: generate random numbers and sort it
#Assignment Number: chapter5-6
#Kevin Liu
#Github<barbqueen>

import random
def main():
    x = int(input('Please enter how many numbers you want:'))
    number_of_throws = sorted(roll(x, 0, [], 0))
    print(number_of_throws)

def roll(x, y, z, count):
    while count < x:
        y = random. randint(1,6)
        z.append(y)
        count += 1
    return z

main()