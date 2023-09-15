people = int(input('Please enter the number people that will join the party'))
number = int(input('Please enter the amount of hotdog each person will eat'))

if people * number % 8  == 0 and people * number % 10 == 0 :
    packages = people * number / 8
    hotdogs = people * number / 10
    print('The minimum amount of hotdog packages needed is ', packages)
    print('The minimum amount of hotdogs needed is', hotdogs)
    print('The amount of hotdog packages that will be leftover is ', 0)
    print('The amount of hotdogs that will be leftover is ', 0)
elif people * number % 8 == 0 and people * number % 8 != 0:
    packages = people * number / 8
    hotdogs = int(people * number / 10) + 1
    hotdog_leftovers = (hotdogs * 10) % (people * number)
    print('The minimum amount of hotdog packages needed is ', packages)
    print('The minimum amount of hotdogs needed is', hotdogs)
    print('The amount of hotdog packages that will be leftover is ', 0)
    print('The amount of hotdogs that will be leftover is ', hotdog_leftovers)
elif people * number % 8 != 0 and people * number % 8 == 0:
    hotdogs = people * number / 10
    packages = int(people * number / 8) + 1
    package_leftovers = (packages * 8) % (people * number)
    print('The minimum amount of hotdog packages needed is ', packages)
    print('The minimum amount of hotdogs needed is', hotdogs)
    print('The amount of hotdog packages that will be leftover is ', package_leftovers)
    print('The amount of hotdogs that will be leftover is ', 0)
else:
    packages = int(people * number / 8) + 1
    hotdogs = int(people * number / 10) + 1
    packages = int(people * number / 8) + 1
    package_leftovers = (packages * 8) % (people * number)
    hotdog_leftovers = (hotdogs * 10) % (people * number)
    print('The minimum amount of hotdog packages needed is ', packages)
    print('The minimum amount of hotdogs needed is', hotdogs)
    print('The amount of hotdog packages that will be leftover is ', package_leftovers)
    print('The amount of hotdogs that will be leftover is ', hotdog_leftovers)









