import Space


class Data:
    """Class that keeps track of data, it has following methods:
    
    - load_galaxies()  this method loads a list of galaxy objects from txt file
    - load_user_data()  this one loads users and returns a list of objects that are either alien or human"""

    def __init__(self, galaxy_data, user_data):
        self.__galaxy_data = galaxy_data    #encapsulated attribute
        self.__user_data = user_data        #encapsulated attribute

    


    def load_galaxies(self):
        """Returns a list of galaxy type objects"""
        galaxies = []
        with open(self.__galaxy_data, "r") as file:
            for line in file:
                components = line.strip().split(", ")
                if len(components) != 5:
                    continue

                name, galaxy_type, x, y, z = components
                x = int(x)
                y = int(y)
                z = int(z)

                galaxy = Space.Galaxy(name, galaxy_type, x, y, z)
                galaxies.append(galaxy)
            return galaxies


    def load_user_data(self):
        """Returns a list of users, that are either human or alien"""
        user_list = []

        with open(self.__user_data, "r") as file:
            for line in file:
                components = line.strip().split(", ")
                if len(components) != 5:
                    continue
                else:
                    name, species, interests, place, number = components
                    if species.lower() == "alien":
                        user_list.append(Space.Alien(name, interests, place, number))
                    elif species.lower() == "human":
                        user_list.append(Space.Human(name, interests, place, number))
        return user_list
                    