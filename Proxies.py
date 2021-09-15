#!/usr/bin/python3
# -*-coding:Utf-8 -*


import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxy():

    url='https://sslproxies.org/' #site dont je vais scrapper les sslproxies
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'html5lib') #to scrap efficiently
    #soup.findAll('td')[::8], prendre l'element qui sort toute les 8 colonnes
    return {'https' : choice(list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}


def proxy_request(request_type, url, **kwargs):
    while True:
        try:
            proxy= get_proxy()
            r=request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
