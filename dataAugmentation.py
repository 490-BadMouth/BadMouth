import numpy as np
import soundfile as sf
import librosa

import librosa.display
import matplotlib.pyplot as plt

import fnmatch
import os

# signal is the waveform in numpy form
def addWhiteNoise(signal, noiseFactor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noiseFactor
    return augmented_signal

# pitch scaling
def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr, num_semitones)

# plot signals
def plot_signal_with_augmented(signal, augmentedSignal,sr ):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveshow(signal, sr=sr, ax=ax[0])
    ax[0].set(title="Original Signal")
    librosa.display.waveshow(augmentedSignal, sr=sr, ax=ax[1])
    ax[1].set(title="Augmented Signal")
    plt.show()

if __name__ == "__main__":
    # process all files and add white  noise (20%)
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.wav'):
            signal, sampleRate = librosa.load(file)
            augmented_signal = addWhiteNoise(signal, 0.2)
            sf.write("whiteNoise_0_2_" + file, augmented_signal, sampleRate)

    # process all files and change pitch scale
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.wav'):
            signal, sampleRate = librosa.load(file)
            augmented_signal = pitch_scale(signal, sampleRate, 0.5)
            sf.write("pitchScalePos0_5" + file, augmented_signal, sampleRate)

    # convert to 16-bit wav file
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.wav'):
            data, samplerate = sf.read(file)
            sf.write(file, data, samplerate, subtype='PCM_16')