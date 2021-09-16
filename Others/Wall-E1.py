#!/usr/bin/python3
# -*-coding:Utf-8 -*
#for adidas

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
#from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys




def URLGen(model, size, name): #url avec la taille

        ShoeBase=530  #la plus petite taille convertie en url (530=taille 4) taille Us
        Shoesize=(size-36)*15                              #(size-4)*20 pour taille Us
        Finalcode=int(ShoeBase+Shoesize)
        Url="https://www.adidas.fr/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(Finalcode)
        print(Url)
        return Url

def UrlGenProduct(name,model):
        url="https://www.adidas.fr/"+name+"/"+model+".html"
        return url

def SneakerBot(url):
        while True:
                try:
                    Myurl=url
                    #grab the page
                    Uclient= Ureq(Myurl)
                    page=Uclient.read() #to not lose the page requested
                    Uclient.close()

                    p=soup(page, "html.parser") #P contains the html page
                    p.findAll("div", {"class","add-to-bag___1vbiu gl-vspace-bpall-small"})
                    time.sleep(6)
                    print("i am looking for the product")
                    return p
                except:
                    pass




model=input("donnez le modèle: ")

print(model)

size1=int(input("donnez la taille (partie entière): "))

size2=int(input("donnez la taille partie décimale 0, 1 ou 2 uniquement: "))

size=size1+(size2/3)

name=input("donnez le nom de la chaussure : ")

url=URLGen(model, size, name)

nav = webdriver.Chrome()

nav.get(url)


#MyBot=SneakerBot(url)

#MyBot.select()
