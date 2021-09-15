#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Module allowing user to read a csv file

import csv
import time

def Lecteur():

    with open('My_file.csv') as csv_file:
        
        csv_reader = csv.reader(csv_file)

        
        for line in csv_reader:
            var= line[0]
            print(var)
            break
