

# 1 class
# 1 built in decorator @classmethod
# string representation
# 1 method
class Alien:
    aliens_dating = 0

    def __init__(self, name, species, galaxy, interests):

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
    






#getter method
#setter method
# 1 class
# 1 method


class User():

    def __init__(self, password, username):
        self.__password = password
        self.username = username


    #getter method for accesing encapsulated password
    @property
    def password(self):
        return self.__password

    #setter method for instances where the user wants to change the password
    @password.setter
    def password(self, new_password):
        self.__password = new_password




#class human
    # 1 class
    # 1 built in decorator @classmethod
    # string representation
    # 1 method




#class galaxy
    #with * < > \ == to measure distance between galaxies




# class that handles user interface with passwords and shit 



#class or method idk that changes the profile






















