#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for Nike

import time
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def  AvailabilityCheck():

    if verif!=False:
        print("available !")
        return True
    else:
        print("not available yet")
        return False
        time.sleep(5)


def buyProduct() :
    print("buying attempt !")
    driver.find_element_by_xpath('//button[contains(text(),"49.5")]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//button[contains(text(),"ACHETER")]').click()
    time.sleep(2)



    try:
        driver.find_element_by_xpath('//button[contains(text(),"LIVRAISON")]').click()
        pass
    finally:
        driver.find_element_by_xpath('//checkbox[contains(text(),"LIVRAISON")]').click()
        pass


    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[id="adresse1")]').send_keys('83 boulevard de strasbourg'+ u'\ue007')

        pass

    finally:
        driver.find_element_by_xpath('//input[contains(text(),"adresse")]').send_keys('83 boulevard de strasbourg'u'\ue007')
        pass

    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[contains(text(),"postal")]').send_keys('59000')

        pass

    finally:
        driver.find_element_by_xpath('//input[contains(text(),"POSTAL")]').send_keys('59000')
        pass
    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[contains(text(),"COMPLEMENT")]').send_keys('appart A313')
        pass

    finally:
        driver.find_element_by_xpath('//input[id="adresse2")]').send_keys('appart A313')
        pass

    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[@id="email"]').send_keys('lilsmoky72@gmail.com')

        pass

    finally:
        driver.find_element_by_xpath('//input[contains(text(),"email"]').send_keys('lilsmoky72@gmail.com')
        pass

    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[@id="firstname"]').send_keys('Abdoul')
        pass

    finally:
        driver.find_element_by_xpath('//input[@id="first"]').send_keys('Abdoul')
        pass

    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[contains(text(),"POSTAL")]').send_keys('59000')
        pass

    finally:
        driver.find_element_by_xpath('//input[contains(text(),"postal")]').send_keys('59000')
        pass

    driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys('0665295292' + u'\ue007')

    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//button[contains(text(),"PAIEMENT")]').click()
        pass

    finally:
        driver.find_element_by_xpath('//checkbox[contains(text(),"PAIEMENT")]').click()
        pass


    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//input[@id="cvNumber")]').send_keys('886'+ u'\ue007')
        pass

    finally:
        driver.find_element_by_xpath('//input[@id="cvNumber")]').send_keys('886')
        pass





    time.sleep(0.5)

    time.sleep(0.5)

    time.sleep(10)


    driver.find_element_by_xpath('//button[contains(text(),"SOUMETTRE LA COMMANDE")]').click()



driver = webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.Chrome()
driver.get("https://www.nike.com/fr/launch/t/air-zoom-spiridon-cage-2-metallic-silver")


while True:
    verif=driver.find_element_by_xpath('//button[contains(text(),"49.5")]')

    Check=AvailabilityCheck()

    if  Check != False:
        buyProduct()
        break
    else:
        print("either not available yet or out of stock")
