import tkinter as tk
from tkinter import messagebox
import DashboardPage as dashboard
import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector import errorcode
import Processes

# This is the main Program Of the Code, This page has to be run for starting the Application
# On Running this code, a window, requesting user and password is opened,
# wherein, You need to enter the Username and The Password where You want to store the database on your local MySQL Server
# Everything is done on the GUI, no need to make changes in the code.


class Login_Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("1920x1080")

        # Taking MySQL Local Server User name as input, as to where the database will be stored
        self.user_label = tk.Label(self.master, text="MySQL Username:")
        self.user_label.pack()
        self.user_entry = tk.Entry(self.master)
        self.user_entry.pack()

        # Taking MySQL Server Password input for given User
        self.password_label = tk.Label(self.master, text="MySQL Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.submit_button = tk.Button(
            self.master, text="Submit", command=self.check_credentials)
        self.submit_button.pack()

    def check_credentials(self):
        # Taking UserName and Password
        username = self.user_entry.get()
        password = self.password_entry.get()
        # Setting MySQL Login Details
        USER = username
        PASSWORD = password
        HOST = 'localhost'
        adminCredentials = ('admin', 'root')
        try:
            # Establishing MySQL Connection
            self.dbConnection = MySQLConnection(
                user=USER, password=PASSWORD, host=HOST)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                messagebox.showinfo(
                    'Error', 'Something is wrong with your user name or password')

        else:
            cursorObject = self.dbConnection.cursor()
            cursorObject.execute("SHOW DATABASES LIKE 'SuperMarket_1463_1458'")
            # Fetching all databases with Same name as ours.
            data = cursorObject.fetchall()

            # If it doesn't exist, we create the database from scratch using our code in db_init.sql
            # Then, code moves forward, and dashboard is opened, where user can run the application
            if len(data) == 0:
                with open('db_init.sql', 'r') as sql_file:
                    sql_script = sql_file.read()
                    sql_commands = sql_script.split(';')
                    for command in sql_commands:
                        try:
                            cursorObject.execute(command)
                        except Exception as e:
                            messagebox.showerror("Error", "Wrong SQL Query")
                self.dbConnection.commit()
                cursorObject.close()
                self.dbConnection.close()

            # Opening Dashboard, and giving Database access to Processes.py
            self.dbConnection = MySQLConnection(
                user=USER, password=PASSWORD, host=HOST, database="SuperMarket_1463_1458")
            tempCursorInit = Processes.Cursor_Init(self.master, USER, PASSWORD)
            new_window = tk.Toplevel(root)

            dashboard.Dashboard(new_window, tempCursorInit)

            self.dbConnection.commit()
            self.dbConnection.close()
            self.master.withdraw()


if __name__ == "__main__":
    root = tk.Tk()
    app = Login_Page(master=root)
    app.mainloop()
