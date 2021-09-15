#!/usr/bin/python3
# -*-coding:Utf-8 -*

class Person :
    """simple test"""
    def __init__(self, prenom, age) :
            self.nom = "Cissé"
            self.age=age
            self.prenom=prenom
            self.mon_age=str(self.age)
    def Present(self) :
            """convertir l'âge avant la fonction"""
            print("Je m'appelle {} {}, j'ai {} ans, Enchanté ".format(self.prenom, self.nom, self.mon_age))
