#File: exercise_12.py
#Description: calculate the factorial giving the number
#Assignment Number: chapter4-12
#Kevin Liu
#Github<barbqueen>

number = int(input('Please put in a nonnegative number:'))
factorial = 1
for x in range(1,number+1):
    factorial *= x
print('The factorial is:', factorial)