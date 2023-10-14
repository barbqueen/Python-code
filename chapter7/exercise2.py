"""  """#File: exercise_2.py
#Description: generate the digits of lottery
#Assignment Number: chapter7-2
#Kevin Liu
#Github<barbqueen>

import random
lottery_number = []
number = 1
count = 0
content = 0

while count < 7:
    number = random. randint(0,9)
    lottery_number. append(number)
    count += 1

for x in lottery_number:
    content = (content * 10) + x 
    #turn the values in the list to an integer

print('The lottery number is:', content)



