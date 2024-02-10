from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# create empty lists which will store the flore, date, user id, comment, number of likes and dislikes later
floor_ls = []
date_ls = []
user_ls = []
comment_ls = []
like_ls = []
dis_ls = []

# ask for the lihkg link and the number of pages you want to scrape
lihkg_link = input("Enter the lihkg link(without /page): ")
pages = input("Enter the number of pages you want to scrape: ")

#open the browser, and disable the notification
chrome_options = ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = Chrome(options=chrome_options)

# a for loop that read all the pages 1 by 1
for i in range(1,int(pages)+1):
    # driver.get("https://lihkg.com/thread/3582359/page/{}".format(i))
    driver.get(lihkg_link + "/page/{}".format(i))

    # sleep 2 second after reaching a new page, to load the contents
    sleep(2)

    # need to accept cookies in the first run, ignore this if cookie is not asked
    '''
    if i == 1:
        driver.find_element(By.CLASS_NAME,'fc-button-label').click()
        #give 2 second to load after accepting cookies
        sleep(2)
    '''
        
    # loop and find the class of all boxes which include the username, comment, number of likes and dislikes etc.
    lihkg_html = BeautifulSoup(driver.page_source,'html.parser')
    result_list = lihkg_html.find_all('div', {'class':'_1Hi94Pa6lplJ436NQaMbEt'})

    for result in result_list:
        floor_ls.append(result.find('span',{'_3SqN3KZ8m8vCsD9FNcxcki'}).get_text()[1:])
        #user_ls.append(result.a.get_text())
        user_ls.append(result.a['href'].split('/')[-1])

        # the comment is in another class when the comment box is in its small form
        if type(result.find('div',{'class':'_2cNsJna0_hV8tdMj3X6_gJ'})) != type(None):
            comment_ls.append(result.find('div',{'class':'_2cNsJna0_hV8tdMj3X6_gJ'}).get_text())
        else: 
            comment_ls.append(result.find('div',{'class':'oStuGCWyiP2IrBDndu1cY'}).get_text())

        
        # its error when the comment box is in its "small" form, which you can't see the date, and the number of likes and dislikes. We will skip the small comment boxes
        like_and_dis = result.find_all('label',{'class':'_1yxPOd27pAzF9olhItRDej'})
        try:
            like_ls.append(like_and_dis[0].get_text())
            dis_ls.append(like_and_dis[1].get_text())
            date_ls.append(result.find('span',{'Ahi80YgykKo22njTSCzs_'})['title'].split(' ')[0])
        except:
            like_ls.append('')
            dis_ls.append('')
            date_ls.append('')

# make the result a table
result_df = pd.DataFrame({'floor': floor_ls, 'date':date_ls, 'userid':user_ls, 'comment':comment_ls,'likes':like_ls,'dislikes':dis_ls})
result_df.to_csv('lihkg.csv',index=False, encoding='utf-8-sig')