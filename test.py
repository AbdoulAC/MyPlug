#!/usr/bin/python3
# -*-coding:Utf-8 -*


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




if __name__ == '__main__':
    url=input("donnez une url : ")
    Page= webdriver.chrome()
    Page.get(URL)
