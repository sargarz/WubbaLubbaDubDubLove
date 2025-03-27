import math

# 1 class
# 1 built in decorator @classmethod
# string representation
# 1 method
class Alien:
    aliens_dating = 0

    def __init__(self, name, species, galaxy: Galaxy, interests):

        self._species = species # protected
        self.galaxy = galaxy
        self.interests = interests

        self.name = name # does name become the username?


        Alien.aliens_dating += 1 # keeps track of total aliens


    @classmethod
    def aliens_in_total(cls):
        return f"Total number of registered aliens is {cls.aliens_dating}"
    
    def __str__(self):
        presentation = f"I am allient named {self.name}, i am from {self.galaxy} galaxy and my interests are {self.interests}"
        return presentation
    








#class human
    # 1 class
    # 1 built in decorator @classmethod
    # string representation
    # 1 method




#class galaxy
    #with * < > \ == to measure distance between galaxies
    # stores coordinates and names of the galaxy
    # we use the euclidead distance formula to calculate the distance between two galaxies

class Galaxy:
    def __init__(self, name, x, y, z):

        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        """puts the coordinates into a tuple"""
        # returns the coordinates or the galaxy
        return (self.x, self.y, self.z)


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
    #checks the distance and other factors to determine compatability




# class that handles user interface with passwords and shit 



#class or method idk that changes the profile






















