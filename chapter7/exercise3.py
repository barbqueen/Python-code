#File: exercise_3.py
#Description: calculate the total and avarage amount of rainfall
#Assignment Number: chapter7-3
#Kevin Liu
#Github<barbqueen>

count = 0
rainfall = []
total = 0

while count < 12:
    x = float(input('Please entert the amount of rainfall:'))
    rainfall. append(x)
    count += 1

for y in rainfall:
    total += y

avarage = total/12

print('The total amount of rainfall during the 12 month is:', total) 
print('The avarage rainfall each month is:', avarage)

