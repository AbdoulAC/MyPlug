#!/usr/bin/python3
# -*-coding:Utf-8 -*


from threading import thread
from Proxies import get_proxy
from selenium import webdriver

proxy=get_proxy()

def A():
    driver.find_element_by_xpath('//*[@id="fakebox-input"]').send_keys("FakeboxA")
    print("called on proxy {}").format(proxy)

def B():
    driver.find_element_by_xpath('//*[@id="fakebox-input"]').send_keys("FakeboxB")
