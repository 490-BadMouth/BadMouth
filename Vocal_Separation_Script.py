#imports
from __future__ import print_function
from operator import index
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import soundfile as sf
import os



def vocal_separation(file_path, Newfile_path):
    
    #############################################
    # Load an example with vocals.
    y, sr = librosa.load(file_path)

    # And compute the spectrogram magnitude and phase
    S_full, phase = librosa.magphase(librosa.stft(y))


    #######################################
    # Plot a 5-second slice of the spectrum
    idx = slice(*librosa.time_to_frames([0, 5], sr=sr))
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(librosa.amplitude_to_db(S_full[:, idx], ref=np.max),
                            y_axis='log', x_axis='time', sr=sr)
    plt.colorbar()
    plt.tight_layout()

    ###########################################################
    # The wiggly lines above are due to the vocal component.
    # Our goal is to separate them from the accompanying
    # instrumentation.
    #

    # We'll compare frames using cosine similarity, and aggregate similar frames
    # by taking their (per-frequency) median value.
    #
    # To avoid being biased by local continuity, we constrain similar frames to be
    # separated by at least 2 seconds.
    #
    # This suppresses sparse/non-repetetitive deviations from the average spectrum,
    # and works well to discard vocal elements.

    S_filter = librosa.decompose.nn_filter(S_full,
                                        aggregate=np.median,
                                        metric='cosine',
                                        width=int(librosa.time_to_frames(.5, sr=sr)))

    # The output of the filter shouldn't be greater than the input
    # if we assume signals are additive.  Taking the pointwise minimium
    # with the input spectrum forces this.
    S_filter = np.minimum(S_full, S_filter)


    ##############################################
    # The raw filter output can be used as a mask,
    # but it sounds better if we use soft-masking.

    # We can also use a margin to reduce bleed between the vocals and instrumentation masks.
    # Note: the margins need not be equal for foreground and background separation
    margin_i, margin_v = 2, 10
    power = 2

    mask_i = librosa.util.softmask(S_filter,
                                margin_i * (S_full - S_filter),
                                power=power)

    mask_v = librosa.util.softmask(S_full - S_filter,
                                margin_v * S_filter,
                                power=power)

    # Once we have the masks, simply multiply them with the input spectrum
    # to separate the components

    S_foreground = mask_v * S_full
    S_background = mask_i * S_full

    ################### .WAV OUTPUT OF FOREGROUND #######
    D_foreground = S_foreground * phase

    Y_foreground = librosa.istft(D_foreground)

    sf.write(Newfile_path,Y_foreground,sr)



PDIR = "audio" # folder where all audio folders are located 

words = np.array(tf.io.gfile.listdir(str(PDIR)))
words = words [words != 'README.md']
print('Words:',words)

for dir in words:
    FolderName = dir + "__Foregrounds"
    newFolder = os.path.join(PDIR,FolderName) 
    os.mkdir(newFolder)
    
    DATADIR = os.path.join(PDIR,dir) 
    fileNum = 0
    for file in os.scandir(DATADIR):
        if file.is_file():
            fileNum += 1
            FILEPATH = file.path
            NewfileName = dir + "__Foreground" + str(fileNum) +".wav"
            Newfile_path = os.path.join(newFolder,NewfileName) 
            vocal_separation(file, Newfile_path)




