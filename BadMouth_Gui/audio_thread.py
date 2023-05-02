from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import model
import numpy as np

import pyaudio, threading, socket, numpy as np

from PySide2.QtCore import QThread

'''
    CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
    PORT = 5000
    CHUNK = 512 * 5
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
'''
class AudioThread(QThread):

    def __init__(self, parent = None, coral_ip = "192.168.100.2", port = 5000, chunk = 2560, format = pyaudio.paInt16, channels = 1, rate = 44100):
        super(AudioThread, self).__init__(parent)
        self.coral_ip = coral_ip
        self.port = port
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.filter_on = False
        
    def run(self):
        self.stream_audio()

    def stream_audio(self):    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.coral_ip, self.port))

        print("Waiting for connection...")
        try:
            while True:
                data, host_addr = sock.recvfrom(self.chunk)
                if data == b"connect":
                    sock.sendto(b"connected", host_addr)
                    break
        except KeyboardInterrupt:
            print("Aborting")
            sock.close()
            exit()

        print("Connected to host @: ", host_addr)

        p = pyaudio.PyAudio()
        stream = p.open(format=self.format, channels=self.channels, rate=self.rate, input= True, frames_per_buffer= self.chunk)

        print("Sending audio stream to", host_addr)
        try:
            while True:
                data = stream.read(self.chunk)

                # This is where the pyaudio stream data is inputted into the filter and outputted to the socket.
                #if(filter_on):
                 #   print("OOO LAWD ITS FILTERIN")
                # parser = argparse.ArgumentParser()
                # model.add_model_flags(parser)
                # args = parser.parse_args()
                # interpreter = model.make_interpreter(args.model_file)
                # interpreter.allocate_tensors()
                # mic = args.mic if args.mic is None else int(args.mic)
                # model.classify_audio(mic, interpreter,
                #                     labels_file="labels.txt",
                #                     result_callback=model.print_results,
                #                     sample_rate_hz=int(args.sample_rate_hz),
                #                     num_frames_hop=int(args.num_frames_hop))
                    sock.sendto(data, host_addr)

        except Exception as e:
            print("Error while streaming audio:", e)
        except KeyboardInterrupt:
            print("Keyboard interrupt!!!")
            stream.stop_stream()
            stream.close()
            exit()
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()
            sock.close()