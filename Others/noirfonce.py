#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for noirefonce




import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def  AvailabilityCheck():

    r=requests.get('https://www.noirfonce.fr/collections/whatsnew/products.json')
    products = json.loads((r.text))['products']
    for product in products :
        productname=product['title']
        if productname == 'Nike Space Hippie 04':#Nike W Space Hippie 04 CD3476-100
            url='https://www.noirfonce.fr/products/'+product['handle']
            return url
    else:

        return False


def buyProduct(url) :
    driver.get(str(url))

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "variant__button-label"))
            )
    finally:
            driver.find_element_by_xpath('//label[contains(text(),"38.5")]').click()


    time.sleep(0.5)
    driver.find_element_by_xpath('//button[@data-testid="Checkout-button"]').click() #mettre une exception au cas où avec un bouton
    time.sleep(3)

    driver.find_element_by_xpath('//input[@id="checkout_email_or_phone"]').send_keys('booking.abdoul@gmail.com')
    time.sleep(0.5)
    driver.find_element_by_xpath('//label[@class="checkbox__label"]').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('abdoul')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('cissé')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('83 blvd de strasbourg')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_address2"]').send_keys('appart A 313 ')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Postal code"]').send_keys('59000')
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Lille')
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='checkout_shipping_address_country']/option[text()='France']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys('0665295292' + u'\ue007') #numéro de tel + touche entrée
    time.sleep(3)

    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="checkout_payment_gateway_20421444"]').click()
    time.sleep(2)

    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Obitouchiwa')

    driver.find_element_by_xpath('//button[@id="btnLogin"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//button[@id="payment-submit-btn"]').click()

    print("purchased !")


driver=webdriver.Chrome()

while True:
    myUrl=AvailabilityCheck()
    if  myUrl != False:
        buyProduct(myUrl)
        break
    else:
        print("either not available yet or out of stock")
        time.sleep(5)
