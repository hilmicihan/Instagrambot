from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


def like_with_hashtags(driver, hashtags):
    # hashtags = ["motivation", "fitness"] before hard coded part
    for i in hashtags:
        comploted_likes = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        first_photo.click()
        time.sleep(2)
        for i in range(1, 20):
            #path = "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button"

            like_button = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "wpO6b ")))

            like_button[1].click()
            link = "Next"
            next_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, link)))
            time.sleep(randint(3,5))
            next_button.click()
            comploted_likes += 1
            time.sleep(randint(3,8))


def only_comments(driver, hashtags):
    commets = ["Really good", "Nice work :)",
               "your are perfect", "Nice Photo i like it :D", "So cool"]
    # hashtags = ["ielts", "fitness"] before hard coded part
    for i in hashtags:
        completed_comments = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        time.sleep(2)
        path = "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        first_photo.click()
        for i in range(1, 20):
            #path = "/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea"
            try:
                comment_area = wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "Ypffh")))
                comment_area.click()
            except:
                link = "Next"
                next_button = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, link)))

                time.sleep(randint(3, 5))
                next_button.click()
                time.sleep(2)
                continue
            #path = "/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea"
            time.sleep(2)
            commet_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "Ypffh")))
            comment = commets[randint(0, len(commets)-1)]
            commet_text.send_keys(comment)
            time.sleep(3)
            #path = "/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/button"
            #path = "//div[text()='Post']"
            #name = "Post"
            post_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Post')]")))
            post_button.click()
            link = "Next"
            next_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, link)))
            time.sleep(randint(5, 20))
            next_button.click()
            completed_comments += 1
    print("completed comments : " + completed_comments)


def follow_with_hashtags(driver, hashtags):
    # hashtags = ["ielts", "fitness"] before hard coded part
    for i in hashtags:
        completed_follows = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        first_photo.click()
        time.sleep(3)
        for i in range(1, 20):
            path = "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button"
            follow_button = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
            follow_button[1].click()
            link = "Next"
            next_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, link)))
            time.sleep(randint(3,5))
            next_button.click()
            completed_follows += 1
            time.sleep(randint(3,8))
    print("completed follows : " + completed_follows)


def like_comment_follow_func(driver, hashtags):
    commets = ["Really good", "Nice work :)", "It is adorable",
               "your are perfect", "Nice Photo i like it :D", "So cool"]
    # hashtags = ["fitness", "motivation"] before hard coded part
    for i in hashtags:
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        first_photo.click()
        for i in range(1, 50):
            #path = "/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/textarea"
            # /html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea
            try:
                comment_area = wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "Ypffh")))
                comment_area.click()
                #path = "/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/textarea"
                time.sleep(2)
                commet_text = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Ypffh")))
                comment = commets[randint(0, len(commets)-1)]
                commet_text.send_keys(comment)
                time.sleep(3)
                #path = "/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/button"
                post_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Post')]")))
                post_button.click()
            except:
                print("there is an error try to comment")
                link = "Next"
                next_button = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, link)))
                time.sleep(randint(3,5))
                next_button.click()
            #path = "/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button"
            time.sleep(2)
            like_button = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "wpO6b ")))

            like_button[1].click()
            time.sleep(2)
            #path = "/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button"
            follow_button = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
            if(follow_button[1].text != "Following"):
                follow_button[1].click()
            link = "Next"
            next_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, link)))
            time.sleep(randint(3,5))
            next_button.click()
