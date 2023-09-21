#File: exercise_4.py
#Description: using loops to draw the diagram showed
#Assignment Number: chapter4-14
#Kevin Liu
#Github<barbqueen>

def find_the_largest(list, x, length, largest):
    for x in list:
        if x > largest:
            largest = x
    return largest

def main():
    list = []
    stop = 1
    while stop != 999:
        value = int(input("enter value(exit with value 999):"))
        if value != 999:
            list.append(value)
        else:
            stop = 999
    length = int(len(list))
    x = 0
    largest = list[0]
    number = find_the_largest(list, x, length,largest)
    print('The largest number in the list is:', number)
main()

        

        
