#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for 

import os
import sys
import requests
import threading
import webbrowser
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys





def SneakerBot(url):
        while True:
                try:
                    Myurl=url
                    #grab the page
                    Uclient= Ureq(Myurl)
                    page=Uclient.read() #to not lose the page requested
                    Uclient.close()
                    print("first step completed")
                    p=soup(page, "html.parser") #P contains the html page
                    containers = p.findAll("div", {"class","col-s-12 col-l-8"})
                    container=containers[2]
                    print("second step completed")

                    rebours= container.findAll("p", "class", "denseText___2wFAe gl-text-center")

                    if (rebours.get_attribute('innerHTML') == "00:00:00:00"):
                            driver.find_element_by_link_text(container.a[href]).click
                            print("step 3 success" )
                            False

                    else :
                            pass


                    time.sleep(3)
                    print("i am waiting for the product")

                except:
                    pass






url="https://www.yeezysupply.com/"

nav = webdriver.Firefox()

nav.get(url)


MyBot=SneakerBot(url)
