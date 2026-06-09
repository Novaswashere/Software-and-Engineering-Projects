class pet():

    def __init__(self,name):
        self.name = name
        self.happiness = 100
        self.hunger = 0

    def timePass(self):
        self.hunger += 5
        self.happiness -= 5

    def feed(self):
        self.hunger = 0
        print("Your pet is no longer hungery!")
        print("\n")
    def play(self):
        self.happiness += 15
        print(f" Your pet is happier!!")
        print("\n")

    def stats(self):
        print('\n')
        print(f"Happiness is {self.happiness}")
        print(f"Hunger Level is {self.hunger}")
        print("\n")


print("Welcome to Virtual Pet Simulator")
print('\n')

name = input("Please enter the name for your pet: ")
name2 = input("Please enter the name for your second pet: ")

pet1 = pet(name)
pet2 = pet(name2)

while True:

    print("------Menu------")
    print(" " * 100)
    print("Select on of the following options for any one of your pets to continue or enter 0 to quit the Menu")
    print(f"Please choose which pet: {name.capitalize()} or {name2.capitalize()}")
    print(" " * 100)
    print("1. Check Pet current stats")
    print("2. Play with Pet")
    print("3. Feed Pet")
    print("0. Enter 0 to quit. ")
    print(" " * 100)

    while True:
        petName = input("Please enter the name for your pet: ")
        if petName.lower() == name.lower() or petName.lower() == name2.lower():
            break

    option = int(input("Select your option: "))

    petName = petName.lower()
    name = name.lower()
    name2 = name2.lower()

    if option == 1:
        pet1.timePass()
        pet2.timePass()

        if petName == name:
            pet1.stats()
        else:
            pet2.stats()

            

    elif option == 2:
        pet1.timePass()
        pet2.timePass()

        if petName == name:
            pet1.play()
            
        else:
            pet2.play()
            

    elif option == 3:
        pet1.timePass()
        pet2.timePass()

        if petName == name:
            pet1.feed()
            
        else:
            pet2.feed()
            

    elif option == 0:
        print("Thanks for Playing our Virtual pet Simulator")
        break




