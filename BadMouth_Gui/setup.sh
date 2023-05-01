#!/bin/bash
export DISPLAY=:0.0

# Display GUI on external LCD
# Give permissions to send/receive UART
uart_path="/dev/ttyS1"
chmod 777 "$uart_path"
# Run main window
python3 mainwindow.py