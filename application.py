import tkinter as tk
from tkinter import messagebox

from Space import Alien, Human
from match import Match
from read_database import Data
import random  # Add this import for randomness


class Application:
    def __init__(self, master, database):
        self.master = master
        self.master.title("Intergalactic Dating App")
        self.master.geometry("400x500")
        self.master.configure(bg="#2ECC71")  # Green background

        self.database = database
        self.match_maker = None
        self.user_profile = None

        self.main_frame = tk.Frame(self.master, bg="#2ECC71")
        self.main_frame.pack(fill="both", expand=True)

        self.create_main_screen()

    def create_main_screen(self):
        """Main screen with welcome message and buttons."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.main_frame,
            text="Intergalactic Dating ",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2ECC71",
        ).pack(pady=20)

        self.create_styled_button("Create Account", self.create_account_screen)
        self.start_finding_button = self.create_styled_button(
            "Start Finding Matches", self.start_finding_matches, state=tk.DISABLED
        )

    def create_styled_button(self, text, command, state=tk.NORMAL):
        """Creates a modern styled button."""
        button = tk.Button(
            self.main_frame,
            text=text,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#2ECC71",
            width=20,
            height=2,
            bd=0,
            relief="ridge",
            highlightthickness=0,
            command=command,
            state=state,
            activebackground="#27AE60",
            activeforeground="white",
        )
        button.pack(pady=10)
        return button

    def create_account_screen(self):
        """Displays the account creation form."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.main_frame,
            text="Create Your Profile ",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2ECC71",
        ).pack(pady=10)

        self.name_entry = self.create_styled_entry("Name:")
        self.interests_entry = self.create_styled_entry("Interests:")
        self.species_entry = self.create_styled_entry("Are you an Alien or Human?")
        self.extra_info_entry = self.create_styled_entry(
            "Galaxy (if Alien) or Country (if Human):"
        )
        self.number_entry = self.create_styled_entry("Phone/Intergalactic Number:")

        self.create_styled_button("Submit", self.submit_account)
        self.create_styled_button("Back", self.create_main_screen)

    def create_styled_entry(self, label_text):
        """Creates a styled entry field with a label."""
        tk.Label(self.main_frame, text=label_text, fg="white", bg="#2ECC71").pack()
        entry = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        entry.pack(pady=5)
        return entry

    def submit_account(self):
        """Processes account creation."""
        name = self.name_entry.get()
        interests = self.interests_entry.get()
        species = self.species_entry.get().lower()
        extra_info = self.extra_info_entry.get()
        number = self.number_entry.get()

        if species == "alien":
            self.user_profile = Alien(name, interests, extra_info, number)
        elif species == "human":
            self.user_profile = Human(name, interests, extra_info, number)
        else:
            messagebox.showerror("Invalid species", "Please enter 'alien' or 'human'.")
            return

        messagebox.showinfo("Success", f"Welcome, {self.user_profile.name}! ")
        self.create_matchmaking_screen()

    def create_matchmaking_screen(self):
        """Screen for matchmaking after account creation."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.main_frame,
            text=f"Welcome, {self.user_profile.name}!",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2ECC71",
        ).pack(pady=10)

        self.start_finding_button = self.create_styled_button(
            "Find Matches", self.start_finding_matches
        )
        self.create_styled_button("Create New Account", self.create_account_screen)

    def start_finding_matches(self):
        """Starts the matchmaking process."""
        if not self.user_profile:
            messagebox.showerror("No profile", "You must create an account first.")
            return

        user_profiles = self.database.load_user_data()
        self.match_maker = Match(user_profiles)
        self.show_next_match()

    def show_next_match(self):
        """Displays the next match in the same UI."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        match_result = self.match_maker.attempt_match()
        if match_result:
            self.show_match_ui(match_result)
        else:
            tk.Label(
                self.main_frame,
                text="No new matches available! ",
                font=("Arial", 14, "bold"),
                fg="white",
                bg="#2ECC71",
            ).pack(pady=10)
            self.create_styled_button("Back", self.create_matchmaking_screen)

    def show_match_ui(self, match):
        """Displays the matched profile in the same UI."""
        matched_profile = match[0]
        match_result = match[1] 
        match_text = str(matched_profile) 

        tk.Label(
            self.main_frame,
            text=f"Matched with:\n{match_text}",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2ECC71",
            wraplength=350, 
            justify="center",
        ).pack(pady=10)

        self.create_styled_button("Smash", lambda: self.process_match("smash", match, match_result))
        self.create_styled_button("Pass", lambda: self.process_match("pass", match, match_result))

    def process_match(self, choice, match, match_result):
        """Processes the user's decision and updates the UI."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if choice == "smash":
            if match_result:
                result_text = "It's a match! "
                
                matched_profile = match[0]
                if isinstance(matched_profile, Alien):
                    result_text += f"Their intergalactic number is: {matched_profile.intergalactic_number}"
                elif isinstance(matched_profile, Human):
                    result_text += f"Their phone number is: {matched_profile.number}"
            else:
                result_text = "Sorry, it's not a match."

        else:
            result_text = "You passed on this match."

        tk.Label(
            self.main_frame,
            text=result_text,
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2ECC71",
        ).pack(pady=10)

        self.create_styled_button("Find Another Match", self.show_next_match)
        self.create_styled_button("Back to Menu", self.create_matchmaking_screen)
