from Space import Galaxy
import os

class ReadGalaxy:
    def __init__(self, filename):
        self.filename = filename


    def load_galaxies(self):
        """Returns a list of galaxy type objects"""
        galaxies = []
        with open(self.filename, "r") as file:
            for line in file:
                components = line.strip().split(", ")
                if len(components) != 5:
                    continue

                name, galaxy_type, x, y, z = components
                x = int(x)
                y = int(y)
                z = int(z)

                galaxy = Galaxy(name, galaxy_type, x, y, z)
                galaxies.append(galaxy)
            return galaxies









