"""Пример расположения с помощью сетки"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно
from PyQt5.QtWidgets import QPushButton #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QGridLayout #кнопочки, на которые можно нажимать


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 600, 600)

layout = QGridLayout() #Создаем объект верстки
"""первый аргумент строка, второй - позиция в ней"""
layout.addWidget(QPushButton("слева"), 0, 0)
layout.addWidget(QPushButton("по центру"), 0, 1)
layout.addWidget(QPushButton("справа"), 2, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec())