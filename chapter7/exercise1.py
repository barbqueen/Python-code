#File: exercise_1.py
#Description: find the numbers, total and average
#Assignment Number: chapter7-1
#Kevin Liu
#Github<barbqueen>

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
total = 0
avarage = 0

for x in numbers:
    if 0 < x < 100:
        valid_numbers.append(x)
print('The new list is', valid_numbers)

for y in valid_numbers:
    total += y

avarage = round(total/len(valid_numbers),2) 
# I take 2 desmos numbers to make it neat here

print('The total is: ', total)
print('The avarage is: ', avarage)





    