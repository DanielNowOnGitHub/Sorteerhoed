from PyQt5 import QtWidgets, uic
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.QtGui
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import json
import time

#INIT
questionnr = 0
sp1 = 0 #IAT
sp2 = 0 #FICT
sp3 = 0 #SE
sp4 = 0 #BDAM

f = open("vragen.json", "r")
vragen = json.load(f)
length = len(vragen["vragen"])
#END INIT
        
vraag = "Ik vind het leuk om mij te verdiepen in de gebruikers."

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('sorteerhoed.ui', self) # Load the .ui file
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setStyleSheet("QWidget#Vraagscherm1 {background-image : url(./harry.jpg);}")
        self.setPalette(p)
    
        self.button1 = self.findChild(QtWidgets.QPushButton,"oneens")
        self.button1.clicked.connect(self.printButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton,"neutraal")
        self.button2.clicked.connect(self.printButtonPressed)
        self.button3 = self.findChild(QtWidgets.QPushButton,"eens")
        self.button3.clicked.connect(self.printButtonPressed1)
        self.button4 = self.findChild(QtWidgets.QPushButton,"back")
        self.button4.clicked.connect(self.printButtonPressed2)

        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)

        self.show()

    def printButtonPressed(self): #Oneens/neutraal
        global questionnr
        f = open("vragen.json", "r")
        vragen = json.load(f)
        soort_vak = (vragen["vragen"][questionnr]["vak"])
        #print(soort_vak)
        vraag = (vragen["vragen"][questionnr]["vraag"])
        #print(questionnr)
        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)
        questionnr += 1
    
    def printButtonPressed1(self): #Eens
        global questionnr
        global sp1
        global sp2
        global sp3
        global sp4

        f = open("vragen.json", "r")
        vragen = json.load(f)
        soort_vak = (vragen["vragen"][questionnr]["vak"])
        #print(soort_vak)
        waarde = (vragen["vragen"][questionnr]["weging"])
        vraag = (vragen["vragen"][questionnr]["vraag"])
        #print(questionnr)
        if soort_vak == "0":
            sp1 = sp1 + int(waarde)
        elif soort_vak == "1":
            sp2 += int(waarde)
        elif soort_vak == "2":
            sp3 += int(waarde)
        else:
            sp4 += int(waarde)
        print (sp1)
        #print (sp2)
        #print (sp3)
        #print (sp4)
        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)
        questionnr += 1
    
    def printButtonPressed2(self): #Back
        global questionnr
        global sp1
        global sp2
        global sp3
        global sp4

        questionnr -= 1
        f = open("vragen.json", "r")
        vragen = json.load(f)
        soort_vak = (vragen["vragen"][questionnr]["vak"])
        #print(soort_vak)
        waarde = (vragen["vragen"][questionnr]["weging"])
        vraag = (vragen["vragen"][questionnr]["vraag"])
        #print(questionnr)
        if soort_vak == "0":
            sp1 -= int(waarde)
        elif soort_vak == "1":
            sp2 -= int(waarde)
        elif soort_vak == "2":
            sp3 -= int(waarde)
        elif soort_vak == "3":
            sp4 -= int(waarde)
        print (sp1)
        print (sp2)
        print (sp3)
        print (sp4)
        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)
        questionnr += 1

font = QtGui.QFont("MS Shell Dlg 2", 20)
app = QtWidgets.QApplication(sys.argv) 
window = Ui() 
app.exec_() 