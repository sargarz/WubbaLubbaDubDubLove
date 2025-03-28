import math


class Profile:
    def __init__(self, name, species, interests):
        self._name = name
        self.species = species
        self.interests = interests
        
    @property
    def name(self):
        return self._name
    
    def display_interests(self):
        interests_string = f"Interests: {self.interests}"
        return interests_string
    
    def get_information(self):
        info_string = f"Name: {self.name} \n Species: {self.species}"
        return info_string

    def __str__(self): 
        return f"My name is {self.name}, I am {self.species} and my special interests are {self.interests}"



class Alien(Profile):
    aliens_dating = 0

    def __init__(self, name, interests, galaxy, intergalactic_number):
        super().__init__(name, "Alien", interests)
        #inherits:
        #name
        #species
        #interests

        #alien attributes:

        self._galaxy = galaxy #protecte attribute, since the address should be private
        self.__intergalactic_number = intergalactic_number #private attribute highest security

        Alien.aliens_dating += 1 # keeps track of total aliens

    @property
    def galaxy(self):
        return self._galaxy
    
    @galaxy.setter
    def galaxy(self, new_galaxy):
        self._galaxy = new_galaxy
    
    @property
    def intergalactic_number(self):
        return self.__intergalactic_number
    
    

    @classmethod
    def aliens_in_total(cls):
        return f"Total number of registered aliens is {cls.aliens_dating}"
    
    #overridden method from class Profile
    def display_interests(self):
        interest_presentation = f"I am from {self.galaxy} and these are my interests: {self.interests}"
        return interest_presentation
    
    #another overridden method from class Profile
    def get_information(self):
        information = f"I am an Alien and my name is {self.name}"
        return information

    def __str__(self):
        presentation = f"{self.get_information} \n{self.display_interests()}"
        return presentation
    





class Human(Profile):
    humans_dating = 0

    def __init__(self, name, interests, country, number):
        super().__init__(name, "Human", interests)
        #from class User inherits attribute name, species interests

        self.__number = number # private attribute
        self._country = country # protected attribute


        
        Human.humans_dating += 1

    @property
    def country(self):
        return self._country
    

    @property
    def number(self):
        return self.__number
    
    @classmethod
    def humans_in_total(cls):
        return f"Total number of registered humans is {cls.humans_dating}"
    

    
    def display_interests(self): #overridden method
        return f"I am from {self.country} and these are my interests: {self.interests}"

    def get_information(self):
        return f"I am Human from planet earth that is in Milkyway galaxy and my name is {self.name}"

    
    def __str__(self):
        return f"{self.get_information}\n{self.display_interests}"





class Galaxy:
    def __init__(self, name, type, x, y, z):

        self.name = name

        #either can be eliptical or spiral or irregular
        self.type = type

        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        """puts the coordinates into a tuple"""
        # returns the coordinates or the galaxy
        return (self.x, self.y, self.z)
    
    def __str__(self):
        return f"I am {self.name} galaxy and my coordinates are: {self.coordinates()}"


    def calculate_distance_to(self, another_galaxy: "Galaxy"):
        """Returns the distance between the self galaxy and another galaxy"""
        self_coordinates = self.coordinates()
        another_galaxy_coordinates = another_galaxy.coordinates()

        # defining this so the formula is shorter

        x1, y1, z1 = self_coordinates
        x2, y2, z2 = another_galaxy_coordinates


        distance = math.sqrt((x1 - x2)**2     +     (y1 - y2)**2    +      (z1 - z2)**2)
        return distance



























