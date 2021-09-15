import csv
import time

with open('My_file.csv', newline='') as file:
    lecteur = csv.reader(file)

    i=0
    nb=1
    for row in lecteur:
        for i in nb:
            print(row[i])
            time.sleep(2)
            i=+1     
            print(row[i])
            time.sleep(2)
            if row >= 2 :
                break
            i=0
                
      