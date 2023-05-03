from periphery import Serial
from PySide2.QtCore import QThread, Signal

class UartThread(QThread):

    uart_data_received = Signal(str)

    def __init__(self, port='/dev/ttyS1', baudrate=115200, parent=None):
        super(UartThread, self).__init__(parent)
        self.uart = Serial(port, baudrate)

    def run(self):
        line_buffer = ''
        while True:
            data = self.uart.read(1)
            if data:
                decoded_data = data.decode('utf-8')
                if decoded_data == '\n':
                    self.uart_data_received.emit(line_buffer)
                    line_buffer = ''
                else:
                    line_buffer += decoded_data

    def __del__(self):
        self.uart.close()
