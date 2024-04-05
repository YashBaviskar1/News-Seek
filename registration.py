import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox 
from subprocess import call
import mysql.connector
import re


class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600+250+150")
        self.title("News App")
        self.components()
        self.resizable(False, False)
    


    def connection(self, name, email_address, password):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'newsapp')

        self.cursor = self.db.cursor()   


        query = "INSERT INTO users(name, email_address, password) VALUES (%s, %s, %s)"

        val = (name, email_address, password)

        self.cursor.execute(query, val)
        self.db.commit()

        self.cursor.close()
        self.db.close()


    def components(self) :
        
        
        self.Login_label = tk.Label(self, text= 'Registration', foreground = 'white',
                      font= ('Arial', 25, 'bold'),
                       background = '#242423', padx = 30)

        self.Login_label.grid(row = 0, column =  1, pady = 30)

        self.NameLabel = tk.Label(self, text = 'Name : ', foreground= 'white',
                              font = ('Times new Roman', 17),
                               background= '#242424', padx = 5, pady = 5)
        self.NameLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.name_input = ctk.CTkEntry(self, placeholder_text= 'Enter name')
        self.name_input.grid(row=1, column=1, pady=10, sticky="ew")


        self.email_label = tk.Label(self, text = 'Email address : ', foreground= 'white',
                              font = ('Times new Roman', 17),
                               background= '#242424', padx = 5, pady = 5)
        self.email_label.grid(row=2, column=0, padx=20, pady=50, sticky="ew")


        self.email_input = ctk.CTkEntry(self, placeholder_text= 'enter email')
        self.email_input.grid(row=2, column=1, pady=10, sticky="ew")


        self.Password_Label = tk.Label(self, text = 'Password :', foreground=  'white', 
                          font = ('Times new Roman', 17), 
                           background= '#242424', padx = 5, pady = 5)
        self.Password_Label.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.password_input = ctk.CTkEntry(self, placeholder_text= 'Enter Passowrd', show='*')
        self.password_input.grid(row= 3, column=1, pady=10, sticky="ew" )
        self.register_button = ctk.CTkButton(self, text = 'Register Here')
        self.register_button.grid(row = 6, column = 1, pady = 10)

        self.login_button = ctk.CTkButton(self, text = 'Login', command = self.button_event)
        self.login_button.grid(row = 6 , column = 1, pady = 30)

    def button_event(self): 
        name = self.name_input.get()
        password = self.password_input.get()
        email = self.email_input.get()

        
        if name.isalpha() == False:
            messagebox.showerror(message='Only Alphabets allowed in name field')

        elif len(password) < 6 :
            messagebox.showerror(message= 'Password needs to more than 6 chracters')

        elif self.validate_email(email) == False:
            messagebox.showerror(message= "Email not in valid format ")

        else :
            self.connection(name, email, password)
            App.destroy()
            messagebox.showinfo(message= 'Login Successful')
            call(['python', 'login.py'])



    def validate_email(self, email):

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if re.match(pattern, email):
            return True
        else:
            return False






App = app()
App.mainloop()