#File: exercise_1.py
#Description: create a dictionary of moons and display the date of it when user calls it
#Assignment Number: chapter9-1
#Kevin Liu
#Github<barbqueen>


rad = {"Io": 1821.6, "Europa": 1560.8, "Ganymede": 2634.1, "Callisto": 2410.3}

gravity = {"Io": 1.796, "Europa": 1.314, "Ganymede": 1.428, "Callisto": 1.235}

orbital= {"Io": 1.769, "Europa": 3.551, "Ganymede": 7.154, "Callisto": 16.689}

a = input("Enter the name of a Galilean moon of Jupiter (Io, Europa, Ganymede, Callisto): ")

if a in rad and a in gravity and a in orbital:
    mean_radius = rad[a]
    surface_gravity = gravity[a]
    orbital_period = orbital[a]

    print(f"\n{a}'s Information:")
    print(f"Mean Radius: {mean_radius} kilometers")
    print(f"Surface Gravity: {surface_gravity} meters/second squared")
    print(f"Orbital Period: {orbital_period} days")
else:
    print("Invalid moon name. Please enter a valid name (Io, Europa, Ganymede, Callisto).")