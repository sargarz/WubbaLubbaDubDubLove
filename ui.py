import tkinter as tk

class UI:
    """Helper class to manage UI elements."""
    # probably makes it easier for me
    BG_COLOR = "#004d25"
    ACCENT_COLOR = "#2ecc71"
    FONT_FAMILY = "Segoe UI"
    TEXT_COLOR = "white"
    CARD_BG = "white"
    CARD_TEXT = "#004d25"

    def __init__(self, master, app):
        self.master = master
        self.app = app

        self.master.configure(bg=self.BG_COLOR)
        self.main_frame = tk.Frame(self.master, bg=self.BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        self.content_frame = tk.Frame(self.main_frame, bg=self.BG_COLOR)
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

    def clear_frame(self):
        """Clears the current frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def create_label(self, text, font_size=12, fg=TEXT_COLOR):
        """Creates a styled label."""
        label = tk.Label(
            self.content_frame,
            text=text,
            font=(self.FONT_FAMILY, font_size, "bold"),
            fg=fg,
            bg=self.BG_COLOR,
            wraplength=400,
            justify="center"
        )
        label.pack(pady=(10, 5))
        return label

    def create_button(self, text, command, state=tk.NORMAL):
        """Creates a styled button."""
        button = tk.Button(
            self.content_frame,
            text=text,
            font=(self.FONT_FAMILY, 12, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.BG_COLOR,
            width=25,
            height=2,
            bd=0,
            relief="flat",
            highlightthickness=0,
            command=command,
            state=state,
            activebackground="#27ae60",
            activeforeground="white",
            cursor="hand2"
        )
        button.pack(pady=12)
        return button

    def create_entry(self, label_text):
        """Creates a labeled entry field."""
        self.create_label(label_text, font_size=12)

        entry = tk.Entry(
            self.content_frame,
            font=(self.FONT_FAMILY, 12),
            width=34,
            bd=0,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self.BG_COLOR,
            highlightcolor=self.BG_COLOR,
            insertbackground=self.BG_COLOR,
            bg="white",
            fg="black"
        )
        entry.pack(pady=(0, 15))
        return entry

    def create_card(self, text):
        """Creates a modern profile card."""
        card_frame = tk.Frame(
            self.content_frame,
            bg=self.CARD_BG,
            relief="flat",
            bd=0,
            highlightthickness=0,
            padx=20,
            pady=20
        )
        card_frame.pack(pady=20, fill="x")

        tk.Label(
            card_frame,
            text=text,
            font=(self.FONT_FAMILY, 14, "bold"),
            fg=self.CARD_TEXT,
            bg=self.CARD_BG,
            wraplength=380,
            justify="center"
        ).pack(pady=10)
