#I first turn the date to number, and then add the days to skip, and get the number after adding the skip days and turn it to a date

def main():
    month = input('Please enter a month:')
    day = int(input('Please enter a day:'))
    year = int(input('Please enter a yaer:'))
    skip_day = int(input('Please enter the days you want to skip(between 1-20):'))
    count = check_leap_year(year)
    x = check_total_days(month, leap_year_month, nonleap_year_month, count, day)
    y = check_year(x, skip_day, count, x)









    leap_year_month = {'January': 31, 'February': 60,'March': 91, 'April': 121, 'May': 152, 'June': 182, 'July': 213, 'August': 244, 'September': 274, 'October': 305, 'November': 335,
        'December': 366}
    nonleap_year_month = {'January': 31, 'February': 59,'March': 90, 'April': 120, 'May': 151, 'June': 181, 'July': 212, 'August': 143, 'September': 173, 'October': 304, 'November': 334,
        'December': 365}
    


def check_leap_year(year):   #check for leap year
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return 1
    else:
        return 2

def check_total_days(month, leap_year_month, nonleap_year_month, count, day): 
    if count == 1:
        total_days = day + leap_year_month(month)
    else:
        total_days = day + nonleap_year_month(month)
    return total_days

def check_year(x, skip_day, count,):
    if count ==1:
        if x + skip_day <= 366:
            return 1
        else:
            return 2
    else:
        if x + skip_day <= 365:
            return 1
        else:
            return 2
        
def check_date(x, y):
    if y == 1:
        if 0 < x <= 31:
            new_month = 'January'
        elif 31 < x <= 60:
            new_month = 'February'
        elif 60 < x <= 91:
            new_month = 'March'
        elif 91 < x <= 121:
            new_month = 'March'


        

    
main()
    



