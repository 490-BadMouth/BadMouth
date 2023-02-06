

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.4
import QtQuick.Controls 6.4
import BadMouthGUI
import QtQuick.Studio.Components 1.0
import QtQuick.Layouts 6.3

Rectangle {
    id: main_Rec
    width: Constants.width
    height: Constants.height
    color: "#241f31"
    property bool isDialogOpen: false
    property bool isDialog2Open: false
    property bool isDialog3Open: false
    z: 0

    states: [
        State {
            name: "clicked"
            when: button_EQ.checked

            PropertyChanges {
                target: button_EQ
                x: 8
                y: 8
                text: qsTr("Equalizer")
            }

            PropertyChanges {
                target: button_Stats
                x: 8
                y: 54
            }


            PropertyChanges {
                target: button_AudView
                x: 8
                y: 100
            }

            PropertyChanges {
                target: rectangle_EQ
                x: 114
                y: 17
                width: 358
                height: 295
            }

            PropertyChanges {
                target: text_Slider_Mid
                x: -36
                text: qsTr("Mid")
                anchors.topMargin: 5
            }

            PropertyChanges {
                target: text_Slider_Treb
                x: -36
                text: qsTr("Treble")
                anchors.topMargin: 5
            }
        },
        State {
            name: "State1"

            PropertyChanges {
                target: text_Slider_Mid
                x: -36
            }

            PropertyChanges {
                target: text_Slider_Treb
                x: -36
            }

            PropertyChanges {
                target: button_EQ
                x: 0
                y: 54
                font.family: "Arial"
                highlighted: true
            }

            PropertyChanges {
                target: button_Stats
                x: 0
                y: 100
                text: qsTr("Statistics")
                font.family: "Arial"
                highlighted: true
            }

            PropertyChanges {
                target: button_AudView
                x: 0
                y: 149
                font.family: "Arial"
                highlighted: true
            }

            PropertyChanges {
                target: button_Home
                y: 8
                text: qsTr("Home")
                font.family: "Arial"
                wheelEnabled: false
                icon.cache: true
                flat: false
                icon.color: "#26282a"
                highlighted: true
            }

            PropertyChanges {
                target: rectangle_EQ
                x: 140
                y: 8
                width: 332
                height: 304
                color: "#26282a"
            }

            PropertyChanges {
                target: column
                x: 8
                y: 8
                width: 117
                height: 304
                spacing: 8
            }

            PropertyChanges {
                target: el_Pato
                source: "../asset_imports/Logo.png"
            }
        }
    ]
    Rectangle {
        id: rectangle_EQ
        x: 140
        y: 25
        width: 332
        height: 287
        visible: main_Rec.isDialogOpen
        color: "#26282a"
        radius: 30
        z: 1
        clip: false

        Grid {
            id: grid
            anchors.fill: parent

            Slider {
                id: slider
                anchors.verticalCenter: parent.verticalCenter
                rotation: 90
                anchors.verticalCenterOffset: 0
                anchors.horizontalCenterOffset: -100
                anchors.horizontalCenter: parent.horizontalCenter
                value: 0.5

                Text {
                    id: text_Slider_Bass
                    x: -36
                    width: 50
                    height: 30
                    color: "#ffffff"
                    text: qsTr("Bass")
                    anchors.top: parent.top
                    font.pixelSize: 15
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.bold: true
                    rotation: 270
                    font.family: "Arial"
                    anchors.topMargin: 5
                }
            }

            Slider {
                id: slider1
                anchors.verticalCenter: parent.verticalCenter
                rotation: 90
                anchors.horizontalCenter: parent.horizontalCenter
                value: 0.5

                Text {
                    id: text_Slider_Mid
                    x: -36
                    y: 235
                    width: 50
                    height: 30
                    color: "#ffffff"
                    text: qsTr("Mid")
                    anchors.top: parent.top
                    font.pixelSize: 15
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.topMargin: 5
                    font.bold: true
                    font.family: "Arial"
                    rotation: 270
                }
            }

            Slider {
                id: slider2
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenterOffset: 100
                rotation: 90
                anchors.horizontalCenter: parent.horizontalCenter
                value: 0.5

                Text {
                    id: text_Slider_Treb
                    x: -38
                    y: 335
                    width: 50
                    height: 30
                    color: "#ffffff"
                    text: qsTr("Treble")
                    anchors.top: parent.top
                    font.pixelSize: 15
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.topMargin: 6
                    font.bold: true
                    font.family: "Arial"
                    rotation: 270
                }
            }
        }
    }

    Rectangle {
        id: rectangle_Stats
        x: 140
        y: 25
        width: 332
        height: 287
        visible: main_Rec.isDialog2Open
        color: "#26282a"
        radius: 30
        z: 1
        clip: false

        ColumnLayout {
            x: 95
            y: 36
            Text {
                id: text1
                color: "#ffffff"
                text: qsTr("Bad Word")
                font.pixelSize: 30
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: 143
                Layout.preferredHeight: 40
            }

            Text {
                id: text2
                color: "#ffffff"
                text: qsTr("Count")
                font.pixelSize: 30
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: 143
                Layout.preferredHeight: 31
            }
        }
    }

    Rectangle {
        id: rectangle_Aud
        x: 140
        y: 25
        width: 332
        height: 287
        visible: main_Rec.isDialog3Open
        color: "#26282a"
        radius: 30
        z: 1
        clip: false

        ColumnLayout {
            x: 95
            y: 36
            Text {
                id: text3
                color: "#ffffff"
                text: qsTr("FFT Data")
                font.pixelSize: 30
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: 143
                Layout.preferredHeight: 40
            }
        }
    }

    Column {
        id: column
        x: 8
        y: 8
        width: 111
        height: 304
        spacing: 8

        Button {
            id: button_Home
            text: qsTr("Home")
            icon.color: "#26282a"
            font.family: "Arial"
            highlighted: true

            Connections {
                target: button_Home
                onClicked: main_Rec.isDialogOpen = false
            }

            Connections {
                target: button_Home
                onClicked: main_Rec.isDialog2Open = false
            }

            Connections {
                target: button_Home
                onClicked: main_Rec.isDialog3Open = false
            }
        }

        Button {
            id: button_EQ
            text: qsTr("EQ")
            icon.color: "#26282a"
            font.family: "Arial"
            highlighted: true

            Connections {
                target: button_EQ
                onClicked: main_Rec.isDialogOpen = !main_Rec.isDialogOpen
            }

            Connections {
                target: button_EQ
                onClicked: main_Rec.isDialog2Open = false
            }

            Connections {
                target: button_EQ
                onClicked: main_Rec.isDialog3Open = false
            }
        }

        Button {
            id: button_Stats
            text: qsTr("Statistics")
            highlighted: true

            Connections {
                target: button_Stats
                onClicked: main_Rec.isDialog2Open = !main_Rec.isDialog2Open
            }

            Connections {
                target: button_Stats
                onClicked: main_Rec.isDialogOpen = false
            }

            Connections {
                target: button_Stats
                onClicked: main_Rec.isDialog3Open = false
            }
        }

        Button {
            id: button_AudView
            text: qsTr("Audio View")
            highlighted: true

            Connections {
                target: button_AudView
                onClicked: main_Rec.isDialog3Open = !main_Rec.isDialog3Open
            }

            Connections {
                target: button_AudView
                onClicked: main_Rec.isDialogOpen = false
            }

            Connections {
                target: button_AudView
                onClicked: main_Rec.isDialog2Open = false
            }
        }
    }

    Image {
        id: el_Pato
        x: 140
        y: 25
        width: 332
        height: 287
        source: "../asset_imports/logooooooooo.png"
        z: 0
        clip: false
        fillMode: Image.PreserveAspectFit
    }

}

/*##^##
Designer {
    D{i:0}D{i:19;locked:true}
}
##^##*/

