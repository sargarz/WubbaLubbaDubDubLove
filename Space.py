import math


# 1 class
# 1 built in decorator @classmethod
# string representation
# 1 method
class Alien():
    aliens_dating = 0

    def __init__(self, name, species, galaxy: "Galaxy", intergalactic_number):

        self._species = species # protected attirubut
        self.galaxy = galaxy #public attribute
        self.__intergalactic_number = intergalactic_number
 

        self.name = name # does name become the username?


        Alien.aliens_dating += 1 # keeps track of total aliens

    @property
    def species(self):
        return self._species
    
    @property
    def intergalactic_number(self):
        return self.__intergalactic_number
    

    @classmethod
    def aliens_in_total(cls):
        return f"Total number of registered aliens is {cls.aliens_dating}"
    
    def __str__(self):
        presentation = f"I am allient named {self.name}, my species is {self.species} and I am from {self.galaxy} galaxy"
        return presentation
    





#class human
    # 1 class
    # 1 built in decorator @classmethod
    # string representation
    # 1 method


class Human:
    humans_dating = 0

    def __init__(self, name, password, species, galaxy, number):
        super().__init__(password)
        self._name = name # protected attribute
        self.__number = number # private attribute
        self.species = species # public attribute
        self.galaxy = galaxy

        #static method
        Human.humans_dating += 1

    @property
    def number(self):
        return self.__number
    
    @classmethod
    def humans_in_total(cls):
        return f"Total number of registered aliens is {cls.humans_dating}"
    

    def __str__(self):
        return f"I am human, i am from milky way and my name is {self.name}"


#class galaxy
    #with * and + and -
    # stores coordinates and names of the galaxy
    # we use the euclidead distance formula to calculate the distance between two galaxies




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
        return f"I am {self.name} galaxy and my coordinates are: {self.coordinates}"


    #idk do we keep it in galaxy class or do we put it outside so there is more class interactions
    def calculate_distance_to(self, another_galaxy: "Galaxy"):
        """Returns the distance between the self galaxy and another galaxy"""
        self_coordinates = self.coordinates()
        another_galaxy_coordinates = another_galaxy.coordinates()

        # defining this so the formula is shorter

        x1, y1, z1 = self_coordinates
        x2, y2, z2 = another_galaxy_coordinates


        distance = math.sqrt((x1 - x2)**2     +     (y1 - y2)**2    +      (z1 - z2)**2)
        return distance









class Compatability_calculator:
    print("kferfberbhj")
    #checks the distance and other factors to determine compatability
    # distance check uses < > / == *



# class that handles user interface with passwords and shit 



#class or method idk that changes the profile






















