#!/bin/bash
export DISPLAY=:0.0

# Display GUI on external LCD
# Give permissions to send/receive UART
uart_path="/dev/ttyS1"
mainwindow_path="/home/mendel/BadMouth/BadMouth_Gui/mainwindow.py"
sudo chmod 777 "$uart_path"
sudo chmod 777 "$mainwindow_path"
# Run main window
python3 /home/mendel/BadMouth/BadMouth_Gui/mainwindow.py