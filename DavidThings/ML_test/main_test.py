import os
import glob
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import numpy as np


from keras import models

from recorder import record_audio, terminate
from spec import preprocess


loaded_model = models.load_model("bad_mouth_1c_16n_0d_newData.model")

def predict_mic():
    # audio,rate = record_audio()
    # spec = preprocessing_Audio(audio,rate)
    
    #audio,rate= record_audio()
    
    #spec= preprocessing_Audio(audio,rate)
    
    # testing with actual sample from data 
    BAD = os.path.join("C:/Users/David/Documents/ML Training Audios/ML_test/test_negs")
    #BAD_FILE = os.path.join("C:/Users/jreye/OneDrive/CSULB/CECS_490/ml/test/test.wav")
    pos = tf.data.Dataset.list_files((BAD+'\*.wav'), shuffle = False) 
    
    # append correct label to data
    data = tf.data.Dataset.zip((pos, tf.data.Dataset.from_tensor_slices(tf.zeros(len(pos)))))

    # apply preprocess to all the files 
    data = data.map(preprocess)

    # process data in batches of 16
    data = data.batch(17)

    # prefetch 8 values (not sure if this is needed for predicting)
    #data = data.prefetch(8)

    # get next batch
    sample, labels = data.as_numpy_iterator().next()

    #print(sample.shape)
    prediction = loaded_model.predict(sample)
    
    #print(prediction.shape)
    
    # iterate through the batch
    for i in np.nditer(prediction): 
        if (i > 0.9):
            print("Bad Word  -- Prob:", i)
        
        else:
            print("Good word -- Prob:", i)
    

    # prediction = [1 if prediction > 0.99 else 0 for prediction in prediction]

    return prediction


if __name__ == "__main__":
    # while True:
    predict_mic()
    terminate()
        