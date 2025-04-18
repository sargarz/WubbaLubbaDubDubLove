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

        # Display the total number of humans and aliens
        if isinstance(potential_match, Human):
            print(Human.humans_in_total())  # Display total humans
        elif isinstance(potential_match, Alien):
            print(Alien.aliens_in_total())  # Display total aliens

        # Randomly determines if it's a match or not
        match_result = random.choice([True, False])  
        self._attempted_profiles.add(potential_match)
        return potential_match, match_result
    
    def __str__(self):
        """String representation of the Match object."""
        return f"Match object with {len(self._database)} potential matches"



database = Data("galaxy_database.txt", "user_database.txt") 


user_profiles = database.load_user_data()  

match_maker = Match(user_profiles)

match_maker.attempt_match()
