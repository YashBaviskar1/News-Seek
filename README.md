# News-Seek
A Python Tkinter News Application which uses Web Scraping to fetch real time news from bing news, also includes various features like searching for a specific topic, news by category and comprehensive database connectivity using MySQL for implementing features like Bookmarks to get news from specific topics sent to user directly through email

## Setup Instructions
Follow these instructions to set this application up in your system, pre-requirement is to make sure python is installed in system and accessible through bash or command line as well as mysql. 

1. **Clone the Repository :**
   ``` bash
   git clone https://github.com/YashBaviskar1/News-Seek.git
   cd News-Seek
  
2. **Set Up Virtual Environment (Optional) :**
    ``` bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows

3. **Install Dependencies :**
   ``` bash
   pip install -r requirements.txt

4. **Database Configuration :**
   make sure to change the name of user = 'root' and password = '1234' in the database code as per the Convenience
   Here are all the queries to execute in mysql command line to configure the database as per the source files. 
   ``` sql
   CREATE DATABASE newsapp;
   
    CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name CHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    );
   
    CREATE TABLE bookmarks (
    bookmark_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    headline TEXT,
    href VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
    );

5. In order to run the Application run registration.py to add data in database and login through login.py to access the rest of the application
