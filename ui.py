import tkinter as tk
from application import Application
from read_database import Data

def main():
    root = tk.Tk()
    database = Data("galaxy_database.txt", "user_database.txt")
    app = Application(root, database)
    root.mainloop()

if __name__ == "__main__":
    main()
