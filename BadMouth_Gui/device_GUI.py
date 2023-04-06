# This Python file uses the following encoding: utf-8
import sys
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

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.x = np.arange(0,2*self.CHUNK,2)
        self.line, = self.canvas.axes.plot(self.x, np.random.rand(self.CHUNK),'r')
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.set_ylim(-20000,20000)
        self.canvas.axes.ser_xlim = (0,self.CHUNK)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui_init()

    def update_plot(self):
        worker = Worker(self.update_plot)

        if(self.ui.stackedWidget_content.currentIndex() == 2):
            data = self.stream.read(self.CHUNK)
            ydata = struct.unpack(str(self.CHUNK) + 'h', data)

            if self._plot_ref is None:
                # First time we have no plot reference, so do a normal plot.
                # .plot returns a list of line <reference>s, as we're
                # only getting one we can take the first element.
                plot_refs = self.canvas.axes.plot(self.x, ydata, 'r')
                self._plot_ref = plot_refs[0]
            else:
                # We have a reference, we can use it to update the data for that line.
                self._plot_ref.set_ydata(ydata)        

            # Trigger the canvas to update and redraw.
            self.canvas.draw()

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
    config = bm_config()
    widget.show()
    widget.showMaximized()
    sys.exit(app.exec_())

