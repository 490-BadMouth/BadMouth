# import libraries
import os
import sys
import bm_gui


def main():
    print("It's BadMouthin' Time...")
    #Create QApplication 
    app = bm_gui.QApplication(sys.argv)
    #Spawn window and show
    window = bm_gui.main_window()
    window.show()
    print("Exiting...")
    #Exit QApplication
    sys.exit(app.exec_())


# launch app
if __name__ == '__main__':
 print("Starting...")
 main()