#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Module allowing user to check the stocks


import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 


def check(url):

    r = requests.get(url)
    products = json.loads((r.text))['products']

    for product in products:
        productname= product['handle']
        print(productname)
        

  







