import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    x = int(x)
    x = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)

    button_2 = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button_2.click()


finally:
    time.sleep(12)
    browser.quit()
