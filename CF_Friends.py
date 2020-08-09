#Plase:
#Remember to download the correct selenium driver (https://chromedriver.chromium.org/downloads)
#Remember to set the country of friends you want to add in config.py
#Remember to set your handle and password for you codeforces account in the config.py file

#Import libraries
from selenium import webdriver
import os
#Import config
from config import *
#Import functions
from functions import *

#Browser
browser = webdriver.Chrome(os.getcwd()+'/chromedriver')

#Login
login(browser)
#Get user list
users=get_users(browser)
#Add friends
add_cf_friends(browser, users)

#Close browser
browser.close()