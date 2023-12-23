#File: exercise_1.py
#Description: Create a class of a pet, ask the user to give the information and printout the information
#Assignment Number: chapter10-1
#Kevin Liu
#Github<barbqueen>

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    my_pet = Pet("", "", 0)

    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of animal (Dog, Cat, Bird): ")
    age = int(input("Enter the age of your pet: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print("\nPet Details:")
    print("Name:", my_pet.get_name())
    print("Animal Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

if __name__ == "__main__":
    main()
