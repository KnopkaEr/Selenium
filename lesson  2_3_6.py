import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, '[type= "submit"]')
    button_1.click()

    w_name_1 = browser.window_handles[0]
    w_name_2 = browser.window_handles[1]
    browser.switch_to.window(w_name_2)

    x = browser.find_element(By.ID, 'input_value').text
    x = int(x)
    x = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)

    button_2 = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button_2.click()

finally:
    time.sleep(5)
    browser.quit()
    
