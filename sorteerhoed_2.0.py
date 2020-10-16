from PyQt5 import QtWidgets, uic
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtMultimedia as m
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
musicnr = 1

f = open("vragen.json", "r")
vragen = json.load(f)
length = len(vragen["vragen"])
#END INIT

        
vraag = ""

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        self.setFixedSize(1082, 770)
        uic.loadUi('sorteerhoed.ui', self) # Load the .ui file
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setStyleSheet("QWidget#Vraagscherm1 {background-image : url(./Image2.png);}")
        self.setPalette(p)
      
        
        self.button1 = self.findChild(QtWidgets.QPushButton,"oneens")
        self.button1.clicked.connect(self.printButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton,"neutraal")
        self.button2.clicked.connect(self.printButtonPressed)
        self.button3 = self.findChild(QtWidgets.QPushButton,"eens")
        self.button3.clicked.connect(self.printButtonPressed1)
        self.button4 = self.findChild(QtWidgets.QPushButton,"back")
        self.button4.clicked.connect(self.exit_to_mainmenu)
        self.tabs = self.findChild(QtWidgets.QTabWidget, "Vraagscherm")
        self.startButton = self.findChild(QtWidgets.QPushButton,"start")
        self.startButton.clicked.connect(self.startx)
        self.ExitButton = self.findChild(QtWidgets.QPushButton, "exit_naar_home")
        self.ExitButton.clicked.connect(self.exit_to_mainmenu)
        self.mz1Button = self.findChild(QtWidgets.QPushButton, "MUZIEK1")
        self.mz2Button = self.findChild(QtWidgets.QPushButton, "MUZIEK2")
        self.mz3Button = self.findChild(QtWidgets.QPushButton, "MUZIEK3")
        self.mz1Button.clicked.connect(self.music)
        self.mz2Button.clicked.connect(self.music)
        self.mz3Button.clicked.connect(self.music)

        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)
        self.musicurl = QtCore.QUrl.fromLocalFile("song1.mp3")
        self.play()

        self.show()
    
    def music(self):
        global musicnr
        if musicnr == 0:
            self.musicurl = QtCore.QUrl.fromLocalFile("song1.mp3")
            musicnr += 1
        elif musicnr == 1:
            self.musicurl = QtCore.QUrl.fromLocalFile("song2.mp3")
            musicnr += 1
        elif musicnr == 2:
            self.musicurl = QtCore.QUrl.fromLocalFile("song3.mp3")
            musicnr += 1
        elif musicnr == 3:
            self.musicurl = QtCore.QUrl.fromLocalFile("song4.mp3")
            musicnr += 1
        elif musicnr == 4:
            self.musicurl = QtCore.QUrl.fromLocalFile("song5.mp3")
            musicnr = 0
        

        self.play()
            


    def play(self):
        self.content = m.QMediaContent(self.musicurl)
        self.player = m.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()



    def startx(self):
        global questionnr
        global sp1
        global sp2
        global sp3
        global sp4
        sp1 = 0 #IAT
        sp2 = 0 #FICT
        sp3 = 0 #SE
        sp4 = 0 #BDAM
        questionnr = 0
        vraag = (vragen["vragen"][questionnr]["vraag"])
        self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
        self.label.setText(vraag)
        self.label.setFont(font)
        questionnr += 1

        self.tabs.setCurrentIndex(1)


    def printButtonPressed(self): #Oneens/neutraal
        global questionnr
        #f = open("vragen.json", "r")
        #vragen = json.load(f)
        #soort_vak = (vragen["vragen"][questionnr]["vak"])
        #print(soort_vak)
        if questionnr <= 14:
            vraag = (vragen["vragen"][questionnr]["vraag"])
            self.label = self.findChild(QtWidgets.QLabel,"vraagbox")
            self.label.setText(vraag)
            self.label.setFont(font)
            print(questionnr)
            questionnr += 1
        else: 
            self.tabs.setCurrentIndex(2)

    
    def printButtonPressed1(self): #Eens
        global questionnr
        global sp1
        global sp2
        global sp3
        global sp4

        
        if questionnr <= 14:
            soort_vak = (vragen["vragen"][questionnr]["vak"])
            waarde = (vragen["vragen"][questionnr]["weging"])
            vraag = (vragen["vragen"][questionnr]["vraag"])
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
        else:
            self.tabs.setCurrentIndex(2)
    
    def printButtonPressed2(self): #Back
        global questionnr
        global sp1
        global sp2
        global sp3
        global sp4

        questionnr -= 1
        #f = open("vragen.json", "r")
        #vragen = json.load(f)
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

    def exit_to_mainmenu(self):     #naar startscherm
        self.tabs.setCurrentIndex(0)


font = QtGui.QFont("MS Shell Dlg 2", 20)
app = QtWidgets.QApplication(sys.argv)
window = Ui() 
app.exec_() 