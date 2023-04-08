import os
import glob
import datetime
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import numpy as np
from keras import models
from recorder import record_audio, terminate
from spec import preprocess
import pyaudio
import wave
import shutil

#loaded_model = models.load_model("bad_mouth_1c_16n_0d_newData.model")


def predict_mic():
    # set the recording parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 48000
    CHUNK = 2048
    RECORD_SECONDS = 1.5
    WAVE_OUTPUT_FILENAME = "recorded_file.wav"

    src_folder = "."
    dst_folder = "C:/Users/David/Documents/BadMouth/DavidThings/ML_test/recorded_bad"
    #dst_folder = "C:/Users/David/Documents/ML Training Audios/ML_test/recorded_good"

    # initialize PyAudio
    audio = pyaudio.PyAudio()

    # start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("start recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
   
    print("recording stopped")

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the recorded data as a WAV file with date and time in the filename
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    old_filename = "recorded_file.wav"
    new_filename = f"recorded_file_{now}_BAD.wav"
    #new_filename = f"recorded_file_{now}_GOOD.wav"

    wf = wave.open(old_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    os.rename(old_filename, new_filename)

    # pos = tf.data.Dataset.list_files(new_filename) 

    # # append correct label to data
    # data = tf.data.Dataset.zip((pos, tf.data.Dataset.from_tensor_slices(tf.zeros(len(pos)))))

    # # apply preprocess to all the files 
    # data = data.map(preprocess)

    # # process data in batches of 16
    # data = data.batch(16)

    # # get next batch
    # sample, labels = data.as_numpy_iterator().next()

    # #print(sample.shape)
    # prediction = loaded_model.predict(sample)
    
    
    # # iterate through the batch
    # for i in np.nditer(prediction): 
    #     if (i > 0.9):
    #         print("Bad Word  -- Prob:", i)
    #     else:
    #         print("Good word -- Prob:", i)
    shutil.move(os.path.join(src_folder, new_filename), os.path.join(dst_folder, new_filename))

    # # prediction = [1 if prediction > 0.99 else 0 for prediction in prediction]

    # return prediction

if __name__ == "__main__":
    # while True:
    predict_mic()
    terminate()