# This Python file uses the following encoding: utf-8
import sys
import struct
import pyaudio as pa
import numpy as np
import matplotlib
import random
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QTimer
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):

    def update_plot(self):

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

    def set_page(self,i):
        self.ui.stackedWidget_content.setCurrentIndex(i)

    def init_ui(self):
        print("init ui")
        self.ui.pushButton_home.clicked.connect(set_page(0))
        self.ui.pushButton_eq.clicked.connect(set_page(1))
        self.ui.pushButton_vis.clicked.connect(set_page(2))
        self.ui.pushButton_stats.clicked.connect(set_page(3))
        print("buttons connected")

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.CHUNK = 1024 * 2
        FORMAT = pa.paInt16
        CHANNELS = 1
        RATE = 44100 # in Hz

        p = pa.PyAudio()

        self.stream = p.open(
            format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )        

        self.x = np.arange(0,2*self.CHUNK,2)
        self.line, = self.canvas.axes.plot(self.x, np.random.rand(self.CHUNK),'r')
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.set_ylim(-10000,10000)
        self.canvas.axes.ser_xlim = (0,self.CHUNK)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.ui.gridLayout_plot.addWidget(self.canvas)

        # We need to store a reference to the plotted line
        # somewhere, so we can apply the new data to it.
        self._plot_ref = None
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())