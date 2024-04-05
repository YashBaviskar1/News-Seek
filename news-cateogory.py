import tkinter as tk 
import customtkinter as ctk 
from bs4 import BeautifulSoup
import requests
import webbrowser
from subprocess import call
import webview
class NewsCategory(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600+250+150")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.initframes()
        self.initcomponents()
        self.initscrollable()


    def initframes(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew", columnspan = 2)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight = 1)
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 5, columnspan = 5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
    def initscrollable(self):
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=2, sticky="nsew", rowspan = 5, columnspan = 5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.NewsCategory = ctk.CTkLabel(self.scrollable_frame, text = "News category", font=('Arial', 25, 'bold'))
        self.NewsCategory.grid(row = 0, column = 0, sticky = 'nsew', pady = 15)
        self.checkboxes()

    def initcomponents(self):

        self.NewsCategoryLabel = ctk.CTkLabel(self.sidebar_frame, text="News Category", font = ('Arial', 20, 'bold'))
        self.NewsCategoryLabel.grid(row = 0, column = 0, pady = 20)

        self.Dashboard_button = tk.Button(self.sidebar_frame, text="Dashboard", height=3,  font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                          command=self.dashboard)
        self.Dashboard_button.grid(row=2, column=0, sticky= 'nsew', pady= 15)

        self.SearchNews_button = tk.Button(self.sidebar_frame, text="Search News", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                           command=self.search_news)
        self.SearchNews_button.grid(row=3, column=0, sticky= 'new', pady = 15)

        self.infographics_button = tk.Button(self.sidebar_frame, text="Infographics", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                             command=self.infographics)
        self.infographics_button.grid(row=4, column=0, sticky= 'new', pady = 15)

        self.myprofile_button = tk.Button(self.sidebar_frame, text="My Profile", height=3, font = ('Arial', 14, 'bold'), background='#14476E', foreground= 'white',
                                          command=self.profile)
        self.myprofile_button.grid(row=5, column=0, sticky= 'new', pady = 15)

        self.Logout_button = tk.Button(self.sidebar_frame, text="Log out", height=1, font = ('Arial', 12, 'bold'), background='#14497E', foreground= 'white',
                                       command=self.loginPage)
        self.Logout_button.grid(row=7, column=0, sticky= 'ws', pady = 0)

        self.NewsCategory = ctk.CTkLabel(self.scrollable_frame, text = "News category", font=('Arial', 25, 'bold'))
        self.NewsCategory.grid(row = 0, column = 0, sticky = 'nsew', pady = 15)



        self.checkboxes()
      


    def state_of_checkoox(self, index):
        checkboxes_list = [self.SportsCheckbox, self.FinanceCheckbox, self.EntertainmentCheckbox, self.WorldNewsbox, 
                      self.Politicsbox, self.SciTechbox]
        checkbox_text = ["Sports", "Finance", "Entertainment", "World", "Politics", "Sci/Tech"]
        current_checkbox = checkboxes_list[index]
        current_selection = checkbox_text[index]
        if current_checkbox.get() == 1:
            print(current_selection)
            self.CheckBoxLabel = ctk.CTkLabel(self.scrollable_frame, text=(' '*5) + current_selection + (' '*5), font = ( 'Helvetica', 20, 'bold'),
                                              width = 30)
            self.CheckBoxLabel.grid(row = 3, column = 0 , pady = 4)
            for checkbox in checkboxes_list:
                if checkbox != current_checkbox:
                    checkbox.configure(state='disabled')
            self.getnewsbycategory(index)
        else :
            
            self.CheckBoxLabel.destroy()
            self.initscrollable()
            for checkbox in checkboxes_list:
                checkbox.configure(state='enabled')
                self.checkboxes()
    
    def checkboxes(self):
        self.SportsCheckbox = ctk.CTkCheckBox(self.scrollable_frame, text = "Sports", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue=1, offvalue= 0,
                                              command=lambda :self.state_of_checkoox(0))
        self.SportsCheckbox.grid(row = 1, column = 0, pady = 5, padx = 5)

        self.FinanceCheckbox = ctk.CTkCheckBox(self.scrollable_frame, text = "Finance", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue=1, offvalue= 0,
                                              command=lambda: self.state_of_checkoox(1))
        self.FinanceCheckbox.grid(row = 1, column = 1, pady = 5, padx = 5)


        self.EntertainmentCheckbox = ctk.CTkCheckBox(self.scrollable_frame, text = "Entertainment", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue=1, offvalue= 0,
                                              command=lambda : self.state_of_checkoox(2))
        self.EntertainmentCheckbox.grid(row = 1, column = 2, pady = 5, padx = 5)


        self.WorldNewsbox = ctk.CTkCheckBox(self.scrollable_frame, text = "World", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue= 1, offvalue=0,
                                              command=lambda :self.state_of_checkoox(3))
        self.WorldNewsbox.grid(row = 2, column = 0, pady = 15, padx = 5)

        self.Politicsbox = ctk.CTkCheckBox(self.scrollable_frame, text = "Politics", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue=1, offvalue= 0,
                                              command=lambda :self.state_of_checkoox(4))
        self.Politicsbox.grid(row = 2, column = 1, pady = 15, padx = 5)


        self.SciTechbox = ctk.CTkCheckBox(self.scrollable_frame, text = "Science/Tech", 
                                              fg_color= '#47574F', font = ( 'Helvetica', 18, 'bold'),
                                              onvalue=1, offvalue= 0,
                                              command=lambda :self.state_of_checkoox(5))
        self.SciTechbox.grid(row = 2, column = 2, pady = 15, padx = 5)
    



    def getnewsbycategory(self, index):
        checkbox_text = ["Sports", "Finance", "Entertainment", "World", "Politics", "Sci/Tech"]
        
        format_list = ['Sports', 'Business', 'Entertainment', 'World', 'Politics', 'Sci%2fTech']
        url = f"https://www.bing.com/news/search?q={format_list[index]}"
        print(url)
        # testurl = "https://www.bing.com/news/search?q={Sports}"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}

        request = requests.get(url)
        
        soup = BeautifulSoup(request.text, 'lxml')

        x = 4
        headlines = soup.find_all('div', class_ = 'na_t news_title ns_big')
        links = soup.find_all('a', class_='news_fbcard wimg')
        results = soup.select('a', class_= 'news_fbcard wimg')



        for headline, link in zip(headlines, links):
            href = link.get('href')
            self.headlineButton = ctk.CTkButton(self.scrollable_frame, text = headline.text.strip(), width=30,
                                            font=ctk.CTkFont(size=20, weight="bold"), 
                                             command= lambda href = href : self.show_headline(href))
            self.headlineButton._text_label.configure(wraplength=499)
            self.headlineButton.grid(row = x, column = 0, pady = 5, sticky = 'nsew', columnspan = 5 )
            self.bookmark_radio = ctk.CTkRadioButton(self.scrollable_frame, text = '', bg_color='#0168AA', width = 5, fg_color= 'white' )
            self.bookmark_radio.grid(row =x, column = 3, stick = 'ew', )
            x += 1


    def GotoNews(self, link):
         webbrowser.open(link)

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
        news_app.destroy()
        call(['python', 'profile_1.py'])   

    def loginPage(self):
        news_app.destroy()
        call(['python', 'login.py'])






news_app = NewsCategory()
news_app.mainloop()
