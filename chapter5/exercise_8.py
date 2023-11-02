#File: exercise_8.py
#Description: calculate the charges of painting the wall
#Assignment Number: chapter5-8
#Kevin Liu
#Github<barbqueen>

def paint(area,price):
    gallons = area/112
    print('You need', gallons, 'of paint to paint this wall.')

    hours = area*8/112
    print('You need', hours, 'hours of labor to complete painting this wall.')

    cost = gallons * price
    print('You need', cost, 'dollars to buy the paint.')

    charge = hours * 35
    print('You need', charge, 'dollars to pay for labor.')

    total_cost = cost + charge
    print('The total charge is:', total_cost, 'dollars.')
    
def main():
    area = float(input('Pleaase enter how many square feet of wall that need to be painted:'))
    price = float(input('Please enter the price of the paint per gallon:'))
    paint(area,price)
main()



