#File: exercise_13.py
#Description: using time to calculate the falling distance
#Assignment Number: chapter4-13
#Kevin Liu
#Github<barbqueen>

def falling_distance(t):
    displacement = 4.9 * t * t
    return displacement

def main():
    print('The falling distance when time is equal to 1-10 is as following:')
    for t in range(1,11):
        distance = falling_distance(t)
        print(distance)
main()