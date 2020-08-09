#Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
#Import config
from config import *

#Login
def login(browser):
    #Login URL
    URL='https://codeforces.com/enter'
    #Get website
    browser.get(URL)
    #Fill handle
    browser.find_element_by_xpath('/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[1]/td[2]/input').send_keys(CF_Handle)
    #Fill password
    browser.find_element_by_xpath('/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[2]/td[2]/input').send_keys(CF_Password)
    #Login
    browser.find_element_by_xpath('/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input').click()
    #Wait for page load
    sleep(1)

#Get user list
def get_users(browser):
    #URL of the list of people in a country
    URL_CF_Country='https://codeforces.com/ratings/country/'+CF_Country
    #Get website
    browser.get(URL_CF_Country)
    #Wait for page load
    sleep(3)
    #Number of tabls
    tabs=0
    #Try
    try:
        tabs=int(browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[4]/ul').text.split(' ')[-2])
    except:
        tabs=1
    #User handles
    handles=[]
    #Extract users by tab
    for tab in range(1, tabs+1):
        #Tab url
        tab_url='https://codeforces.com/ratings/country/'+CF_Country+'/page/'+str(tab)
        #Get website
        browser.get(tab_url)
        #Get table
        table=browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[3]/div[6]/table/tbody').get_attribute('innerHTML')
        #BS4
        BS=BeautifulSoup(table, "html.parser")
        #Number of users
        number_of_users=len(BS)
        #Get users
        for user_number in range(2, number_of_users):
            #User
            user=browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[3]/div[6]/table/tbody/tr['+str(user_number)+']/td[2]')
            #Add the handle to the list
            handles.append(user.text)
    #Return handles
    return handles

#Add friends
def add_cf_friends(browser, users):
    #For each user
    for user in users:
        #I don't add myself
        if user==CF_Handle:
            continue
        #User URL
        URL='https://codeforces.com/profile/'+user
        #Get website
        browser.get(URL)
        #Wait for page load
        sleep(.2)
        #Get star status
        star_status=browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div[2]/div/h1/img').get_attribute("class").split(' ')[0]
        #If not my friend
        if star_status=='addFriend':
            try:
                #Add new friend
                browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div[2]/div[2]/h1/img').click()
            except:
                try:
                    #Add new friend
                    browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div[2]/div/h1/img').click()
                except:
                    #Error
                    print('Failed to add', user, 'as friend.')
            #Print
            print(user, 'added as friend.')