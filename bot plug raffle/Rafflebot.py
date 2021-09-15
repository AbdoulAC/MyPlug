#!/usr/bin/python3
#-*-coding:Utf-8 -*
#This is the raffle bot itself



import time
import requests
import json
import checkstocks
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# should be able to check the stocks

val = 0
url=""

print("1 - AFEW")
print("\n")
print("2 - Feature Sneaker boutique")
print("\n")
print("3 - Bape")
print("\n")
print("4 - Supreme")
print("\n")
print("\n")

val = input("on which website does the raffle occur ? print the number only.")

valeur = int(val)

if (valeur==1):
    url="https://en.afew-store.com/products.json"
else:
    if (valeur==2):
        url="https://feature.com/products.json"

    else:
        print("wrong input")


checkstocks.check(url)

print("\n")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
print("opening the website at selected url")
print("\n")

print('wait for it ...')

i=0

driver=webdriver.Firefox()

myurl = "https://de.afew-store.com/products/air-jordan-4-retro-university-blue-black-tech-grey-white"


with open('my_file.csv') as csv_file:
        
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for line in csv_reader:
            # Go to the right Page  (to modify and adapt with previous step)

            driver.get(myurl)

            time.sleep(4.5)
           
            if (i==0):

                close_cookie = WebDriverWait(driver, 10, 0.25).until(EC.visibility_of_element_located([By.XPATH, '//*[@id="onetrust-accept-btn-handler"]']))
                driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
                time.sleep(1)

            # Select the shoes 

            print("Step : Selecting the shoe ")


            print("Working")

            driver.find_element_by_xpath('//a[contains(text(),"12.5")]').click()


            driver.find_element_by_xpath('//*[@id="raffle-instagram"]').send_keys(line[2])

            driver.find_element_by_xpath('//*[@id="raffle-terms"]').click()
            time.sleep(1)

            driver.find_element_by_xpath('/html/body/main/section/header/div/div/div[2]/form/div[3]/div[2]/button').click()



            print(" shoe selection done")
            time.sleep(3)

            # Fill out the informations (some are from csv file)

            print('filling out infos')


            driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys(line[0])

            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Abdoul-aziz')


            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys("Cisse")


            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('4 rue aimé Cesaire')



            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').send_keys('110')


            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('93400')



            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Saint-Ouen')

            driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('0033665295292')

            driver.find_element_by_xpath('//*[@id="continue_button"]').click()


            print('infos handover done')

            #purchase via paypal (don't forget the anti-bot)
            print('payment')

            close_btn = WebDriverWait(driver, 10, 0.25).until(EC.visibility_of_element_located([By.XPATH, '//*[@id="continue_button"]']))

            driver.find_element_by_xpath('//*[@id="continue_button"]').click()

            time.sleep(2)

            close_btn2 = WebDriverWait(driver, 10, 0.25).until(EC.visibility_of_element_located([By.XPATH, '//*[@id="continue_button"]']))
            driver.find_element_by_xpath('//*[@id="continue_button"]').click()

            time.sleep(2)

            close_btn3 = WebDriverWait(driver, 10, 0.25).until(EC.visibility_of_element_located([By.XPATH, '//*[@id="continue_button"]']))
            driver.find_element_by_xpath('//*[@id="continue_button"]').click()

            


            time.sleep(15)

            print('payment process done')
            # repeat the process

            print('repeating the process with a new email @')
            i+=1
            
Print("all the accounts are successfully registered")            