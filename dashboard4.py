import tkinter as tk
from bs4 import BeautifulSoup
import requests
import customtkinter as ctk
import webbrowser
from subprocess import call
from subprocess import Popen
from tkinter import messagebox
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
import webview
import sys
import mysql.connector

class NewsAppDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("News App Dashboard")
        self.geometry(f"{1100}x{800}")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.initframes()
        self.initcomponents()
        self.headline_list = []
        self.href_list = []
        self.login_number = sys.argv[1]
        print(self.login_number)

    def initframes(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew", columnspan = 2)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight = 1)
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 5, columnspan = 5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

    
    def initcomponents(self):
        self.dashboardLabel = ctk.CTkLabel(self.sidebar_frame, text="Dashboard", font = ('Arial', 20, 'bold'))
        self.dashboardLabel.grid(row = 0, column = 0, pady = 20)

        self.search_button = tk.Button(self.sidebar_frame, text="Search News", height=3,  font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white', command=self.search_news)
        self.search_button.grid(row=2, column=0, sticky= 'nsew', pady= 15)

        self.category_button = tk.Button(self.sidebar_frame, text="News by Category", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white', command=self.news_by_category)
        self.category_button.grid(row=3, column=0, sticky= 'new', pady = 15)

        self.infographics_button = tk.Button(self.sidebar_frame, text="Infographics", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white', command=self.infographics)
        self.infographics_button.grid(row=4, column=0, sticky= 'new', pady = 15)

        self.myprofile_button = tk.Button(self.sidebar_frame, text="My Profile", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white', command=self.profile)
        self.myprofile_button.grid(row=5, column=0, sticky= 'new', pady = 15)

        self.Logout_button = tk.Button(self.sidebar_frame, text="Log out", height=1, font = ('Arial', 12, 'bold'), background='#14497E', foreground= 'white', command = self.loginPage)
        self.Logout_button.grid(row=7, column=0, sticky= 'ws', pady = 0)

        self.dailyNewsLabel = ctk.CTkLabel(self.scrollable_frame, text="Daily News", font=('Arial', 25, 'bold'))
        self.dailyNewsLabel.grid(row=0, column=0, sticky='nsew')

        self.bookmark_button = ctk.CTkButton(self.scrollable_frame, text = 'bookmark', command= self.bookmark_action)
        self.bookmark_button.grid(row = 1, column = 3, sticky = 'w')
        

        self.fetch_and_display_headlines()


    def fetch_and_display_headlines(self):
        url = "https://www.bing.com/news"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')

        headlines = soup.find_all('a', class_='title')
        titles = soup.find_all('div', class_='publogo')
        x = 2
        for index, (headline, title) in enumerate(zip(headlines, titles), start=1):
            if headline.text.strip() and title.text.strip() and title.text != 'Ad':
                href = headline.get('href')
                a = headline.text.strip() + ' by ' + ' ' +title.text.strip()
                #title_label = ctk.CTkLabel(self.scrollable_frame, text = title.text.strip(), bg_color= 'green')
                #title_label.grid(row = x + 1, column = 0)
                headline_button = ctk.CTkButton(self.scrollable_frame, text=a, width= 30,
                                                font=ctk.CTkFont(size=20, weight="bold"),
                                                command=lambda idx=index, href=href: self.show_headline(href))
                headline_button._text_label.configure(wraplength=499)
                headline_button.grid(row=index + 3, column= 0 ,  sticky="nsew", columnspan = 4, pady = (20, 0))

                self.bookmark_radio = ctk.CTkRadioButton(self.scrollable_frame, text = '', bg_color='#0168AA', width = 5 )
                #self.bookmark_radio.grid(row = index + 3, column = 3, stick = 'ew')
                self.scrollable_frame.grid_rowconfigure(index, weight= 0)

                #self.checkbox = ctk.CTkCheckBox(self.scrollable_frame, text = '', width = 1)
                #self.checkbox.grid(row = index + 3, column = 0, sticky = 'e')

    def bookmark_action(self) : 
        self.headline_dict = {}
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 5, columnspan = 5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        url = "https://www.bing.com/news"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')

        headlines = soup.find_all('a', class_='title')
        titles = soup.find_all('div', class_='publogo')
        x = 2
        for index, (headline, title) in enumerate(zip(headlines, titles), start=1):
            if headline.text.strip() and title.text.strip() and title.text != 'Ad':
                href = headline.get('href')
                a = headline.text.strip() + ' by ' + ' ' +title.text.strip()
                #title_label = ctk.CTkLabel(self.scrollable_frame, text = title.text.strip(), bg_color= 'green')
                #title_label.grid(row = x + 1, column = 0)
                headline_button = ctk.CTkButton(self.scrollable_frame, text=a, width= 30,
                                                font=ctk.CTkFont(size=20, weight="bold"),
                                                command=lambda idx=index, href=href: self.show_headline(href))
                headline_button._text_label.configure(wraplength=499)
                headline_button.grid(row=index + 3, column= 0 ,  sticky="nsew", columnspan = 4, pady = (20, 0))

                #self.bookmark_radio = ctk.CTkRadioButton(self.scrollable_frame, text = '', bg_color='#0168AA', width = 5 )
                #self.bookmark_radio.grid(row = index + 3, column = 3, stick = 'ew')
                self.scrollable_frame.grid_rowconfigure(index, weight= 1)

                self.check_var = ctk.StringVar(value="off")
                self.checkbox = ctk.CTkCheckBox(self.scrollable_frame, text = '', width = 1,  command = lambda sv = self.check_var, a = a, href = href: self.checkbox_event(sv, a, href), 
                                                variable=self.check_var, onvalue="on", offvalue="off")
                self.checkbox.grid(row = index + 3, column = 1, sticky = 'e')
                self.headline_dict[a] = self.check_var

        self.confirm_bookmark = ctk.CTkButton(self.scrollable_frame, text = 'bookmark confirm ', command= self.bookmark_confirm)
        self.confirm_bookmark.grid(row = index, column = 1, sticky = 'e', pady = 10)
        

    def checkbox_event(self, var, headline, href):
        #print("checkbox for ", var.get(), headline)
        
        if var.get() == "on":
            self.headline_list.append(headline)
            self.href_list.append(href)
        if var.get() == 'off':
            if headline in self.headline_list and href in self.href_list:
                self.headline_list.remove(headline)
                self.href_list.remove(href)


    def bookmark_confirm(self):
        
        # print(self.headline_list)
        # print(self.href_list)
        # for i in range(len(self.headline_list)):
        #     print(self.headline_list[i])
        #     print(self.href_list[i])
        #     print('\n')

        self.insert_in_database()
        messagebox.showinfo(message="Bookmarks confirmed")
        self.initframes()
        self.initcomponents()
        self.headline_list = []
        self.href_list = []
        self.bookmark_button = ctk.CTkButton(self.scrollable_frame, text = 'bookmark', command= self.bookmark_action)
        self.bookmark_button.grid(row = 1, column = 3, sticky = 'w')
        self.fetch_and_display_headlines()

    def insert_in_database(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'newsapp'
        )
        print(self.db)
        self.cursor = self.db.cursor()
        query = "INSERT INTO bookmarks (user_id, headline, href) VALUES (%s, %s, %s)"
        for headline, href in zip(self.headline_list, self.href_list):
            self.cursor.execute(query, (self.login_number, headline, href))
        self.db.commit()



    def dashboard(self):
        news_app.destroy()
        call(['python', 'dashboard4.py'])

    def search_news(self):
        news_app.destroy()
        call(['python', 'search-email2.py'])

    def news_by_category(self):
        news_app.destroy()
        call(['python', 'news-cateogory.py'])

    def infographics(self):
        news_app.destroy()
        call(['python', 'infographics.py'])

    def show_headline(self, link):

        webview.create_window('News Headline', link)
        webview.start()

    def profile(self):
        self.destroy()
        Popen(['python', 'profile_1.py', self.login_number])   

    def loginPage(self):
        news_app.destroy()
        call(['python', 'login.py'])





if __name__ == "__main__":
    news_app = NewsAppDashboard()
    news_app.mainloop()

