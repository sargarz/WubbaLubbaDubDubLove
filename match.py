import random
from read_database import Data  
from Space import Alien, Human

class Match:
    def __init__(self, database):
        """Initialize with a list of profiles (aliens and humans)."""
        self._database = database  
        self._attempted_profiles = set() 

    @property
    def database(self):
        """Getter for the database to allow controlled access."""
        return self._database

    @staticmethod
    def pick_random_profile(database, attempted_profiles):
        """Randomly selects a profile from the database that hasn't been attempted yet."""
        available_profiles = [profile for profile in database if profile not in attempted_profiles]
        return random.choice(available_profiles) if available_profiles else None

    def attempt_match(self):
        """Returns the selected match and randomly determines if it's a match or not."""
        potential_match = self.pick_random_profile(self._database, self._attempted_profiles)

        if not potential_match:
            return None

        match_result = random.choice([True, False])  
        self._attempted_profiles.add(potential_match)
        return potential_match, match_result
    
    def __str__(self):
        """String representation of the Match object."""
        return f"Match object with {len(self._database)} potential matches"


# Load the database and profiles
database = Data("galaxy_database.txt", "user_database.txt") 

# Load profiles into Match object
user_profiles = database.load_user_data()  

# Create a Match instance with loaded profiles
match_maker = Match(user_profiles)

# Start matching
match_maker.attempt_match()
