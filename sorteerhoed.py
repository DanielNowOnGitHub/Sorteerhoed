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

app = QApplication(sys.argv)

question = ""
vraag = "wil je dood?"
#hallo hoe gaat het met mij gaat alles goed 

iat = 0
se = 0
fict = 0
bdm = 0
iets = "hoiikbengijs"
specialisatie = 0
window = QWidget()
window.setAutoFillBackground(True)
layout = QGridLayout()
window.setLayout(layout)
qApp.setStyleSheet("QLabel { color: black; }");
font = QtGui.QFont("Arial", 40)
qApp.setFont(font)



b1 = QPushButton("fuck1",)
b2 = QPushButton("fuck 2")
b3 = QPushButton("fuck3")
b4 = QPushButton("fuck4")
l1 = QLabel(vraag)



window.setGeometry(200,200,500,300)
b1.setMinimumHeight(80)
p = window.palette()
p.setColor(window.backgroundRole(), Qt.red)
window.setPalette(p)
layout.addWidget(l1, 2, 1,)
layout.setColumnStretch(2 ,3)
layout.addWidget(b1, 5, 0)
layout.addWidget(b2, 3, 1)
layout.addWidget(b3, 3, 2)
layout.addWidget(b4, 3, 3)


def color():
    p.setColor(window.backgroundRole(), Qt.red)
    window.setPalette(p)
    time.sleep(3)
    p.setColor(window.backgroundRole(), Qt.yellow)
    window.setPalette(p)
    time.sleep(3)
    p.setColor(window.backgroundRole(), Qt.green)
    window.setPalette(p)
    time.sleep(3)

#timer = QTimer()
#timer.timeout.connect(color)
#timer.start(10)

window.show()
app.exec_()

for i in iets:
    antwoord = input("zet ff 1 neer:")
    if antwoord == 1:
        specialisatie + 1
    else:
        specialisatie + 0

#hoi dit gasat wel goed
#ik was hier :gijs
