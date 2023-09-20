#File: exercise_7.py
#Description: calculate the salary giving the day
#Assignment Number: chapter4-7
#Kevin Liu
#Github<barbqueen>

days = int(input('Pleass enter the number of days:'))
salary = 0
x = 1

for a in range(1,days + 1):
    salary += x
    print('The salary is:' , x/100, 'in day', a)
    x *= 2
    

print('The total salary is:', salary/100)
