"""Пример расположения с помощью сетки"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно
from PyQt5.QtWidgets import QLineEdit #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QPushButton #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QLabel #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QFormLayout #кнопочки, на которые можно нажимать


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 600, 600)

layout = QFormLayout() #Создаем объект верстки
"""первый аргумент строка, второй - позиция в ней"""
layout.addRow(QLabel("Enter you IDs"))
layout.addRow("Name", QLineEdit())
layout.addRow("Surname", QLineEdit())
layout.addRow("Card Number", QLineEdit())
layout.addRow(QPushButton("Send data"))

window.setLayout(layout)
window.show()
sys.exit(app.exec())