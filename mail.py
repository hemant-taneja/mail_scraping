import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import random
import pandas as pd

options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(10)

url = "https://login.yahoo.com/?.src=ym&.lang=en-IN&.intl=in&.done=https%3A%2F%2Fin.mail.yahoo.com%2Fd"
driver.get(url)

email_elem = driver.find_element_by_name("username")
email_elem.send_keys("email id")
driver.find_element_by_name("signin").click()
time.sleep(2)
password_elem = driver.find_element_by_name("password")
password_elem.send_keys("password")
driver.find_element_by_name("verifyPassword").click()


driver.implicitly_wait(8)
time.sleep(8)
mail = []
count = 0
i = 3
# links = soup.find("div", {"id": "objects_container"}).findAll("a", {"href": re.compile("^/groups/")})
while driver.find_element_by_tag_name('div'):
    elems = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li["+str(i)+"]/a/div/div[1]/div[2]/span")
    for elem in elems:
        mail.append(elem.get_attribute("title"))
        print(mail[count])
        count += 1
    print(i)
    driver.implicitly_wait(3)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    i += 1
    if 'End of Results' in Divs:
        print('end')
        break
    else:
        continue