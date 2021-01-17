from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name('firstname').send_keys('Name')
    LastName = browser.find_element_by_name('lastname').send_keys('Lastname')
    email = browser.find_element_by_name('email').send_keys('Email')

    file = browser.find_element_by_id('file')
    dir_path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(dir_path, 'file.txt')
    file.send_keys(filepath)

    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
finally:
    time.sleep(20)
    browser.quit()
