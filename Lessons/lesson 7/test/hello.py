"""Простое приветствие на PyQt5"""
import sys
#Работа приложения, конпки
from PyQt5.QtWidgets import QApplication
# Не интерактивные элементы
from PyQt5.QtWidgets import QLabel
# Представляет из себя 1 окно
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 800, 800)

helloMSG = QLabel("<h1> Привет! </h1>", parent=window)
helloMSG.move(260,15)
# print(QLabel.BOX.__doc__)
# print(dir(QLabel.BOX.__doc__))
hello2 = QLabel("<h2> Ozon </h2>", parent=window)
hello2.move(265,55)

window.show()
sys.exit(app.exec())

