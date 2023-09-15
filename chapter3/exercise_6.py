day = int(input('Please enter the day'))
month = int(input('Please entet the month'))
year = int(input('Please enter the last 2 digits oft the year'))

if day*month == year:
    print('It is a magic day')
else:
    print('The date is not magic')