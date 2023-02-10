import sys
from PySide2.QtWidgets import QApplication ,QMainWindow ,QWidget , QLabel, QPushButton

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Click me!", self)
        button.move(100, 100)
        button.clicked.connect(self.button_clicked)

        self.label = QLabel("Welcome to PyQt5!", self)
        self.label.move(100, 50)

    def button_clicked(self):
        self.label.setText("Button clicked!")
