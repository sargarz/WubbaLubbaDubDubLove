import tkinter as tk
from application import Application
from read_database import Data


def main():
    """Initialize the GUI application."""
    database = Data("galaxy_database.txt", "user_database.txt")
    root = tk.Tk()
    app = Application(root, database)
    root.mainloop()


if __name__ == "__main__":
    main()
