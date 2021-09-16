#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for sivasdelcalzo




import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def  AvailabilityCheck():
    if  driver.find_elements_by_xpath('//div[@data-us="12.5" or aria-checked="false"]')!=[] :# pas "and" sinon cherche les deux parametres en une variable
        print("available !")
        return True
    else :
        print("not available yet")
        return False




def buyProduct() :
    time.sleep(2)
    print("Purchasing process starting")

    driver.find_element_by_xpath('//div[@data-us="12.5"]').click()

    try:
        element = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.ID, "product-addtocart-button"))
        )
    finally:
        driver.find_element_by_xpath('//button[@id="product-addtocart-button"]').click()


    time.sleep(2)

    print("Purchasing process started ...\n")

    try:
        elt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//a[@class="btn-primary btn--full mb-3"]'))
        )
    finally:
        time.sleep(3)
        driver.find_element_by_xpath('//a[@class="btn-primary btn--full mb-3"]').click()


    time.sleep(5)

    print("Filling infos")

    driver.find_element_by_xpath('//input[@id="customer-email"]').send_keys('lilsmoky72@gmail.com')
    time.sleep(0)

    driver.find_element_by_xpath('//input[@name="firstname"]').send_keys('Abdoul')
    time.sleep(0)

    driver.find_element_by_xpath('//input[@name="lastname"]').send_keys('Cisse')
    time.sleep(0)

    driver.find_element_by_xpath('//input[@name="street[0]"]').send_keys('83 boulevard de strasbourg')
    time.sleep(0)

    driver.find_element_by_xpath('//input[@name="street[1]"]').send_keys('appart A313')
    time.sleep(0.5)

    driver.find_element_by_xpath('//input[@name="city"]').send_keys('Lille')
    time.sleep(0.5)

    driver.find_element_by_xpath("//select[@class='select inp-select inp--full']/option[text()='France']").click()
    time.sleep(0.5)

    driver.find_element_by_xpath("//select[@class='select inp-select inp--full']/option[text()='Vendée']").click()
    time.sleep(0.5)




    driver.find_element_by_xpath('//input[@name="postcode"]').send_keys('59000')
    time.sleep(0.5)

    driver.find_element_by_xpath('//input[@name="telephone"]').send_keys('0665295292'+ u'\ue007')

    time.sleep(3)


    driver.find_element_by_xpath("//span[@class='price' or innerHTML='€0.00']").click()
    time.sleep(0.5)


    driver.find_element_by_xpath("//button[@data-role='opc-continue']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//input[@id='braintree']").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"braintree-hosted-field-number")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.number#credit-card-number"))).send_keys("0000000000000000")
    driver.switch_to.default_content()
    time.sleep(0.5)


    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"braintree-hosted-field-expirationMonth")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.expirationMonth#expiration-month"))).send_keys("12")
    time.sleep(0.5)

    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"braintree-hosted-field-expirationYear")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.expirationYear#expiration-year"))).send_keys("20")
    time.sleep(0.5)

    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"braintree-hosted-field-cvv")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.cvv#cvv"))).send_keys("504")

    time.sleep(0.5)


    driver.switch_to.default_content()

    conditions =driver.find_element_by_css_selector("#checkout-payment-method-load > div > div > div.payment-method.payment-method-braintree._active > div.payment-method-content > div.checkout-agreements-block > div > label")

    driver.execute_script("arguments[0].click();", conditions)
    #the checkbox is hidden so we look for its container's path and click on the first element
    time.sleep(0.5)

    driver.find_element_by_xpath("//button[@class='action primary checkout']").click()
    time.sleep(2)


    print("purchased ! ")







driver=webdriver.Chrome()
driver.get("https://www.sivasdescalzo.com/en/adidas-yeezy-500-high-fw4968")


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btn-cookie-allow"))
    )
finally:
    driver.find_element_by_xpath('//button[@id="btn-cookie-allow"]').click()



while True:
    Check=AvailabilityCheck() #modifier pour pls tailles
    if  Check != False:
            buyProduct()
            break
    else:
            print("wait 5")
            time.sleep(5)
