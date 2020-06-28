import sys
from PyQt5.QtCore import Qt #нужен для обработки событий клавиатуры
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLayout, QVBoxLayout, QPushButton
import random

def greeting():
    """"""
    # if msg.text():

    rand = random.randint(0, 1)
    print(rand)
    if rand >0.5:
        msg.setText("Done!")
    else:
        msg.setText("not Done!")
# msg.setText(str(random.randint(0,10)))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Casino")
layout = QVBoxLayout()
btn = QPushButton("Hi")
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())

