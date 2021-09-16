#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for afew




import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#r=requests.get('https://de.afew-store.com/products.json') 
r=requests.get('https://de.afew-store.com/collections/sneakers/products.json')#https://de.afew-store.com/products.json')
products = json.loads((r.text))['products']
for product in products :
    print(product['title'])
