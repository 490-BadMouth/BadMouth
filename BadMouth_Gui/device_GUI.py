# This Python file uses the following encoding: utf-8
import sys, os
from subprocess import Popen, PIPE, call

from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThread, QSettings, Qt

# Run this in terminal to enable LCD: export DISPLAY=:0.0

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from audio_stream import AudioThread

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Set the window flags to be frameless, not frameless for demo
        #self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.filter_on = True

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui_init()

        self.audio_thread = AudioThread()
        self.audio_thread.start()

    def home_widget(self):
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

    def toggle_filter(self):
        self.filter_on = not self.filter_on
                
    def ui_init(self):
        self.ui.stackedWidget_content.setCurrentIndex(0)
        self.ui.label_enabled.setHidden(True)
        self.ui.pushButton_home.clicked.connect(self.home_widget)
        self.ui.pushButton_eq.clicked.connect(self.eq_widget)
        self.ui.pushButton_vis.clicked.connect(self.vis_widget)
        self.ui.pushButton_stats.clicked.connect(self.stat_widget)
        self.ui.reset_stats.clicked.connect(self.reset_widget)
        self.ui.pushButton_pato.clicked.connect(self.toggle_filter)


if __name__ == "__main__":
    os.system("export DISPLAY=:0.0") # Set GUI to display on LCD
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.showMaximized()
    sys.exit(app.exec_())
