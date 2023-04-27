from keras import models
from recorder import record_audio, terminate
from spec import preprocess
import numpy as np


model= models.load_model("prediction_model.h5") 


def predict_mic():   
    
    spec = record_audio()

    spec= preprocess(spec) # input: waveform and sample rate spec
  
    prediction = model.predict(spec)
    
    print (prediction)
    
    prediction = np.argmax(prediction, axis = 1)
    
    print(prediction)

    
    
    if (prediction == 0):
        print("Good Word")
    
    elif (prediction == 1):
        print('Fuck')
    else:
        print("Shit")
        
        
    
    
    return prediction


if __name__ == "__main__":
    predict_mic()  
    terminate() 

        
    
    
    
    
    
    