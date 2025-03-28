from read_database import Data
import Space
from read_database import Data
from application import Application
import tkinter as tk


database = Data("galaxy_database.txt", "user_database.txt")


def generate_user():
        
    """Asks user for information and then returns either a human object or an alien object"""
    print("Welcome to the intergalactic dating app")
    print("pls give us information about yourself")
    name = input("What is your name? ")
    interests = input("Tell us about yourself! What are your interests?: ")
    
    species = input("Are you an alien or a human? (alien/human): ").lower()
    if species == "alien":
        number = input("what is your intergalactic phone number?")
        print("Our dating app is only awailable in the following galaxies:")

        reader = database.load_galaxies()# Create an instance 
        galaxies = reader.load_galaxies()
        galaxy_names = []
        for galaxy in galaxies:
            print(galaxy.name)
            galaxy_names.append(galaxy.name)
        
        print("\n")
        galaxy = input("Please input one of the names of the galaxy: ")
        if galaxy in galaxy_names:
            return Space.Alien(name, interests, galaxy, number )
        else:
            print("OUR DATING APP IS NOT AVAILABLE IN YOUR GALAXY :P")
    if species == "Human":
        number = input("what is your phone number?")
        country = print("Which country are you from?")
        return Space.Human(name, interests, country, number)


#user_profile = generate_user()
#if user_profile:
#    print("\nProfile created successfully!")
#    print(user_profile)





galaxies = database.load_galaxies()
print("\n Loaded Galaxies:")
for galaxy in galaxies:
    print(galaxy)

users = database.load_user_data()
print("\n Loaded Users:")
for user in users:
    print(user)




if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root, database)  # Fixed the class name
    root.mainloop()