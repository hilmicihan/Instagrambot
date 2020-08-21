from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_func
from like_comment_follow import *
from followers_following import *
from random import randint

""" driver = webdriver.Chrome("C:/setups/chromedriver_win32/chromedriver.exe")
url = "https://www.instagram.com/"
driver.get(url)
username = "fitnesseducator20"
password = "123456123456"
time.sleep(2)
 """

#login_func(driver, username, password)
""" wait = WebDriverWait(driver, 10)
profilename = "fitnesseducator20"
get_followers_names(driver, profilename)
get_following_names(driver, profilename)
names_not_following_back("followers_names.txt", "following_names.txt")
unfollow_with_file(driver, "not_following_back.txt")"""
#like_comment_follow_func(driver, ["software"])
