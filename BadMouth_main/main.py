# import libraries
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from bm_io import Setting

# launch app
if __name__ == '__main__':
    app = QApplication([])
    engine = QQmlApplicationEngine()
    # location of the fullscreen app that was created
    url = QUrl("./App.qml")
    context = engine.rootContext()
    setting = Setting()
    context.setContextProperty("_Setting", setting)
    engine.load(url)
    app.exec_()
