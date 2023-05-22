import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name.send_keys('Оксана')

    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name.send_keys('Васильева')

    email_name = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email_name.send_keys('knopkaer@list.ru')

    file_img = browser.find_element(By.ID, 'file')
    dir_way = os.path.abspath(os.path.dirname(__file__))
    file_ = os.path.join(dir_way, 'Пустой.txt')
    file_img.send_keys(file_)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
