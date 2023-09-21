#File: exercise_2.py
#Description: using recusion to use adding to get the multipication
#Assignment Number: chapter12-2
#Kevin Liu
#Github<barbqueen>

def multiplication(x, y):
    if x > 0:
        return y + multiplication(x-1,y)
    else:
        return 0
 
def main():
    x = int(input('Please enter a positive integer:'))
    y = int(input('Please enter a positive integer:'))
    result = multiplication(x,y)
    print('The answer is:', result)
main()
    