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

proxies={
'http' : '5.79.73.131:13010',
'https' : '5.79.73.131:13010'
}

Threadcount=1
PROXY = '5.79.73.131:13010'



def Nav():
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "noProxy":None,
        "proxyType":"MANUAL",
        "autodetect":False
    }
    i=1
    while i < 4:
        print(i)
        i=i+1
        time.sleep(1)
    driver=webdriver.Chrome()
    driver.get('http://whatismyipaddress.com/')
    time.sleep(40)


threads = [threading.Thread(name="ThreadNumber{}".format(n), target=Nav) for n in range(Threadcount)]
for t in threads:
    t.start()
