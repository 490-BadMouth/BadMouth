import os 
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import numpy as np
# import keras

BAD  = os.path.join('AudioAudio','Bad')
NOTBAD = os.path.join('AudioAudio','NotBad')

bad = tf.data.Dataset.list_files(BAD+'/*.wav')
notbad = tf.data.Dataset.list_files(NOTBAD+'/*.wav')

#convert 16hz mono channel
def load_wav_16k_mono(filename):
    file_contents = tf.io.read_file(filename)
    wav,sample_rate = tf.audio.decode_wav(file_contents,desired_channels=1)
    wav = tf.squeeze(wav,axis=-1)
    sample_rate = tf.cast(sample_rate,dtype = tf.int64) #64
    wav = tfio.audio.resample(wav,rate_in=sample_rate,rate_out=16000)
    return wav






positives = tf.data.Dataset.zip((bad,tf.data.Dataset.from_tensor_slices(tf.ones(len(bad)))))
negatives = tf.data.Dataset.zip((notbad,tf.data.Dataset.from_tensor_slices(tf.zeros(len(notbad)))))
data = positives.concatenate(negatives)

#spec 
def preprocess(file_path,label):
    wav = load_wav_16k_mono(file_path)
    wav = wav[:25000]
    zero_padding = tf.zeros([25000] - tf.shape(wav), dtype=tf.float32)
    wav = tf.concat([zero_padding, wav],0)
    spectrogram = tf.signal.stft(wav, frame_length=320, frame_step=32)
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.expand_dims(spectrogram, axis=2)
    return spectrogram,label




# d = data.shuffle(1000).as_numpy_iterator().next()

# print(d)





# lengths = []
# for file in os.listdir(os.path.join('AudioAudio', 'Bad')):
#     tensor_wave = load_wav_16k_mono(os.path.join('AudioAudio', 'Bad', file))
#     lengths.append(len(tensor_wave))
    
    
# mean = tf.math.reduce_mean(lengths)
# min = tf.math.reduce_min(lengths)
# max = tf.math.reduce_max(lengths)


# print ("mean", mean )
# print (" min", min )
# print (" max", max)

    


# filepath, label = positives.shuffle(buffer_size=10000).as_numpy_iterator().next()
# spectrogram, label = preprocess(filepath, label)
# plt.figure(figsize=(30,20))
# plt.imshow(tf.transpose(spectrogram)[0])
# plt.show()




data = data.map(preprocess)

# print(data.as_numpy_iterator())

data = data.cache()
data = data.shuffle(buffer_size =1000)
data = data.batch(16)
data = data.prefetch(8)

print(len(data))
train = data.take(226) #226
test = data.skip(226).take(100) #100


samples,labels = train.as_numpy_iterator().next()


print("Shape:",samples.shape)

######################
from keras.models  import Sequential
from keras.layers  import Conv2D, Dense, Flatten


# PDIR = "AudioAudio" # folder where all audio folders are located 

# words = np.array(tf.io.gfile.listdir(str(PDIR)))
# words = words [words != 'README.md']

model = Sequential()
model.add(Conv2D(16, (3,3), activation='relu', input_shape=(1491, 257,1)))
model.add(Conv2D(16, (3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile('Adam', loss='BinaryCrossentropy', metrics=[tf.keras.metrics.Recall(),tf.keras.metrics.Precision()])

print(model.summary())

hist = model.fit(train, epochs=4, validation_data=test)



plt.title('Loss')
plt.plot(hist.history['loss'], 'r')
plt.plot(hist.history['val_loss'], 'b')
plt.show()
plt.title('Precision')
plt.plot(hist.history['precision'], 'r')
plt.plot(hist.history['val_precision'], 'b')
plt.show()
plt.title('Recall')
plt.plot(hist.history['recall'], 'r')
plt.plot(hist.history['val_recall'], 'b')
plt.show()



# print('Words:',words)



# train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
#     directory='audio',
#     batch_size=30,
#     validation_split=0.2,
#     seed=0,
#     output_sequence_length=16000,
#     subset='both')

# label_names = np.array(train_ds.class_names)
# print()
# print("label names:", label_names)

# data = os.path.join('David','fuck2.wav')
# //DATA = tf.data.Dataset.list_files(data+'/*.wav')





#dir

# for dir in words:
#     # FolderNameSpec = dir + "__ForegroundSpec"
#     # newFolderSpec = os.path.join(PDIR,FolderNameSpec) 
#     # os.mkdir(newFolderSpec)
#     DATADIR = os.path.join(PDIR,dir) 
#     fileNum = 0
    
#     for file in os.scandir(DATADIR):
#         if file.is_file():
#             fileNum += 1
#             FILEPATH = file.path
#             plt.figure(figsize = (12,8))
#             plt.imshow(tf.transpose(preprocess(FILEPATH))[0])
#             plt.show()









    







