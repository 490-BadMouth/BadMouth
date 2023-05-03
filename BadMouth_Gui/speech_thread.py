'''
import warnings
warnings.filterwarnings("ignore")

# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
'''

import warnings
warnings.filterwarnings("ignore")

import speech_recognition as sr
import os
from pydub import AudioSegment
import pyaudio

# List of words to remove or dub over
blocked_words = ["fuck", "shit"]

# Function to remove or dub over specific words
def filter_blocked_words(audio_data, words_data, silence_audio):
    filtered_audio = AudioSegment.empty()
    prev_end = 0
    for word_data in words_data:
        word = word_data["word"]
        if word.lower() in blocked_words:
            start_time = int(word_data["start"] * 1000)
            end_time = int(word_data["end"] * 1000)
            filtered_audio += audio_data[prev_end:start_time] + silence_audio[(end_time-start_time)]
            prev_end = end_time
        else:
            start_time = int(word_data["start"] * 1000)
            end_time = int(word_data["end"] * 1000)
            filtered_audio += audio_data[start_time:end_time]
            prev_end = end_time
    return filtered_audio

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    response = r.recognize_google(audio_data, show_all=True)
    
    if response and "alternative" in response:
        alternatives = response["alternative"]
        transcript = alternatives[0]["transcript"]
        words_data = alternatives[0]["words"]
        print(transcript)

        # Get the raw audio data and convert it to an AudioSegment
        raw_audio_data = audio_data.get_wav_data()
        input_audio = AudioSegment.from_wav(io.BytesIO(raw_audio_data))

        # Create a silent audio segment to dub over the blocked words
        silence_audio = AudioSegment.silent(duration=1000)

        # Filter the blocked words and get the filtered audio
        filtered_audio = filter_blocked_words(input_audio, words_data, silence_audio)

        # Save the filtered audio
        filtered_audio.export("filtered_audio.wav", format="wav")
        print("Filtered audio saved as filtered_audio.wav")
        
