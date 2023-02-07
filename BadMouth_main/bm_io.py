#import libraries
import sys
import os
from PySide2.QtCore import *

class Setting(QObject):

    def top_test(self):
        input("This is a test, enter a any key to exit. ")
        print("Exiting...")
        sys.exit()