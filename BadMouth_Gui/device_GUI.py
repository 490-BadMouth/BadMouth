# This Python file uses the following encoding: utf-8
import sys
from subprocess import Popen, PIPE, call
import threading
import socket
import pyaudio
from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThread, QSettings, Qt


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 512 * 5
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

class AudioThread(QThread):
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((CORAL_IP, PORT))

        print("Waiting for connection...")

        while True:
            data, host_addr = sock.recvfrom(CHUNK)
            if data == b"connect":
                sock.sendto(b"connected", host_addr)
                break

        print("Connected to host @: ", host_addr)

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("Sending audio stream to", host_addr)
        try:
            while True:
                data = stream.read(CHUNK)
                sock.sendto(data, host_addr)
        except Exception as e:
            print("Error while streaming audio:", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt!!!")
            stream.stop_stream()
            stream.close()
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()
            sock.close()
            
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Set the window flags to be frameless, not frameless for demo
        #self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui_init()

        self.audio_thread = AudioThread(self)
        self.audio_thread.start()

    def home_widget(self):
        print("Hello I am Home")
        self.ui.stackedWidget_content.setCurrentIndex(0)

    def eq_widget(self):
        self.ui.stackedWidget_content.setCurrentIndex(1)

    def vis_widget(self):
        self.ui.stackedWidget_content.setCurrentIndex(2)
        
    def stat_widget(self):
        self.ui.stackedWidget_content.setCurrentIndex(3)
    
    def reset_widget(self):
        self.ui.main_count.display(0)
        self.ui.f_bomb_count.display(0)
        self.ui.s_disposed_count.display(0)
        self.ui.ass_count.display(0)
        self.ui.nasty_count.display(0)
        self.ui.d_blocked_count.display(0)
                
    def ui_init(self):
        self.ui.stackedWidget_content.setCurrentIndex(0)
        self.ui.label_enabled.setHidden(True)
        self.ui.pushButton_home.clicked.connect(self.home_widget)
        self.ui.pushButton_eq.clicked.connect(self.eq_widget)
        self.ui.pushButton_vis.clicked.connect(self.vis_widget)
        self.ui.pushButton_stats.clicked.connect(self.stat_widget)
        self.ui.reset_stats.clicked.connect(self.reset_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.showMaximized()
    sys.exit(app.exec_())