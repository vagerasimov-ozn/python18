import sys
from PyQt5.QtWidgets import QInputDialog, QWidget, QApplication, QLabel, QLayout, QVBoxLayout, QPushButton

class Diary(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    data = []

    def initUI(self):
        self.btn = QPushButton("Add ", self)
        self.todos.addWidget(self.btn)
        self.btn.clicked.connect(self.showDialog)
        # self.todos = QLabel("",self)
        # self.move(50, 50)
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)

        self.setGeometry(400 ,300, 500, 300)
        self.setWindowTitle("My Diary")
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self,'Input dialog', 'Input other')
        if ok:
            self.data.append(str(text))
            self.todos.addWidget(QLabel(str(text)))
            self.setLayout(self.todos)

app = QApplication(sys.argv)
diary = Diary()
sys.exit(app.exec_())