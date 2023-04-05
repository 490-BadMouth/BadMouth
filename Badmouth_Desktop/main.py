import sys
import socket
from subprocess import Popen, PIPE, call
import threading
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QColor, QPalette, QTextCursor, QPixmap

#Bash script for virtual mic setup through Port Audio
BASH_SCRIPT = "bash vmic3.sh"  
#Connection Info
CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 1024 * 4
#Virtual Mic Path for pipe to connect
PIPE_PATH = "/tmp/Badmouth"

class MainWindow(QMainWindow):
    append_output_signal = Signal(str)

    def __init__(self):
        super().__init__()

        # Set up the UI
        print("Initializing UI...")
        self.init_ui()

        # Connect the append_output_signal to the append_output slot
        self.append_output_signal.connect(self.append_output)

        # Run the bash script in a separate thread to avoid blocking the GUI
        print("Running Bash Script...")
        self.run_bash_script()

        print("Attempting to connect stream...")
        self.connect_stream()

        self.running_indicator_init()



    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.status_indicator = QLabel("Status")
        self.status_indicator.setAutoFillBackground(True)
        self.set_status_indicator_color("red")
        layout.addWidget(self.status_indicator)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFixedSize(300,800)
        layout.addWidget(self.output_text)

        # Image
        self.image_label = QLabel()
        #pixmap = QPixmap("pain.png")
        pixmap = QPixmap("bad duck.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        layout.addWidget(self.image_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # Set window size and aspect ratio
        self.setFixedSize(300,450)

    def set_status_indicator_color(self, color_name):
        palette = self.status_indicator.palette()
        color = QColor(color_name)
        palette.setColor(QPalette.Window, color)
        self.status_indicator.setPalette(palette)

    def append_output(self, text):
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.textCursor().deletePreviousChar()
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.insertPlainText(text)
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.insertPlainText(self.running_indicator.text())

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

    def connect_stream(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(2)  # Added timeout to avoid blocking
        self.process_poll_socket_connect = threading.Thread(target=self.poll_connection)
        self.process_poll_socket_connect.start()

    def poll_connection(self):
        while True:
            try:
                self.sock.sendto(b"connect", (CORAL_IP, PORT))
                data, _ = self.sock.recvfrom(CHUNK)
                print(data)
            except socket.timeout:  # Handle timeout exception
                continue
            except Exception as e:
                print("Error while polling connection: ", e)
                self.sock.close()
                break

            if data == b"connected":
                print("Connected.")
                self.append_output_signal.emit("BadMouth connection established, beginning stream...\n")
                break

        self.set_status_indicator_color("green")
        try:
            print("Opening pipe.")
            with open(PIPE_PATH, "wb") as pipe:
                self.set_status_indicator_color("green")
                while True:
                    data, _ = self.sock.recvfrom(CHUNK * 4)
                    pipe.write(data)
        except Exception as e:
            print("Error while receiving audio stream: ", e)
            self.append_output_signal.emit("Error while receiving audio stream: ", e)
            self.set_status_indicator_color("red")
            self.sock.close()

    def update_running_indicator(self):
        self.indicator_i += 1
        new_txt = self.indicator_text[(self.indicator_i + 1) % 4]
        self.running_indicator.setText(new_txt)

        # Remove the current running indicator character
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.textCursor().deletePreviousChar()

        # Add the updated running indicator character
        self.output_text.moveCursor(QTextCursor.End)
        self.output_text.insertPlainText(self.running_indicator.text())

    def running_indicator_init(self):
        # Initialize running indicator
        self.running_indicator = QLabel()
        self.indicator_text = "|/-\\"
        self.indicator_i = 0
        self.running_indicator.setText("|")

        # Set up a timer to update the running indicator
        self.running_indicator_timer = QTimer()
        self.running_indicator_timer.timeout.connect(self.update_running_indicator)
        self.running_indicator_timer.start(150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
