#File: exercise_7.py
#Description: calculate the income geenrated from ticket sales
#Assignment Number: chapter4-7
#Kevin Liu
#Github<barbqueen>

def income(A_seat_number, B_seat_number, C_seat_number):
    A_seat_income = A_seat_number * 20
    B_seat_income = B_seat_number * 15
    C_seat_income = C_seat_number * 10
    total_income = A_seat_income + B_seat_income + C_seat_income
    return total_income

def main():
    A_seat_number = int(input('Please enter the number of A seats:'))
    B_seat_number = int(input('Please enter the number of B seats:'))
    C_seat_number = int(input('Please enter the number of C seats:'))
    total = income(A_seat_number, B_seat_number, C_seat_number)
    print('The total income from these 3 kind of seats are:', total)
main()

