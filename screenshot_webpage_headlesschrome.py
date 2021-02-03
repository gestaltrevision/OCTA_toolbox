# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:32:50 2021

@author: u0090621
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com")
driver.get("file:///C:/Users/u0090621/Box%20Sync/1.%20Research/NeatlyOrganized/7.%20OCTA/OCTA/OCTA_toolbox/test.svg")

# capture the screen
driver.get_screenshot_as_file("capture.png")