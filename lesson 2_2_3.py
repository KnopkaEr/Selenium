from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element(By.ID, 'num1').text
    n2 = browser.find_element(By.ID, 'num2').text

    a = int(n1) + int(n2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(a))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

