#!/bin/bash
if pactl list short modules | grep -q "source_name=Badmouth file=/tmp/Badmouth" ; then
    echo 'Virtual Mic Exists: Module #'
    module="$(pactl list short modules | awk '/source_name=Badmouth/ {print $1}')"
    echo "$module"
    read -n1 -p 'Do you want to remove this module? (y for yes, n for no): ' input
    if [[ $input == "Y" || $input == "y" ]]; then
        echo ''
        pactl unload-module $module
        echo 'Module Removed'
    else
        echo ''
    fi
else
    echo 'Virtual Mic Created: Module #'
    pactl load-module module-pipe-source source_name=Badmouth file=/tmp/Badmouth format=s16le rate=44100 channels=1
fi