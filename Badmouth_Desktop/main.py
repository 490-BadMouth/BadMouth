import sys
import os
import socket
from subprocess import Popen, PIPE, call
import threading
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout,QHBoxLayout, QWidget, QLabel, QDial, QLCDNumber
from PySide6.QtGui import QColor, QPalette, QTextCursor, QPixmap

#Bash script for virtual mic setup through Port Audio
BASH_SCRIPT = "bash vmic3.sh"  
#Connection Info
CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 1024 * 4
#Virtual Mic Path for pipe to connect
PIPE_PATH = "/tmp/Badmouth"

indicator_i = 0


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
        self.stream_init()

        self.running_indicator_init()

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()

        left_column_layout = QVBoxLayout()

        self.status_indicator = QLabel("Status")
        self.status_indicator.setAutoFillBackground(True)
        self.set_status_indicator_color("red")
        left_column_layout.addWidget(self.status_indicator)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFixedSize(256, 400)
        left_column_layout.addWidget(self.output_text)

        self.image_label = QLabel()
        pixmap = QPixmap("bad duck.png")
        scaled_pixmap = pixmap.scaled(256, 232, Qt.AspectRatioMode.KeepAspectRatio)  # fix duck aspect ratio
        self.image_label.setPixmap(scaled_pixmap)  # for scaled pixmap
        self.image_label.setScaledContents(True)
        left_column_layout.addWidget(self.image_label)

        main_layout.addLayout(left_column_layout)

        right_column_layout = QVBoxLayout()

        # Add dial widget
        self.volume_dial = QDial()
        self.volume_dial.setRange(0, 100)
        self.volume_dial.valueChanged.connect(self.set_microphone_volume)
        self.volume_dial.setFixedSize(256, 232)

        # Add 7-segment display
        self.volume_display = QLCDNumber()
        self.volume_display.setDigitCount(3)
        # Update Display with dial
        self.volume_dial.valueChanged.connect(self.volume_display.display)
 
        right_column_layout.addWidget(self.volume_display)
        right_column_layout.addWidget(self.volume_dial)

        main_layout.addLayout(right_column_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        # Set window size and aspect ratio
        self.setFixedSize(512, 800)

    def set_microphone_volume(self, value):

        # Set the microphone volume using the pactl command
        os.system(f"pactl set-source-volume @DEFAULT_SOURCE@ {value}%")

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

    def stream_init(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(2)  # Added timeout to avoid blocking
        self.process_poll_socket_connect = threading.Thread(target=self.stream_connect)
        self.process_poll_socket_connect.start()

    def stream_connect(self):
        while True:
            try:
                self.sock.sendto(b"connect", (CORAL_IP, PORT))
                data, _ = self.sock.recvfrom(CHUNK)
                print(data)
                self.runner_indicator = True
            except socket.timeout:  # Handle timeout exception
                continue
            except Exception as e:
                print("Error while polling connection: ", e)
                self.sock.close()
                break

            if data == b"connected":
                print("Connected.")
                self.append_output_signal.emit("BadMouth connection established, beginning stream...\n")
                self.runner_indicator = True
                break

        self.set_status_indicator_color("green")
        try:
            print("Opening pipe.")
            self.runner_indicator = True            
            with open(PIPE_PATH, "wb") as pipe:
                self.set_status_indicator_color("green")
                self.runner_indicator = True
                while data is not None:
                    data, _ = self.sock.recvfrom(CHUNK * 4)
                    pipe.write(data)
        except Exception as e:
            print("Error while receiving audio stream: ", e)
            self.append_output_signal.emit("Error while receiving audio stream.")
            self.set_status_indicator_color("red")
            self.runner_indicator = False
            self.sock.close()

    def update_running_indicator(self):
        if self.runner_indicator:
            global indicator_i
            new_txt = self.indicator_text[(indicator_i % 4)]
            indicator_i += 1
            self.running_indicator.setText(new_txt)

            # Remove the current running indicator character
            self.output_text.moveCursor(QTextCursor.End)
            self.output_text.textCursor().deletePreviousChar()

            # Add the updated running indicator character
            self.output_text.moveCursor(QTextCursor.End)
            self.output_text.insertPlainText(self.running_indicator.text())
        else:
            self.indicator_text = "00"
            self.running_indicator_init()
            
    def running_indicator_init(self):
        # Initialize running indicator
        self.running_indicator = QLabel()
        self.indicator_text = "|/-\\"
        self.running_indicator.setText("|")
        self.runner_indicator = False

        # Set up a timer to update the running indicator
        self.running_indicator_timer = QTimer()
        self.running_indicator_timer.timeout.connect(self.update_running_indicator)
        self.running_indicator_timer.start(150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())