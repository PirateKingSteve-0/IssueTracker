from datetime import date
from tkinter import *
from turtle import title
from unittest import result
import mysql.connector
from mysql.connector import Error



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

    # newButton = Button(root, text="Report Issue")
    # newButton.place(height=30, width=100, x=400, y=25)

    # updateButt = Button(root, text="Update Report")
    # updateButt.place(height=30, width=100, x=500, y=25)

    mydb = mysql.connector.connect(
        host = "localhost",
        database ="issues",
        user = "root",
        password = "Kealani5264"
    )

    # try:
    #     mydb = mysql.connector.connect(
    #         host = "localhost",
    #         database ="bugTracker",
    #         user = "root",
    #         password = "Kealani5264"
    #     )

    #     if mydb.is_connected():
    #         db_Info = mydb.get_server_info()
    #         print("Connected to MySQL Server version ", db_Info)
    #         cursor = mydb.cursor()
    #         cursor.execute("select database();")
    #         record = cursor.fetchone()
    #         print("You're connected to database: ", record)
    #         cursor.execute("CREATE DATABASE IF NOT EXISTS bugTracker")

    # except Error as e:
    #     print("Error while connecting to MySQL", e)
    # finally:
    #     if mydb.is_connected():
    #         cursor.close()
    #         mydb.close()
    #         print("MySQL connection is closed")

    #Create a cursor and initialize
    my_cursor = mydb.cursor();

    # #Create db
    # my_cursor.execute("CREATE DATABASE issues")

    #Check if created
    #my_cursor.execute("SHOW DATABASES")
    # for db in my_cursor:
    #     print(db)

    #Create table
    # my_cursor.execute("CREATE TABLE ticket (reporter VARCHAR(30), date_reported DATE, issue VARCHAR(255), ticket_id INT AUTO_INCREMENT PRIMARY KEY)")

    def submit_tick():
        sql_command = "INSERT INTO ticket (reporter, date_reported, issue) VALUES (%s, %s, %s)"
        values = (rep_name_box.get(), date_box.get(), rep_issue_box.get())
        my_cursor.execute(sql_command, values)

        #Commit changes to the db
        mydb.commit()

        #Clear fields
        clear_fields()

    def clear_fields():
        rep_name_box.delete(0, END)
        date_box.delete(0, END)
        rep_issue_box.delete(0, END)

    #Create a label
    title_label = Label(root, text="Issue Tracker Database", font=("Helvetica",16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    #Create Main form to enter customer data
    reporter_name = Label(root, text="Reporter").grid(row=1, column=0, sticky=W, padx=10)
    data_of_rep = Label(root, text="Date reported ('YYYY-MM-DD')").grid(row=2, column=0, sticky=W, padx=10)
    reported_issue = Label(root, text="Issue description").grid(row=3, column=0, sticky=W, padx=10)

    #Create input fields
    rep_name_box = Entry(root)
    rep_name_box.grid(row=1, column=1, pady=5)

    date_box = Entry(root)
    date_box.grid(row=2, column=1, pady=5)

    rep_issue_box = Entry(root)
    rep_issue_box.grid(row=3, column=1, pady=5)

    #Create buttons
    add_issue_button = Button(root, text="Submit Issue", command=submit_tick)
    add_issue_button.grid(row=5, column=0, padx=10, pady=10)
    clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
    clear_fields_button.grid(row=5, column=1)

    my_cursor.execute("SELECT * FROM ticket")
    result = my_cursor.fetchall()
    for x in result:
        print(x)

#splash screen timer
splash_root.after(3000, main_window)

mainloop()
