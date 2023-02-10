import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class bm_visualizer():
    def __init__(self):
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
        self.fig,ax = plt.subplots()
        x = np.arange(0,2*self.CHUNK,2)
        self.line, = ax.plot(x, np.random.rand(self.CHUNK),'r')
        ax.set_ylim(-60000,60000)
        ax.ser_xlim = (0,self.CHUNK)
        self.fig.show()

    def update_vis(self):
        data = self.stream.read(self.CHUNK)
        dataInt = struct.unpack(str(self.CHUNK) + 'h', data)
        self.line.set_ydata(dataInt)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        print("Updated")