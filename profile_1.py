import tkinter as tk

import customtkinter as ctk
from PIL import ImageTk, Image
from subprocess import call
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
import sys
import mysql.connector
class NewsAppDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("News App Dashboard")
        self.geometry(f"{1000}x{800}")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.initframes()
        self.initcomponents()
        self.profilecomponents()

        self.login_number = 1

    def initframes(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew", columnspan = 2)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight = 1)
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 10, columnspan = 10)
        self.scrollable_frame.grid_columnconfigure(1, weight=0)

    def initcomponents(self):
        self.myprofile_label = ctk.CTkLabel(self.sidebar_frame, text="My Profile", font = ('Arial', 20, 'bold'))
        self.myprofile_label.grid(row = 0, column = 0, pady = 20)

        self.dashboard_button = tk.Button(self.sidebar_frame, text="Dashboard", height=3,  font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white'
                                          )
        self.dashboard_button.grid(row=2, column=0, sticky= 'nsew', pady= 15)

        self.search_button = tk.Button(self.sidebar_frame, text="Search News", height=3,  font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                       command=self.search_news)
        self.search_button.grid(row=3, column=0, sticky= 'nsew', pady= 15)

        self.category_button = tk.Button(self.sidebar_frame, text="News by Category", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                         command=self.news_by_category)
        self.category_button.grid(row=4, column=0, sticky= 'new', pady = 15)

        self.infographics_button = tk.Button(self.sidebar_frame, text="Infographics", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                             command=self.infographics)
        self.infographics_button.grid(row=5, column=0, sticky= 'new', pady = 15)

 

        self.Logout_button = tk.Button(self.sidebar_frame, text="Log out", height=1, font = ('Arial', 12, 'bold'), background='#14497E', foreground= 'white',
                                       command=self.loginPage)
        self.Logout_button.grid(row=7, column=0, sticky= 'ws', pady = 0)

        self.my_profile_label = ctk.CTkLabel(self.scrollable_frame, text="My Profile", font=('Arial', 25, 'bold'))
        self.my_profile_label.grid(row=0, column=0, sticky='nsew')
    
    def profilecomponents(self):
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(2, weight=1)
        image_url = 'profilepic.jpeg'
        img = ImageTk.PhotoImage(Image.open(image_url))
        profile_label = ctk.CTkLabel(self.scrollable_frame, image = img, text= ' ')
        profile_label.grid(row = 1, column= 0, padx = 15, pady = 20, rowspan = 2)
       
        profile_name_label = ctk.CTkLabel(self.scrollable_frame, text= " Name : ", font = ('serif', 25, 'bold'))
        profile_name_label.grid(row = 1, column = 1, sticky = 'nw', pady = 15)

        profile_age_label = ctk.CTkLabel(self.scrollable_frame, text= "Age :  ", font = ('serif', 25, 'bold'))
        profile_age_label.grid(row = 2, column = 1, sticky = 'nw',  padx = 5)



        self.option_tab = ctk.CTkTabview(self.scrollable_frame, width= 50, height= 455, border_color='white')
        self.option_tab.add("My News")
        self.option_tab.add("Bookmarks")

        self.option_tab.grid(row = 3, column = 0, columnspan = 5, rowspan = 5, sticky = 'nsew')
        self.fetch_bookmarks()
        self.bookmarks_components()

    def bookmarks_components(self):
        self.login_number = 1
        self.button = ctk.CTkButton(master = self.option_tab.tab("Bookmarks"), text= "test button")
        self.button.grid(row = 0, column = 0, sticky = 'nsew')

        if len(self.headline_list) > 0:
            x = 2
            for index, (headline, href) in enumerate(zip(self.headline_list, self.href_list), start=1):
                a = headline 

                headline_button = ctk.CTkButton(master = self.option_tab.tab("Bookmarks"), text=a, width= 30,
                                                font=ctk.CTkFont(size=20, weight="bold"),
                                                command=lambda idx=index, href=href: self.show_headline(href))
                headline_button._text_label.configure(wraplength=499)
                headline_button.grid(row=index + 3, column= 0 ,  sticky="nsew", columnspan = 4, pady = (20, 0))

                    
            

        

    def fetch_bookmarks(self):
        self.login_number = 2
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'newsapp'
        )
        print(self.db)
        self.cursor = self.db.cursor()

        query = "SELECT headline, href from bookmarks where user_id = %s"

        self.cursor.execute(query, (self.login_number,))    

        self.headline_list = []
        self.href_list = []

        for headline, href in self.cursor:
            self.headline_list.append(headline)
            self.href_list.append(href)


    def search_news(self):
        news_app.destroy()
        call(['python', 'search-email2.py'])

    def news_by_category(self):
        news_app.destroy()
        call(['python', 'news-cateogory.py'])

    def infographics(self):
        news_app.destroy()
        call(['python', 'infographics.py'])


    def profile(self):
        news_app.destroy()
        call(['python', 'profile_1.py'])   

    def loginPage(self):
        news_app.destroy()
        call(['python', 'login.py'])

if __name__ == "__main__":
    news_app = NewsAppDashboard()
    news_app.mainloop()

