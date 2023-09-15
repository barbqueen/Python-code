number = int(input("Enter a pocket number from 0 - 36: "))

if 0 <= number <= 36:
    if number == 0:
        color = "green"
    elif (1 <= number <= 10) or (19 <= number <= 28):
        color = "red" if number % 2 == 1 else "black"
    else:
        color = "black" if number % 2 == 1 else "red"
    
    print('The color is: ', color)
else:
    print("Please enter a number within the range of 0 through 36.")