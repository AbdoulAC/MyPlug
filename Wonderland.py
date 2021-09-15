#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for featuresneakerboutique

import time
import requests
import json
from selenium import webdriver


def  AvailabilityCheck():

    r=requests.get('https://www.featuresneakerboutique.com/products.json')
    products = json.loads((r.text))['products']
    for product in products :
        productname=product['title']
        if productname == 'Stussy 8 Ball Pig Dyed Tee - Moss':
            url='https://www.featuresneakerboutique.com/product/'+product['handle']
            return url
    else:

        return False


def buyProduct(url) :
    driver=webdriver.Chrome()
    driver.get(str(url))
    driver.find_element_by_xpath('//div[@data-value="10"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//button[@class="add to cart default-btn"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//button[@name="Chekout"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="email"]').send_keys('example@gmail.com')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="first"]').send_keys('Alice')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('0665320000' + u'\ue007') #numéro de tel + touche entrée




while True:
    myUrl=AvailabilityCheck()
    if  myUrl != False:
        buyProduct(myUrl)
        break
    else:
        print("either not available yet or out of stock")
