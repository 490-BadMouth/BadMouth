// import library
import QtQuick.Controls 2



ApplicationWindow {

    id: application
    width: 1280
    height: 720
    visible: true
    visibility: "FullScreen"

    //initialize first window of Application
    property var iniITEM: "Screen01_v215.qml"

    // stack-based navigation model
    StackView {
        id: stackview
        initialItem: iniITEM
    }

}