import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox 
from subprocess import call, Popen
import mysql.connector


class app(ctk.CTk):
    login = 0
    def __init__(self):
        super().__init__()
        self.geometry("600x600+250+150")
        self.title("News App")
        self.components()
        self.resizable(False, False)
        # self.databaseconnection()
        
    def components(self) :
        
        
        self.Login_label = tk.Label(self, text= 'Login', foreground = 'white',
                      font= ('Arial', 25, 'bold'),
                       background = '#242423', padx = 30)

        self.Login_label.grid(row = 0, column =  1, pady = 30)

        self.Username_Label = tk.Label(self, text = 'Username : ', foreground= 'white',
                              font = ('Times new Roman', 17),
                               background= '#242424', padx = 5, pady = 5)
        self.Username_Label.grid(row=1, column=0, padx=20, pady=50, sticky="ew")


        self.username_input = ctk.CTkEntry(self, placeholder_text= 'Enter Username')
        self.username_input.grid(row=1, column=1, pady=10, sticky="ew")


        self.Password_Label = tk.Label(self, text = 'Password :', foreground=  'white', 
                          font = ('Times new Roman', 17), 
                           background= '#242424', padx = 5, pady = 5)
        self.Password_Label.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.password_input = ctk.CTkEntry(self, placeholder_text= 'Enter Passowrd', show='*')
        self.password_input.grid(row=2, column=1, pady=10, sticky="ew" )
        self.register_button = ctk.CTkButton(self, text = 'Register Here')
        self.register_button.grid(row = 4, column = 1, pady = 10)

        self.login_button = ctk.CTkButton(self, text = 'Login', command =self.button_event)
        self.login_button.grid(row = 3 , column = 1, pady = 30)

    def button_event(self): 
        username = self.username_input.get()
        password = self.password_input.get()

        # if username == 'Yash' and password == '1234' :
        #     App.destroy()
        self.databaseconnection()
        
        #     call(['python', 'dashboard4.py'])

    def databaseconnection(self):

        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'newsapp'
        )
        # print(self.db)
        self.cursor = self.db.cursor()

        check_sql = "SELECT * from users where email_address = %s"
        self.username = self.username_input.get()
        self.passoword = self.password_input.get()

        self.cursor.execute(check_sql, (self.username,) )
        soln = self.cursor.fetchone()
        print(soln)
        if soln != None:
            if self.passoword == soln[3]:  

                app.login = soln[0]
                messagebox.showinfo(message= 'Login Successful')
                self.destroy()
                Popen(['python', 'dashboard4.py', str(app.login)])



            elif self.passoword != soln[3] :
                messagebox.showinfo(message= 'Incorrect password')
        else :
                messagebox.showinfo(message= 'Username not found')
        
        self.db.commit()

        self.cursor.close()
        self.db.close()
        



if __name__ == "__main__":
    App = app()
    App.mainloop()