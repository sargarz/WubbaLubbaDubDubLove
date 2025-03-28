import tkinter as tk
from tkinter import messagebox
from Space import Alien, Human
from match import Match
from read_database import Data
from ui import UI


class Application:
    def __init__(self, master, database):
        self.master = master
        self.master.title("WubbaLubbaDubDubLove")
        self.master.geometry("400x600")  
        self.master.configure(bg="#06402B")

        self.database = database
        self.match_maker = None
        self.user_profile = None

        self.ui = UI(self.master, self)

        self.create_main_screen()

    def create_main_screen(self):
        """Main screen with buttons"""
        self.ui.clear_frame()

        self.ui.create_label("WubbaLubbaDubDubLove", font_size=24).pack(pady=40)

        self.ui.create_button("Create Account", self.create_account_screen)
        self.start_finding_button = self.ui.create_button(
            "Start Finding Matches", self.start_finding_matches, state=tk.DISABLED
        )

    def create_account_screen(self):
        """Displays the account creation form"""
        self.ui.clear_frame()

        self.ui.create_label("Create Your Profile", font_size=18).pack(pady=20)

        self.name_entry = self.ui.create_entry("Name:")
        self.interests_entry = self.ui.create_entry("Interests:")
        self.species_entry = self.ui.create_entry("Are you an Alien or Human?")
        self.extra_info_entry = self.ui.create_entry("Galaxy (if Alien) or Country (if Human):")
        self.number_entry = self.ui.create_entry("Phone/Intergalactic Number:")

        self.ui.create_button("Submit", self.submit_account)
        self.ui.create_button("Back", self.create_main_screen)

    def submit_account(self):
        """Processes account creation"""
        name = self.name_entry.get()
        interests = self.interests_entry.get()
        species = self.species_entry.get().lower()  # Convert species to lowercase
        extra_info = self.extra_info_entry.get().title()  # Convert galaxy to title case
        number = self.number_entry.get()

        allowed_galaxies = {"Milky Way", "Andromeda", "Triangulum", "Messier 87", "Sombrero", "Whirlpool", "Centaurus A"}

        if not number.isdigit():
            messagebox.showerror("Invalid phone number", "Please enter numbers only.")
            return

        if species == "alien":
            if extra_info not in allowed_galaxies:
                messagebox.showerror(
                    "Invalid galaxy",
                    "Please enter one of these: Milky Way, Andromeda, Triangulum, Messier 87, Sombrero, Whirlpool, Centaurus A."
                )
                return
            self.user_profile = Alien(name, interests, extra_info, number)
        elif species == "human":
            self.user_profile = Human(name, interests, extra_info, number)
        else:
            messagebox.showerror("Invalid species", "Please enter 'alien' or 'human'.")
            return

        messagebox.showinfo("Success", f"Welcome, {self.user_profile.name}! :P")
        self.create_matchmaking_screen()


    def create_matchmaking_screen(self):
        """Screen for matchmaking after account creation."""
        self.ui.clear_frame()

        self.ui.create_label(f"Welcome, {self.user_profile.name}!", font_size=18).pack(pady=20)

        self.ui.create_button("Find Matches", self.start_finding_matches)
        self.ui.create_button("Create New Account", self.create_account_screen)

    def start_finding_matches(self):
        """Starts the matchmaking process."""
        if not self.user_profile:
            messagebox.showerror("No profile", "You must create an account first.")
            return

        user_profiles = self.database.load_user_data()
        self.match_maker = Match(user_profiles)
        self.show_next_match()

    def show_next_match(self):
        """Displays the next match in same UI"""
        self.ui.clear_frame()

        match_result = self.match_maker.attempt_match()
        if match_result:
            self.show_match_ui(match_result)
        else:
            self.ui.create_label("Uh oh, no new matches available!", font_size=16).pack(pady=10)
            self.ui.create_button("Back", self.create_matchmaking_screen)

    def show_match_ui(self, match):
        """Displays the matched profile in the UI."""
        matched_profile = match[0]
        match_result = match[1]

        match_text = str(matched_profile)  

        self.ui.create_card(match_text)

        self.ui.create_button("Match", lambda: self.process_match("match", match, match_result))
        self.ui.create_button("Pass", lambda: self.process_match("pass", match, match_result))

    def process_match(self, choice, match, match_result):
        """Processes the user's decision and updates the UI."""
        self.ui.clear_frame()

        if choice == "match":
            if match_result:
                result_text = "It's a match! :D"
                matched_profile = match[0]
                result_text += f"\nTheir phone number is: {matched_profile.number if isinstance(matched_profile, Human) else matched_profile.intergalactic_number}"
            else:
                result_text = "Aw man, it's not a match :("
        else:
            result_text = "You passed on this match."

        self.ui.create_label(result_text, font_size=16).pack(pady=10)

        self.ui.create_button("Find Another Match", self.show_next_match)
        self.ui.create_button("Back to Menu", self.create_matchmaking_screen)
