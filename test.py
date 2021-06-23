#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)
driver.save_screenshot('search_results.png')

driver.quit()
