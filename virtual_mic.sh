#!/bin/bash
if pactl list short modules | grep -q "source_name=Badmouth file=/tmp/Badmouth" ; then
    echo 'Virtual Mic Exists: Module #'
    module="$(pactl list short modules | awk '/source_name=Badmouth/ {print $1}')"
    echo "$module"
else
    echo 'Virtual Mic Created: Module #'
    pactl load-module module-pipe-source source_name=Badmouth file=/tmp/Badmouth format=s16le rate=44100 channels=1
fi