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



def  AvailabilityCheck():

    req=r=requests.get('https://de.afew-store.com/collections/sneakers/products.json')
 #requests.get('https://de.afew-store.com/products.json')  
#r=requests.get('https://de.afew-store.com/collections/sneakers/products.json')
#https://de.afew-store.com/products.json')
    products = json.loads((req.text))['products']
    for product in products :
        productname=product['title']
        if 'Nike AIR MAX III "LASER BLUE"' in productname:
            url='https://en.afew-store.com/products/'+product['handle']
            return url
    else:
        return False


def buyProduct(url) :
    driver.get(str(url))
    time.sleep(3)

    try: #cookie btn
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cc-btn cc-dismiss"))
        )

    except:
        pass
    driver.find_element_by_xpath('//a[@class="cc-btn cc-dismiss"]').click()

    while True:
        if  driver.find_elements_by_xpath('//a[@class="btn btn-sm"]')!=[] :
            break
        else:
            print("no size available yet")
            driver.refresh();
            time.sleep(7)


    try:#size selection
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn btn-sm"))
            )

    except:
        pass

    driver.find_element_by_xpath('//a[contains(text(),"10")]').click()

    time.sleep(0.5)

    print("validating")
    driver.find_element_by_xpath('//*[@id="product-section"]/header/div/div/div[2]/form/div/div[2]/button').click() #mettre une exception au cas où avec un bouton
    time.sleep(3)

    print("Purchasing...")
    driver.find_element_by_xpath('//*[@id="cart-form"]/div/div[2]/footer/div[1]/p[2]/button').click()
    time.sleep(3)

    print("Filling informations...")
    driver.find_element_by_xpath('//input[@id="checkout_email"]').send_keys('booking.abdoul@gmail.com')
    time.sleep(0.3)


    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_first_name"]').send_keys('abdoul aziz')
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_last_name"]').send_keys('cissé')
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_address1"]').send_keys('83 blvd de strasbourg')
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_address2"]').send_keys('appart A 313 ')
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_zip"]').send_keys('59000')
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_city"]').send_keys('Lille')
    time.sleep(0.3)
    driver.find_element_by_xpath("//*[@id='checkout_shipping_address_country']/option[text()='France']").click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_phone"]').send_keys('0665295292' + u'\ue007') #numéro de tel + touche entrée
    time.sleep(1)

    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    time.sleep(2)

    #driver.find_element_by_xpath('//*[@id="checkout_payment_gateway_14656077867"]').click() #here
    #time.sleep(5)
    driver.find_element_by_xpath('//*[@id="checkout_payment_gateway_36434739243"]').click()

    print("validation 1")
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    time.sleep(2)

    print("validation 2")
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    time.sleep(1)



    #driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    #driver.find_element_by_xpath('//*[@id="password"]').send_keys('Obitouchiwa1')
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="Ecom_Payment_Card_Number"]').send_keys(5355842322876017)
    #driver.find_element_by_xpath('//button[@id="acceptAllButton"]').click()
    #driver.find_element_by_xpath('//button[@id="btnLogin"]').click()

    driver.find_element_by_xpath('//*[@id="Ecom_Payment_Card_ExpDate_Month"]/option[text()="12"]').click()
    time.sleep(0.2)


    driver.find_element_by_xpath('//*[@id="Ecom_Payment_Card_ExpDate_Year"]/option[text()="2025"]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="Ecom_Payment_Card_Verification"]').send_keys(504)
    time.sleep(0.2)

    driver.find_element_by_xpath('//*[@id="submit3"]').click()
    print("purchased !")


driver=webdriver.Chrome('/usr/bin/chromedriver')

while True:


    
    myUrl=AvailabilityCheck()
    if  myUrl != False:
        buyProduct(myUrl)
        break
    else:
        print("either not available yet or out of stock")
        time.sleep(5)
