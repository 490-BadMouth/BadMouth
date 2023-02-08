

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.8
import QtQuick.Controls 2.1
Item{

    id:badMouthGUI
    width:1280
    height:720

    Rectangle {
        id: rectangle
        width: 1280
        height: 720
        visible: true
        color: "#98a2a4"

        Column {
            id: column
            x: 8
            y: 8
            width: 120
            height: 464

            Button {
                id: buttonHome
                height: 100
                text: qsTr("Home")
                font.pointSize: 11
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

                Connections {
                    target: buttonHome
                    onClicked: rectangle.isStatsOpen = false
                }
            }

            Button {
                id: buttonEq
                height: 100
                text: qsTr("Equalizer")
                font.pointSize: 11
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
                    onClicked: rectangle.isVisOpen = false
                }

                Connections {
                    target: buttonEq
                    onClicked: rectangle.isStatsOpen = false
                }
            }

            Button {
                id: buttonStats
                height: 100
                text: qsTr("Stats")
                font.pointSize: 11
                highlighted: false
                font.family: "Arial"
                transformOrigin: Item.Center
                flat: false

                Connections {
                    target: buttonStats
                    onClicked: rectangle.isStatsOpen = !rectangle.isStatsOpen
                }

                Connections {
                    target: buttonStats
                    onClicked: rectangle.isVisOpen = false
                }

                Connections {
                    target: buttonStats
                    onClicked: rectangle.isEqOpen = false
                }
            }

            Button {
                id: buttonAudVis
                height: 100
                text: qsTr("Visualizer")
                font.pointSize: 11
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

                Connections {
                    target: buttonAudVis
                    onClicked: rectangle.isStatsOpen = false
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

            TabBar {
                id: tabBarVis
                width: 624
                height: 400
                visible: rectangle.isVisOpen
                position: TabBar.Header
                contentHeight: 100
                contentWidth: 50

                TabButton {
                    id: tabBars
                    height: 40
                    text: qsTr("Bar Graph")
                    checked: false
                }

                TabButton {
                    id: tabSpec
                    height: 40
                    text: qsTr("Spectrogram")
                }
            }

            Row {
                id: row
                y: 32
                width: 624
                height: 400
                visible: rectangle.isEqOpen
                spacing: 16

                Slider {
                    id: sliderBass
                    layer.textureMirroring: ShaderEffectSource.MirrorVertically
                    scale: 1.5
                    rotation: 90
                    value: 0.5

                    TextArea {
                        id: textBass
                        x: -76
                        y: 1
                        color: "#ffffff"
                        text: "Bass"
                        horizontalAlignment: Text.AlignHCenter
                        rotation: 270
                    }
                }

                Slider {
                    id: sliderMid
                    scale: 1.5
                    rotation: 90
                    value: 0.5

                    TextArea {
                        id: textMid
                        x: -76
                        y: 1
                        color: "#ffffff"
                        text: "Mids"
                        horizontalAlignment: Text.AlignHCenter
                        rotation: 270

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
                        x: -76
                        y: 1
                        color: "#ffffff"
                        text: "Treble"
                        horizontalAlignment: Text.AlignHCenter
                        rotation: 270
                    }
                }
            }
        }

        Rectangle {
            id: stats_rect
            x: 136
            y: 7
            width: 656
            height: 464
            visible: rectangle.isStatsOpen
            color: "#26282a"
            radius: 30

            Text {
                id: text1
                x: 0
                y: 0
                color: "#ffffff"
                text: qsTr("FFT Data")
                font.pixelSize: 35
                horizontalAlignment: Text.AlignHCenter
            }

        }

        Item {
            id: __materialLibrary__
        }



        states: [
            State {
                name: "clicked"
            }
        ]
    }
}
