# Date: 2020.12.23
# Author: hygoni
# Description: 특쩡 키워드에 대한 링크를 수집함 (태그 정보 수집하는 애는 따로 있음)

from selenium import webdriver
from collections import Counter
import time
import getpass
import pickle
import threading
from urllib.parse import unquote
import traceback
import hgtk

# Constants
LOGIN_URL = 'https://instagram.com'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
MAIN_TAG = '먹스타그램'
EXPLORE_URL = 'https://www.instagram.com/explore/tags/' + MAIN_TAG
WAIT_TIME = 5
WAIT_SHORT_TIME = 2
SCROLL_PAUSE_TIME = 1

n = 1
# Load Chrome Driver
options = webdriver.ChromeOptions()
options.add_argument('user-agent={}'.format(USER_AGENT))

# define lock
setLock = threading.Lock()
counterLock = threading.Lock()

linkSet = set()
f = open('links.bin', 'rb')
while True:
    try:
        linkSet = linkSet.union(pickle.load(f))
    except:
        break
f.close()

print('number of links : ' + str(len(linkSet)))
counter = Counter()
timeList = list()
identity = input('id : ')
password = getpass.getpass()

def login(driver):
    driver.get(LOGIN_URL)
    time.sleep(WAIT_TIME)
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

def pop():
    global linkSet
    print('popping list... left : ' + str(len(linkSet)))
    setLock.acquire()
    link = linkSet.pop()
    setLock.release()
    return link

def update(lst, time_list):
    global timeList
    global n

    n += 1
    print('updating...')
    counterLock.acquire()
    print(lst)
    print(time_list)
    
    # save time lst
    timeList += time_list
    counter.update(lst)
    if n % 100 == 0:
        print('saving...')
        f = open('./time_lst.bin', 'wb')
        pickle.dump(timeList, f)
        f.close()

        # save counter
        f = open('./counter.bin', 'wb')
        pickle.dump(counter, f)
        f.close()
    counterLock.release()

def visit(driver, link):
    print('visiting... : ' + link)
    driver.get(link)
    time.sleep(WAIT_SHORT_TIME)
    text = driver.find_element_by_class_name('C4VMK')
    tags = text.find_elements_by_tag_name('a')
    lst = []
    time_list = [driver.find_elements_by_tag_name('time')[0].get_attribute('datetime')]
    for tag in tags:
        tag = tag.get_attribute('href')
        tag = unquote(tag)
        tag = hgtk.text.decompose(tag)
        tag = hgtk.text.compose(tag)
        tag = tag.split('/')[-2]
        if tag != '':
            lst.append(tag)
    update(lst, time_list)

def worker():
    global linkSet
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    login(driver)
    while len(linkSet) > 0:
        try:
            link = pop()
            visit(driver, link)
        except:
            traceback.print_exc()

if __name__ == '__main__':
    threads = []
    for i in range(1):
        print('starting worker : ' + str(i))
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
        time.sleep(WAIT_TIME)
    for thread in threads:
        thread.join()