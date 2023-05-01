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
        #self.setWindowFlags(Qt.FramelessWindowHint)
        
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

        #self.focus_manager = FocusManager([self.ui.pushButton_home,
        #                                    self.ui.pushButton_eq,
        #                                    self.ui.pushButton_vis,
        #                                    self.ui.pushButton_stats
        #                                    ], self)


    def update_uart_data(self,data):
        print("UART Data Received:", data)
        self.ui.label_UART_in.setText(data)
        if data == 'U':
            #self.focus_manager.focus_prev()
            os.system('echo "Test"')
        elif data == 'D':
            #self.focus_manager.focus_next()
            pass
        elif data == 'L':
            #self.focus_manager.focus_left()
            pass
        elif data == 'R':
            #self.focus_manager.focus_right()
            pass
        elif data[0] =='C':
            sys.exit(app.exec_())

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

'''
class FocusManager:
    def __init__(self, pages, main_window):
        self.pages = pages
        self.main_window = main_window
        self.page_index = 0
        self.page_items = self.pages[self.page_index]
        self.item_index = 0
        self.set_focus(self.page_items[self.item_index])

    def set_focus(self, widget):
        if isinstance(widget, QWidget):
            widget.setFocus()

    def focus_next(self):
        self.item_index = (self.item_index + 1) % len(self.page_items)
        self.set_focus(self.page_items[self.item_index])

    def focus_prev(self):
        self.item_index = (self.item_index - 1) % len(self.page_items)
        self.set_focus(self.page_items[self.item_index])

    def activate(self):
        item = self.page_items[self.item_index]
        if isinstance(item, QAbstractButton):
            item.click()

    def focus_left(self):
        self.page_up()

    def focus_right(self):
        self.page_down()

    def page_up(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.page_items = self.pages[self.page_index]
            self.item_index = 0
            self.set_focus(self.page_items[self.item_index])

    def page_down(self):
        if self.page_index < len(self.pages) - 1:
            self.page_index += 1
            self.page_items = self.pages[self.page_index]
            self.item_index = 0
            self.set_focus(self.page_items[self.item_index])
'''

if __name__ == "__main__":
    os.system("export DISPLAY=:0.0") # Set GUI to display on LCD
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.showMaximized()
    sys.exit(app.exec_())