import numpy as np
import tensorflow as tf
import tensorflow_io as tfio

def load_wav_16k_mono(filename):
    # Load encoded wav file
    file_contents = tf.io.read_file(filename)
    # Decode wav (tensors by channels) 
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    # Removes trailing axis
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    # Goes from 44100Hz to 16000hz - amplitude of the audio signal
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav

#spec 
def preprocess(file_path, label): 
    wav = load_wav_16k_mono(file_path)
    wav = wav[:35000] # 35000 sample length (can make smaller to reduce processing time but will affect accuracy)
    zero_padding = tf.zeros([35000] - tf.shape(wav), dtype=tf.float32) 
    wav = tf.concat([zero_padding, wav],0) # pad clips longer than 25000 samples wiht zeros
    spectrogram = tf.signal.stft(wav, frame_length=320, frame_step=32)
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.expand_dims(spectrogram, axis=2)
    return spectrogram, label



def preprocessing_Audio(waveform, rate):
    waveform = waveform/32768
    waveform = tf.convert_to_tensor(waveform, dtype = tf.float32)
    sample_rate = tf.convert_to_tensor(rate, dtype = tf.float32)
    spec = preprocess(waveform, sample_rate)
    spec = tf.expand_dims(spec,0)

    return spec

