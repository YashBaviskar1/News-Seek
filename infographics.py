import tkinter as tk
from bs4 import BeautifulSoup
import requests
import customtkinter as ctk
import webbrowser
from subprocess import call
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
import webview

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



    def initframes(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew", columnspan = 2)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight = 1)
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 5, columnspan = 5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

    def initcomponents(self):
        self.infographics_label = ctk.CTkLabel(self.sidebar_frame, text="Infographics", font = ('Arial', 20, 'bold'))
        self.infographics_label.grid(row = 0, column = 0, pady = 20)

        self.dashboard_button = tk.Button(self.sidebar_frame, text="Dashboard", height=3,  font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                          command= self.dashboard)
        self.dashboard_button.grid(row=2, column=0, sticky= 'nsew', pady= 15)

        self.search_news_button = tk.Button(self.sidebar_frame, text="Search News", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                            command= self.search_news)
        self.search_news_button.grid(row=3, column=0, sticky= 'new', pady = 15)

        self.category_button = tk.Button(self.sidebar_frame, text="News By Category", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                         command=self.news_by_category)
        self.category_button.grid(row=4, column=0, sticky= 'new', pady = 15)

        self.myprofile_button = tk.Button(self.sidebar_frame, text="My Profile", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                          command=self.profile)
        self.myprofile_button.grid(row=5, column=0, sticky= 'new', pady = 15)

        self.Logout_button = tk.Button(self.sidebar_frame, text="Log out", height=1, font = ('Arial', 12, 'bold'), background='#14497E', foreground= 'white')
        self.Logout_button.grid(row=7, column=0, sticky= 'ws', pady = 0)

        self.topics_label = ctk.CTkLabel(self.scrollable_frame, text="Topics", font=('Arial', 25, 'bold'))
        self.topics_label.grid(row=0, column=0, sticky='nsew', padx = 10)


        self.economics_button = tk.Button(self.scrollable_frame, text = 'Economics', font = ('Helavetica', 22), background='white', command=self.show_economics)
        self.economics_button.grid(row = 1, column= 0,  pady = 15, columnspan= 5, rowspan= 5, sticky='nsew')
        self.ent_button = tk.Button(self.scrollable_frame, text = 'Entertainment', font = ('Helavetica', 22), background='white', command=self.show_entartiment)
        self.ent_button.grid(row = 11, column= 0,  pady = 15, columnspan= 5, rowspan= 10, sticky='nsew')

        

    def show_economics(self):
        self.gdp_button = ctk.CTkButton(self.scrollable_frame, text = 'GDP per Capita of India (1960-2022) ', font = ('Helavetica', 15))
        self.gdp_button.grid(row = 30, column = 1, sticky = 'nsew', padx = 5, pady = 5, rowspan = 2)

    def show_entartiment(self):
        self.ent_one_button = ctk.CTkButton(self.scrollable_frame, text = 'no of movies ', font = ('Helavetica', 15))
        self.ent_one_button.grid(row = 30, column = 1, sticky = 'nsew', padx = 5, pady = 5, rowspan = 2)

    def display_graph(self):
        call(['python', 'graph1-1.py'])

    def dashboard(self):
        news_app.destroy()
        call(['python', 'dashboard4.py'])

    def search_news(self):
        news_app.destroy()
        call(['python', 'search-email2.py'])

    def news_by_category(self):
        news_app.destroy()
        call(['python', 'new-cateogory.py'])

    def infographics(self):
        news_app.destroy()
        call(['python', 'infographics.py'])

    def show_headline(self, link):

        webview.create_window('News Headline', link)
        webview.start()

    
    def loginPage(self):
        news_app.destroy()
        call(['python', 'login.py'])

    def profile(self):
        news_app.destroy()
        call(['python', 'profile_1.py'])   



if __name__ == "__main__":
    news_app = NewsAppDashboard()
    news_app.mainloop()

