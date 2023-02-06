

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15
import BadMouthGUI_qt5 1.0

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#5a5a5a"

    Column {
        id: column
        x: 8
        y: 8
        width: 152
        height: 464
        spacing: 20

        Button {
            id: button_Home
            width: 152
            height: 100
            text: qsTr("Home")
        }

        Button {
            id: button_Eq
            width: 152
            height: 100
            text: qsTr("Equalizer")
        }

        Button {
            id: button_Vis
            width: 152
            height: 100
            text: qsTr("Visualizer")
        }

        Button {
            id: button_Stats
            width: 152
            height: 100
            text: qsTr("Stats")
        }
    }

    Rectangle {
        id: content
        x: 166
        y: 8
        width: 626
        height: 464
        color: "#26282a"
        radius: 30

        Image {
            id: image
            x: 188
            y: 107
            width: 250
            height: 250
            source: "../asset_imports/logooooooooo.png"
            fillMode: Image.PreserveAspectFit
        }
    }
}
