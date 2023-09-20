#File: exercise_13.py
#Description: display the date and population
#Assignment Number: chapter4-13
#Kevin Liu
#Github<barbqueen>

starting_number = int(input('Please enter a starting number of organism:'))
avarage_daily_increase = float(input('Please enter the daily increase:'))
number_of_days = int(input('Please enter a number of days to multiply:'))

print('Day Approximate      Population')

for x in range(1,number_of_days + 1):
    population = starting_number * (1 + avarage_daily_increase) ** (x - 1)
    print(x,        population)
