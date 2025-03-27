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
        if available_profiles:
            return random.choice(available_profiles)
        else:
            return None

    def attempt_match(self):
        """ Show the user a random profile. If they pick 'match', randomize whether it's a match. """
        potential_match = self.pick_random_profile(self._database, self._attempted_profiles)

        if not potential_match:
            print("No new profiles available for matchmaking!")
            return None

        print("\n✨ Potential Match Found!")
        print(potential_match)  

        choice = input("Do you want to match? (yes/no): ").lower()

        if choice == "yes":
            match_result = random.choice([True, False])

            if match_result:
                print("\n It's a Match!")
                
                if isinstance(potential_match, Alien):
                    print(f"Here’s their intergalactic number: {potential_match.intergalactic_number}")
                elif isinstance(potential_match, Human):
                    print(f"Here’s their phone number: {potential_match.number}")
            else:
                print("\n They weren’t interested, better luck next time!")

        else:
            print("\n You skipped this match.")

        # Mark the profile as attempted
        self._attempted_profiles.add(potential_match)
        # Continue to the next match
        self.attempt_match()


# Load the database and profiles
database = Data("galaxy_database.txt", "user_database.txt") 

# Load profiles into the Match object
user_profiles = database.load_user_data() 

# Create a Match instance with loaded profiles
match_maker = Match(user_profiles)

# Start matching
match_maker.attempt_match()
