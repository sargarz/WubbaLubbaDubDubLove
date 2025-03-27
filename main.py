from read_database import ReadGalaxy


#getter method
#setter method
# 1 class
# 1 method


reader = ReadGalaxy("galaxy_database.txt")  # Create an instance
galaxies = reader.load_galaxies()
for galaxy in galaxies:
    print(galaxy)