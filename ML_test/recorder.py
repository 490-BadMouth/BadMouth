import pyaudio
import wave
import numpy as np

FRAMES_PER_BUFFER = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

def record_audio():
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    print("start recording...")

    frames = []
    seconds = 1
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    
    wf = wave.open("recorded.wav", "wb")
    # set the channels
    wf.setnchannels(CHANNELS)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(RATE)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    
    return np.frombuffer(b''.join(frames), dtype=np.int16),RATE


def terminate():
    p.terminate()



# import os 
# from matplotlib import pyplot as plt
# import tensorflow as tf
# import tensorflow_io as tfio
# import pyaudio
# import wave


# def record_audio():
#     # the file name output you want to record into
#     filename = "recorded.wav"
#     # set the chunk size of 1024 samples
#     chunk = 1024*2
#     # sample format
#     FORMAT = pyaudio.paInt16
#     # mono, change to 2 if you want stereo
#     channels = 1
#     # 44100 samples per second
#     sample_rate = 44100
#     record_seconds = 2
#     # initialize PyAudio object
#     p = pyaudio.PyAudio()
#     # open stream object as input & output
#     stream = p.open(format=FORMAT,
#                     channels=channels,
#                     rate=sample_rate,
#                     input=True,
#                     output=True,
#                     frames_per_buffer=chunk)
#     frames = []
#     print("Recording...")
#     for i in range(int(sample_rate / chunk * record_seconds)):
#         data = stream.read(chunk)
#         # if you want to hear your voice while recording
#         # stream.write(data)
#         frames.append(data)
#     print("Finished recording.")
#     # stop and close stream
#     stream.stop_stream()
#     stream.close()
#     # terminate pyaudio object
#     p.terminate()
#     # save audio file
#     # open the file in 'write bytes' mode
#     wf = wave.open(filename, "wb")
#     # set the channels
#     wf.setnchannels(channels)
#     # set the sample format
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     # set the sample rate
#     wf.setframerate(sample_rate)
#     # write the frames as bytes
#     wf.writeframes(b"".join(frames))
#     # close the file
#     wf.close()

#     return filename