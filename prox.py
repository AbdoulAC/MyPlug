#!/usr/bin/python3
# -*-coding:Utf-8 -*


import time
import requests
import json
import threading
import randomheaders
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys





i=0
while i < 6:
      print(i)
      i=i+1
      time.sleep(1)
driver=webdriver.Chrome()
driver.get('http://whatismyipaddress.com/') # pour request , proxies=proxies), headers=randomheaders.LoadHeader()
time.sleep(30)
