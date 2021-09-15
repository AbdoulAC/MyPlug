#!/usr/bin/python3
# -*-coding:Utf-8 -*





import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager




#driver=webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

url="www.reddit.com"

driver.get(url)
