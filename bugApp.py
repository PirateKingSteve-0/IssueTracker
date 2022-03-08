
from tkinter import *
import mysql.connector

splash_root = Tk()
splash_root.title("Bug Tracker")
splash_root.geometry("300x200")
#Hide the title bar

splash_label = Label(splash_root, text="Bug Tracker", font=("Helvetica",18))
splash_label.pack(pady=20)

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x_splash = (screen_width / 2) - (300 / 2)
y_splash = (screen_height / 2) - (200 / 2)

splash_root.geometry(f'{300}x{200}+{int(x_splash)}+{int(y_splash)}')

def main_window():
    splash_root.destroy()

    x_mainW = (screen_width / 2) - (700 / 2)
    y_mainW = (screen_height / 2) - (700 / 2)

    root = Tk()
    root.title("Bug Tracker @ PirateKing")
    root.geometry(f'{700}x{700}+{int(x_mainW)}+{int(y_mainW)}')

    newButton = Button(root, text="Report Issue")
    newButton.place(height=30, width=100, x=400, y=25)

    updateButt = Button(root, text="Update Report")
    updateButt.place(height=30, width=100, x=500, y=25)

#splash screen timer
splash_root.after(3000, main_window)

mainloop()
