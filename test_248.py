import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test248():
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 15)
        #1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
        browser.get(link)
        #2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
        price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        #3. Нажать на кнопку "Book"
        book = browser.find_element(By.ID, "book").click()
        #4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
        x_val = browser.find_element(By.ID, "input_value").text
        y = calc(x_val)
        y_value = browser.find_element(By.ID, "answer").send_keys(y)
        Submit = browser.find_element(By.ID, "solve").click()
    finally:
        time.sleep(5)
        browser.quit()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))