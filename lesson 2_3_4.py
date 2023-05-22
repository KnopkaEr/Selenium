import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_1.click()

    alert_confirm = browser.switch_to.alert
    alert_confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    x = int(x)
    x = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)

    button_2 = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()
