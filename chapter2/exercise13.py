length = int(input('Please type in the length of the row in feet'))
space = int(input('Please type in the amount of space used bu an end-post assembly in feet'))
space_between_vines = int(input('Please enter the amount of space between the vines in feet'))

number = (length - 2*space)/space_between_vines
print('The number of grapevines that will fit in the roll is', number)