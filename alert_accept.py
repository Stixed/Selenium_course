from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    FirstButton = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script('return arguments[0].scrollIntoView(true);', FirstButton)
    FirstButton.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector('#input_value').text
    ans = calc(x)
    Input = browser.find_element_by_css_selector('#answer').send_keys(ans)

    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(20)
    browser.quit()
