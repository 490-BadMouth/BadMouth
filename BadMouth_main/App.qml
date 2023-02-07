// import library
import QtQuick.Controls 2.15



ApplicationWindow {

    id: Application
    width: 800
    height: 480
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