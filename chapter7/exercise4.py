#File: exercise_4.py
#Description: show the lowest and largest number in the list
#Assignment Number: chapter7-4
#Kevin Liu
#Github<barbqueen>

count = 0
x = []
total = 0

while count < 20:
    y = int(input('Please enter a number:'))
    x.append(y)
    count += 1

for z in x:
    total += z

lowest_number = min(x)
largest_number = max(x)
avarage = total/20

print('The largest numbe in the lis is:', largest_number)
print('The lowest numbe in the lis is:', lowest_number)
print('The total is', total)
print('The avarage is', avarage)






