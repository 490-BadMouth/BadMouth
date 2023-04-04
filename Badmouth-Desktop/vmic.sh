#!/bin/bash

echo 'Checking for Virtual Input...'

if pactl list short modules | grep -q "source_name=Badmouth file=/tmp/Badmouth "; then 
   echo 'Virtual Mic exists' 
else 
   echo 'Virtual Mic does not exist, creating a new virtual input...'
   pactl load-module module-pipe-source source_name=Badmouth file=/tmp/Badmouth format=s16le rate=44100 channels=1
   echo 'Virtual Mic created.'
fi