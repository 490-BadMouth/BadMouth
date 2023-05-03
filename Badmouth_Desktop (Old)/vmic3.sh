pactl --version
pactl list short modules | awk '/source_name=Badmouth/ {print $2, $3}\'
echo "Testing...Testing 1...2...3..."
if pactl list short modules | grep -q "source_name=Badmouth file=/tmp/Badmouth" ; then
    echo -n 'Virtual Mic Exists: Module # '
    module="$(pactl list short modules | awk '/source_name=Badmouth/ {print $1}')"
    echo "$module"
else
    echo 'Virtual Mic Created: Module #'
    pactl load-module module-pipe-source source_name=Badmouth file=/tmp/Badmouth format=s16le rate=44100 channels=1
    if test -f module_number.txt; then
        rm -rf module_number.txt
    else
        echo 'Virtual Mic creation failed.'
    fi
    echo $(pactl list short modules | awk '/source_name=Badmouth/ {print $1}') >> module_number.txt
fi