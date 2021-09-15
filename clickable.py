from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC









driver = webdriver.Firefox()
driver.get("https://www.nike.com/fr/launch/t/air-zoom-spiridon-cage-2-metallic-silver")



driver.send_keys( u'\ue007')



verif=driver.find_element_by_xpath('//button[contains(text(),"47")]')

if verif!=False :
    driver.find_element_by_xpath('//button[contains(text(),"47")]').click()
    driver.find_element_by_xpath('//button[contains(text(),"AJOUTER AU PANIER")]').click()
