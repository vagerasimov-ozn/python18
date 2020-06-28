import sys
from PyQt5.QtWidgets import QInputDialog, QWidget, QApplication, QLabel, QLayout, QVBoxLayout, QPushButton

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    data = []

    def initUI(self):
        self.btn = QPushButton("Add ", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.diary = QLabel("",self)
        self.move(50, 50)
        self.setFixedHeight(200)
        self.setFixedWidth(200)

        self.setGeometry(400 ,300, 500, 300)
        self.setWindowTitle("My Diary")
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self,'Input dialog', 'Input other')
        if ok:
            self.data.append( str(text))
            for todo in self.data:
                self.diary.setText(todo)

app = QApplication(sys.argv)
diary = Diary()
sys.exit(app.exec())