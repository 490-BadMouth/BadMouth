import sys
from subprocess import Popen, PIPE, call
import threading
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QColor, QPalette, QTextCursor

BASH_SCRIPT = "bash vmic3.sh"  # Replace with the path to your bash script


class MainWindow(QMainWindow):
    append_output_signal = Signal(str)

    def __init__(self):
        super().__init__()

        # Set up the UI
        self.init_ui()

        # Connect the append_output_signal to the append_output slot
        self.append_output_signal.connect(self.append_output)

        # Run the bash script in a separate thread to avoid blocking the GUI
        self.run_bash_script()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.status_indicator = QLabel("Status")
        self.status_indicator.setAutoFillBackground(True)
        self.set_status_indicator_color("red")
        layout.addWidget(self.status_indicator)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_status_indicator_color(self, color_name):
        palette = self.status_indicator.palette()
        color = QColor(color_name)
        palette.setColor(QPalette.Window, color)
        self.status_indicator.setPalette(palette)

    #@Slot(str)
    def append_output(self, text):
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.insertPlainText(text)

    def run_bash_script(self):
        #call(BASH_SCRIPT)
        self.process = Popen([BASH_SCRIPT], stdout=PIPE, stderr=PIPE, universal_newlines=True, bufsize=0, shell=True)
        self.process_output_reader_thread = threading.Thread(target=self.read_process_output)
        self.process_output_reader_thread.start()

    def read_process_output(self):
        while True:
            output = self.process.stdout.readline()
            if output == "" and self.process.poll() is not None:
                break
            if output:
                self.append_output_signal.emit(output)
                self.set_status_indicator_color("green" if "SUCCESS" in output else "red")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
