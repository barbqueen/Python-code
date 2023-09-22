#File: exercise_6.py
#Description: calculate the total calorie
#Assignment Number: chapter4-6
#Kevin Liu
#Github<barbqueen>


def calories(fat, carb):
    calaries_from_fat = fat * 9
    calories_from_carb = carb * 4
    totol_calorie = calaries_from_fat + calories_from_carb
    return totol_calorie
    
def main():
    fat = float(input('Please enter the amount of fat you consume a day:'))
    carb = float(input('Please enter the amount of carb you consume a day:'))
    total = calories(fat, carb)
    print('The totle colaries from carb and fat is;', total)
main()
