""" Простое приветствие на PyQt"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно
from PyQt5.QtWidgets import QPushButton #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QHBoxLayout #кнопочки, на которые можно нажимать


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 600, 600)

layout = QHBoxLayout() #Создаем объект верстки

layout.addWidget(QPushButton("слева")) #Добавляем виджеты слева напрово
layout.addWidget(QPushButton("по центру"))
layout.addWidget(QPushButton("справа"))

window.setLayout(layout)
window.show()
sys.exit(app.exec())