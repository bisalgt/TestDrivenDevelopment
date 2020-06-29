#! /home/bishal/TestDrivenDevelopment/tdd_project/env/bin/python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")
# browser.sleep(4)

assert 'TO-DO' in browser.title, "Browser title was "+ browser.title

browser.quit()

