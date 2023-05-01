#!/bin/bash
pactl --v
pactl list short modules | awk '/source_name=Badmouth/ {print $2, $3}\'
echo "Testing...Testing 1...2...3..."
if pactl list short modules | grep -q "source_name=Badmouth file=/tmp/Badmouth" ; then
    module="$(pactl list short modules | awk '/source_name=Badmouth/ {print $1}')"
    echo -n 'Virtual Mic Exists: Module #'$module''
    echo ""
else
    pactl load-module module-pipe-source source_name=Badmouth file=/tmp/Badmouth format=s16le rate=44100 channels=1 > /dev/null
    module="$(pactl list short modules | awk '/source_name=Badmouth/ {print $1}')"
    echo 'Virtual Mic Created: Module #'$module''
    if test -f "module_number.txt" ; then
        rm -rf "module_number.txt"
    fi
    echo $(pactl list short modules | awk '/source_name=Badmouth/ {print $1}') >> module_number.txt
fi
