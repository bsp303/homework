from selenium import webdriver
from selenium.webdriver.common.by import By

def test246():
    try:
        link = "http://suninjuly.github.io/cats.html"
        browser = webdriver.Chrome()
        browser.get(link)
        #Выполениени кейса
        button = browser.find_element_by_id("button")
    finally:
        browser.quit()
