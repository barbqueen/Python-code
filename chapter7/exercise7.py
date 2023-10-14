#File: exercise_7.py
#Description: Driver's License Exam
#Assignment Number: chapter7-7
#Kevin Liu
#Github<barbqueen>

infile = open('answer.txt','r')
numbers = infile.readlines()
infile.close()
index = 0

while index < len(numbers):
    numbers[index] = numbers[index]. rstrip('\n')
    index += 1

infile = open('student.txt', 'r')
x = infile.readlines()
infile.close()
y = 0

while y < len(x):
    x[y] = x[y]. rstrip('\n')
    y += 1

count = 0
wrong_answers = []
z = 0

while z < 19:
    if numbers[z] == x[z]:
        count += 1
    else:
        wrong_answers.append(z + 1)
    z += 1

wrong = 20 - count


if count >= 15:
    print('You pass the exam')
    print('You answered', count, 'questions correctly')
    print('You answered', wrong, 'questions correctly')
    print('The questions you get wrong is:', wrong_answers)
else:
    print('You fail the exam')
    print('You answered', count, 'questions correctly')
    print('You answered', wrong, 'questions correctly')
    print('The questions you get wrong is:', wrong_answers)
