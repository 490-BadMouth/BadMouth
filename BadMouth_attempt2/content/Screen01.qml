

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import BadMouth_attempt2

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#98a2a4"
    property bool isEqOpen: false
    property bool isVisOpen: false

    Column {
        id: column
        x: 8
        y: 8
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        spacing: 20
        anchors.rightMargin: 670
        anchors.leftMargin: 8
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        width: 120
        height: 464

        Button {
            id: buttonHome
            height: 100
            text: qsTr("Home")
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.verticalCenterOffset: -174
            anchors.leftMargin: 0
            anchors.rightMargin: 2
            font.pointSize: 14
            font.family: "Arial"
            highlighted: false
            flat: false
            transformOrigin: Item.Center

            Connections {
                target: buttonHome
                onClicked: rectangle.isVisOpen = false
            }

            Connections {
                target: buttonHome
                onClicked: rectangle.isEqOpen = false
            }
        }

        Button {
            id: buttonEq
            height: 100
            text: qsTr("Equalizer")
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.verticalCenterOffset: -58
            anchors.leftMargin: 0
            anchors.rightMargin: 2
            font.pointSize: 14
            highlighted: false
            font.family: "Arial"
            transformOrigin: Item.Center
            flat: false

            Connections {
                target: buttonEq
                onClicked: rectangle.isEqOpen = !rectangle.isEqOpen
            }

            Connections {
                target: buttonEq
                onClicked: rectangle.isVisOpen - false
            }
        }

        Button {
            id: buttonStats
            height: 100
            text: qsTr("Stats")
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.verticalCenterOffset: 58
            anchors.leftMargin: 0
            anchors.rightMargin: 2
            font.pointSize: 14
            highlighted: false
            font.family: "Arial"
            transformOrigin: Item.Center
            flat: false
        }

        Button {
            id: buttonAudVis
            height: 100
            text: qsTr("Visualizer")
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.verticalCenterOffset: 174
            anchors.leftMargin: 0
            anchors.rightMargin: 2
            font.pointSize: 14
            highlighted: false
            font.family: "Arial"
            transformOrigin: Item.Center
            flat: false

            Connections {
                target: buttonAudVis
                onClicked: rectangle.isVisOpen = !rectangle.isVisOpen
            }

            Connections {
                target: buttonAudVis
                onClicked: rectangle.isEqOpen = false
            }
        }
    }

    Rectangle {
        id: contentArea
        x: 136
        y: 7
        width: 656
        height: 464
        color: "#26282a"
        radius: 30

        Image {
            id: home_image
            width: 250
            height: 250
            visible: !rectangle.isEqOpen
            anchors.verticalCenter: parent.verticalCenter
            source: "../asset_imports/logooooooooo.png"
            anchors.horizontalCenter: parent.horizontalCenter
        }

        TabBar {
            id: tabBarVis
            width: 624
            height: 400
            visible: rectangle.isVisOpen
            position: TabBar.Header
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            contentHeight: 100
            contentWidth: 50

            TabButton {
                id: tabBars
                height: 40
                text: qsTr("Bar Graph")
                anchors.top: parent.top
                anchors.topMargin: 0
                checked: false
            }

            TabButton {
                id: tabSpec
                height: 40
                text: qsTr("Spectrogram")
                anchors.top: parent.top
                anchors.topMargin: 0
            }
        }

        Row {
            id: row
            x: 16
            y: 32
            width: 624
            height: 400
            visible: rectangle.isEqOpen
            bottomPadding: 0
            topPadding: 0
            spacing: 16

            Slider {
                id: sliderBass
                anchors.verticalCenter: parent.verticalCenter
                scale: 1.5
                rotation: 90
                value: 0.5

                TextArea {
                    id: textBass
                    x: -33
                    y: 6
                    color: "#ffffff"
                    text: "Bass"
                    rotation: 270
                    placeholderTextColor: "#88ffffff"
                    placeholderText: qsTr("Bass")
                }
            }

            Slider {
                id: sliderMid
                anchors.verticalCenter: parent.verticalCenter
                scale: 1.5
                rotation: 90
                value: 0.5

                TextArea {
                    id: textMid
                    placeholderText: qsTr("Text Area")
                }
            }

            Slider {
                id: sliderTreb
                anchors.verticalCenter: parent.verticalCenter
                scale: 1.5
                rotation: 90
                value: 0.5

                TextArea {
                    id: textTreb
                    placeholderText: qsTr("Text Area")
                }
            }
        }
    }

    states: [
        State {
            name: "clicked"
        }
    ]
}
