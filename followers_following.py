from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_names(driver, profilename):
    time.sleep(1)
    path = "/html/body/div[4]/div/div/div[2]"
    scroll_box = driver.find_element_by_xpath(path)
    last_ht = 0
    ht = 1
    while last_ht != ht:
        last_ht = ht
        ht = driver.execute_script(
            """
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        time.sleep(1)
    time.sleep(2)
    links = scroll_box.find_elements_by_tag_name("a")
    names = []
    for i in links:
        if i.text != "":
            names.append(i.text)
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    return names


def get_followers_names(driver, profilename):
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    time.sleep(3)
    path = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
    wait = WebDriverWait(driver, 10)
    followers_button = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
    followers_button.click()
    names_followers = get_names(driver, profilename)
    f = open("followers_names.txt", "w")
    for i in names_followers:
        f.write(i)
        f.write("\n")
    return names_followers


def get_following_names(driver, profilename):
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    time.sleep(3)
    path = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"
    wait = WebDriverWait(driver, 10)
    following_button = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
    following_button.click()
    names_following = get_names(driver, profilename)
    f = open("following_names.txt", "w")
    for i in names_following:
        f.write(i)
        f.write("\n")
    return names_following


def names_not_following_back(followers_filename, following_filename):
    f = open(followers_filename, "r")
    names_followers = f.readlines()
    f = open(following_filename, "r")
    names_following = f.readlines()
    not_following_back = []
    for i in names_following:
        if i not in names_followers and i != "":
            not_following_back.append(i[:-1])
    f = open("not_following_back.txt", "w")
    for i in not_following_back:
        f.write(i)
        f.write("\n")


def unfollow_with_file(driver, filename):
    f = open(filename, "r")
    lines = f.readlines()
    not_following_back = []
    for i in lines:
        not_following_back.append(i[:-1])
    wait = WebDriverWait(driver, 10)
    for i in not_following_back:
        url = "https://www.instagram.com/"+i+"/"
        driver.get(url)
        #path = "/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button"
        unfollow1 = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        unfollow1[1].click()
        time.sleep(4)
        path = "/html/body/div[4]/div/div/div/div[3]/button[1]"
        unfollow2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, path)))
        unfollow2.click()
        time.sleep(randint(5,13))
