import sys
from PyQt5.QtCore import Qt #нужен для обработки событий клавиатуры
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    """ Просто класс для примера
    он наследует от QWidget
    """
    def __init__(self):
        super().__init__()
        self.initUI() # вызов функции отрисовки, которую мы создадим ниже
    def initUI(self):
        label = QLabel("press esc to quit", self)
        label.move(10, 10)
        label = QLabel("press alt to increase size window", self)
        label.move(10, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Обработчик событий")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Alt:
            self.resize(800, 800)

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec())