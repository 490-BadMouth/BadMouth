# This Python file uses the following encoding: utf-8
import sys, os
from subprocess import Popen, PIPE, call

from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication, QAbstractButton
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThread, QSettings, Qt

# Run this in terminal to enable LCD: export DISPLAY=:0.0

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from audio_thread import AudioThread
from uart_thread import UartThread

class MainWindow(QMainWindow):

    uart_data_received = Signal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Set the window flags to be frameless, not frameless for demo
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.page_index = 0
        self.dial_index = 0

        self.filter_on = True

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui_init()

        self.uart_data_received.connect(self.update_uart_data)

        self.uart_thread = UartThread()
        self.uart_thread.uart_data_received.connect(self.uart_data_received.emit)
        self.uart_thread.start()

        self.audio_thread = AudioThread()
        self.audio_thread.start()

    def update_uart_data(self,data):
        print("UART Data Received:", data)
        self.ui.label_UART_in.setText(data)
        if data == 'U':
            self.page_select('U')
            print("Page Index: ",self.page_index)
        elif data == 'D':
            self.page_select('D')
            print("Page Index: ",self.page_index)
        elif data == 'L':
            self.dial_select('L')
        elif data == 'R':
            self.dial_select('R')
        elif data =='C':
             sys.exit(app.exec_())
        else:
            self.dial_update(int(data))

    def update_dial_labels(self):
        labels = [self.ui.label_bass, self.ui.label_mid, self.ui.label_treb, self.ui.label_vol]
        for index, label in enumerate(labels):
            if index == self.dial_index:
                label.setStyleSheet("QLabel { color : red; }")
            else:
                label.setStyleSheet("QLabel { color : black; }")
    
    def update_page_buttons(self):
        buttons = [self.ui.pushButton_home, self.ui.pushButton_eq, self.ui.pushButton_vis, self.ui.pushButton_stats]
        for index, button in enumerate(buttons):
            if index == self.page_index:
                button.setStyleSheet("QPushButton { color : red; }")
            else:
                button.setStyleSheet("QPushButton { color : black; }")

    def page_select(self, direction):
        if direction == 'U':
            self.page_index = (self.page_index - 1) % 4
            self.ui.stackedWidget_content.setCurrentIndex(self.page_index)

        elif direction == 'D':
            self.page_index = (self.page_index + 1) % 4
            self.ui.stackedWidget_content.setCurrentIndex(self.page_index)
        if self.ui.stackedWidget_content.currentIndex() == 1:
            self.update_dial_labels()
        self.update_page_buttons()

    def dial_select(self,direction):
        if self.ui.stackedWidget_content.currentIndex() == 1:
            if direction == 'L':
                self.dial_index = (self.dial_index - 1) % 4
            elif direction == 'R':
                self.dial_index = (self.dial_index + 1) % 4
            print("Dial Index: ",self.dial_index)
            self.update_dial_labels()

    def dial_update(self, value):
        if self.ui.stackedWidget_content.currentIndex() == 1:
            if self.dial_index == 0:
                self.ui.dial_bass.setValue(value)
            elif self.dial_index == 1:
                self.ui.dial_mid.setValue(value)
            elif self.dial_index == 2:
                self.ui.dial_treb.setValue(value)
            elif self.dial_index == 3:
                self.ui.dial_vol.setValue(value)
                volume = int((value/15.0) * 100)
                print(f'pactl set-source-volume alsa_input.platform-sound.HiFi__hw_0_1__source {volume}%')
                os.system(f'pactl set-source-volume alsa_input.platform-sound.HiFi__hw_0_1__source {volume}%')
    
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
        #self.ui.pushButton_home.clicked.connect(self.home_widget)
        #self.ui.pushButton_eq.clicked.connect(self.eq_widget)
        #self.ui.pushButton_vis.clicked.connect(self.vis_widget)
        #self.ui.pushButton_stats.clicked.connect(self.stat_widget)
        #self.ui.reset_stats.clicked.connect(self.reset_widget)
        self.ui.pushButton_pato.clicked.connect(self.toggle_filter)
        self.update_page_buttons()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.showMaximized()
    sys.exit(app.exec_())