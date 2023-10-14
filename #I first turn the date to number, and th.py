#I first turn the date to number, and then add the days to skip, and get the number after adding the skip days and turn it to a date

def main():
    month = input('Please enter a month:')
    day = int(input('Please enter a day:'))
    year = int(input('Please enter a yaer:'))
    skip_day = int(input('Please enter the days you want to skip(between 1-20):'))
    count = check_leap_year(year)
    
    leap_year_month = {'January': 31, 'February': 60,'March': 91, 'April': 121, 'May': 152, 'June': 182, 'July': 213, 'August': 244, 'September': 274, 'October': 305, 'November': 335,
        'December': 366}
    nonleap_year_month = {'January': 31, 'February': 59,'March': 90, 'April': 120, 'May': 151, 'June': 181, 'July': 212, 'August': 143, 'September': 173, 'October': 304, 'November': 334,
        'December': 365}
    
    x = check_total_days(month, leap_year_month, nonleap_year_month, count, day) + skip_day
    y = check_year(x, skip_day, count)
    w,v = check_which_month(x,y,count)
    


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

def check_year(x, skip_day, count):
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
        
def check_which_month(x, y, count):
    if count == 2:
        if 0 < x <= 31:
            new_month = 'January'
            new_date = x
        elif 31 < x <= 60:
            new_month = 'February'
            new_date = x - 31
        elif 60 < x <= 91:
            new_month = 'March'
            new_date = x - 60
        elif 91 < x <= 121:
            new_month = 'April'
            new_date = x - 91
        elif 121 < x <= 152:
            new_month = 'May'
            new_date = x - 121
        elif 152 < x <= 182:
            new_month = 'June'
            new_date = x - 152
        elif 182 < x <= 213:
            new_month = 'July'
            new_date = x - 182
        elif 213 < x <= 244:
            new_month = 'August'
            new_date = x - 213
        elif 244 < x <= 274:
            new_month = 'September'
            new_date = x - 244
        elif 274 < x <= 305:
            new_month = 'October'
            new_date = x - 274
        elif 305 < x <= 335:
            new_month = 'November'
            new_date = x - 305
        elif 335 < x <= 366:
            new_month = 'December'
            new_date = x - 335
        else:
            month = 'January'
            new_date = x - 366
    else: 
        if 0 < x <= 31:
            new_month = 'January'
            new_date = x
        elif 31 < x <= 59:
            new_month = 'February'
            new_date = x - 31
        elif 59 < x <= 90:
            new_month = 'March'
            new_date = x - 60
        elif 90 < x <= 120:
            new_month = 'April'
            new_date = x - 91
        elif 120 < x <= 151:
            new_month = 'May'
            new_date = x - 121
        elif 151 < x <= 181:
            new_month = 'June'
            new_date = x - 152
        elif 181 < x <= 212:
            new_month = 'July'
            new_date = x - 182
        elif 212 < x <= 243:
            new_month = 'August'
            new_date = x - 213
        elif 243 < x <= 273:
            new_month = 'September'
            new_date = x - 244
        elif 273 < x <= 304:
            new_month = 'October'
            new_date = x - 273
        elif 304 < x <= 334:
            new_month = 'November'
            new_date = x - 304
        elif 334 < x <= 365:
            new_month = 'December'
            new_date = x - 334
        else:
            month = 'January'
            new_date = x - 365
    return new_month, new_date





main()
    



