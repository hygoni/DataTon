# Date: 2020.12.23
# Author: hygoni
# Description: 특정 키워드에 대한 링크를 수집함 (태그 정보 수집하는 애는 따로 있음)

from selenium import webdriver
import os
import time
import getpass
import pickle

# Constants
LOGIN_URL = 'https://instagram.com'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
MAIN_TAG = '먹스타그램'
EXPLORE_URL = 'https://www.instagram.com/explore/tags/' + MAIN_TAG
WAIT_TIME = 5
SCROLL_PAUSE_TIME = 1

# Load Chrome Driver
options = webdriver.ChromeOptions()
options.add_argument('user-agent={}'.format(USER_AGENT))
driver = webdriver.Chrome('./chromedriver.exe', options=options)



def login(driver):
    driver.get(LOGIN_URL)
    identity = input('id : ')
    password = getpass.getpass()

    loginForm = driver.find_element_by_id('loginForm')
    inputs = loginForm.find_elements_by_tag_name('input')
    button = loginForm.find_element_by_tag_name('button')
    usernameInput = inputs[0]
    passwordInput = inputs[1]
    usernameInput.send_keys(identity)
    passwordInput.send_keys(password)
    button.click()
    time.sleep(WAIT_TIME)
    later = driver.find_elements_by_tag_name('button')[0]
    later.click()
    time.sleep(SCROLL_PAUSE_TIME)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

def waitScroll(driver):
    last_height = driver.execute_script('return document.body.scrollHeight')   # 자바스크림트로 스크롤 길이를 넘겨줌
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # selenium에서 scroll 기능 사용
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    while new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")


login(driver)
driver.get(EXPLORE_URL)

linkSet = set()
with open('./links.bin', 'rb') as f:
    linkSet = pickle.load(f)

f = open('./links.bin', 'wb')
while True:
    print('links : ' + str(len(linkSet)))
    blocks = driver.find_elements_by_class_name('kIKUG')
    for elem in blocks:
        try:
            link = elem.find_element_by_tag_name('a')
            link = link.get_attribute('href')
            if link not in linkSet:
                print(link)
                linkSet.add(link)
        except:
            pass
    pickle.dump(linkSet, f)
    waitScroll(driver)

#driver.close()