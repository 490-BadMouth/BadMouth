import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Simple GUI")

label = QLabel("Hello World!", window)
label.move(137, 60)

button = QPushButton("Click Me!", window)
button.move(125, 100)

window.show()
sys.exit(app.exec_())