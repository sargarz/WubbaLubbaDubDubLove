import tkinter as tk

class UI:
    """Helper class to manage UI elements."""
    
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.main_frame = tk.Frame(self.master, bg="#2ECC71")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def clear_frame(self):
        """Clears the current frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_label(self, text, font_size=12, fg="white", bg="#06402B"):
        """Creates a styled label."""
        return tk.Label(
            self.main_frame,
            text=text,
            font=("Arial", font_size, "bold"),
            fg=fg,
            bg=bg
        )

    def create_button(self, text, command, state=tk.NORMAL):
        """Creates a styled button."""
        button = tk.Button(
            self.main_frame,
            text=text,
            font=("Arial", 14, "bold"),
            bg="#27AE60",
            fg="black",
            width=20,
            height=2,
            bd=0,
            relief="flat",
            highlightthickness=0,
            command=command,
            state=state,
            activebackground="#2ECC71",
            activeforeground="white",
            cursor="hand2",
            pady=10,
        )
        button.pack(pady=10)
        return button

    def create_entry(self, label_text):
        """Creates a labeled entry field."""
        self.create_label(label_text, font_size=12).pack(pady=5)
        entry = tk.Entry(self.main_frame, font=("Arial", 12, ), width=30,)
        entry.pack(pady=5)
        return entry

    def create_card(self, text):
        """Creates a modern profile card."""
        card_frame = tk.Frame(self.main_frame, bg="white", relief="flat", bd=0, pady=20)
        card_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(
            card_frame,
            text=text,
            font=("Arial", 16, "bold"),
            fg="#2ECC71",
            bg="white",
            wraplength=350,
            justify="center",
        ).pack(pady=10)
