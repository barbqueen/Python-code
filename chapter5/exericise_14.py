#File: exercise_14.py
#Description: using mass and velocity to calculate the kinetic energy
#Assignment Number: chapter4-14
#Kevin Liu
#Github<barbqueen>

def kinetic_energy(mass, velocity):
    ke = 0.5 * mass * velocity ** 2
    return ke

def main():
    mass = float(input('Please enter the mass of the object:'))
    velocity = float(input('Please enter the velovity of the pbject:'))
    energy = kinetic_energy(mass, velocity)
    print('The kinetic energy of the objest is:', energy)
main()