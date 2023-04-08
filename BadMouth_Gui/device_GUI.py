# This Python file uses the following encoding: utf-8
import sys
import socket
from subprocess import Popen, PIPE, call
import threading
import json
import time
import traceback
import struct
import pyaudio as pa
import numpy as np
import matplotlib
import random
from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSettings
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

#Bash script for virtual mic setup through Port Audio
BASH_SCRIPT = "bash audio_sender_v3.sh"  

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Run the bash script in a separate thread to avoid blocking the GUI
        print("Running Bash Script...")
        self.run_bash_script()
        
        self.ui_init()

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

