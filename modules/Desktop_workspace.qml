import QtQuick 2.7
//import QtQuick.Controls 1.5
//import QtQuick.Layouts 1.3
Rectangle {
    id: workspace
    color: "#ececec"
    width: 800; height: 600

    signal run_terminal()
    signal run_file_manager()

    function resize_workspace(width, height) {
        workspace.width = width
        workspace.height = height
    }


    function select_element(element) {
        terminal.border.color = "#00000000"
        file_tree.border.color = "#00000000"
        help.border.color = "#00000000"
        element.border.color = "#adadadff"
    }

    Grid {
        id: grid
        anchors.rightMargin: 15
        anchors.leftMargin: 15
        anchors.bottomMargin: 15
        anchors.topMargin: 15
        spacing: 20
        anchors.fill: parent

        Rectangle {
            id: terminal
            width: 90
            height: 115
            color: "#00000000"
            border.color: "#00000000"


            Image {
                id: terminal_image
                x: 0
                y: 0
                height: 80
                clip: true
                antialiasing: true
                anchors.rightMargin: 5
                anchors.leftMargin: 5
                anchors.topMargin: 5
                anchors.right: parent.right
                anchors.left: parent.left
                anchors.top: parent.top
                source: "images/terminal.png"
                mipmap: true
            }


            Text {
                id: terminal_text
                x: 0
                y: 80
                text: qsTr("Терминал")
                anchors.top: terminal_image.bottom
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.left: parent.left
                anchors.topMargin: 0
                verticalAlignment: Text.AlignTop
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                textFormat: Text.AutoText
                font.pixelSize: 12
            }


            MouseArea {
                id: terminal_mouseArea
                anchors.fill: parent

                onClicked: {
                    select_element(terminal)
                    show_status('Терминал, используется для отправки текстовых команд на сервер')
                }

                onDoubleClicked: {
                    show_status('Запуск терминала')
                    start_application('terminal')
                }
            }
        }

        Rectangle {
            id: file_tree
            width: 90
            height: 115
            color: "#00000000"

            Image {
                id: file_tree_image
                x: -100
                y: 0
                width: 80
                height: 80
                clip: true
                antialiasing: true
                anchors.topMargin: 5
                source: "images/file_tree.png"
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 5
                anchors.leftMargin: 5
                anchors.left: parent.left
                mipmap: true
            }

            Text {
                id: file_tree_text
                x: -100
                y: 100
                text: qsTr("Файловый менеджер")
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.leftMargin: 0
                verticalAlignment: Text.AlignTop
                anchors.topMargin: 0
                anchors.bottom: parent.bottom
                wrapMode: Text.WordWrap
                anchors.right: parent.right
                anchors.top: file_tree_image.bottom
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 12
                anchors.left: parent.left
                textFormat: Text.AutoText
            }

            MouseArea {
                id: file_tree_mouseArea
                anchors.fill: parent

                onClicked: {
                    select_element(file_tree)
                    show_status('Файловый менеджер, используется для работы с файлами на сервере')
                }

                onDoubleClicked: {
                    show_status('Запуск файлового менеджера')
                    start_application('file_manager')
                }
            }
            border.color: "#00000000"
        }

        Rectangle {
            id: help
            width: 90
            height: 115
            color: "#00000000"
            border.color: "#00000000"
            Image {
                id: help_image
                x: 0
                y: 0
                height: 80
                clip: true
                antialiasing: true
                anchors.rightMargin: 5
                anchors.leftMargin: 5
                anchors.topMargin: 5
                anchors.left: parent.left
                anchors.top: parent.top
                source: "images/help.png"
                anchors.right: parent.right
                mipmap: true
            }

            Text {
                id: help_text
                x: 0
                y: 80
                text: qsTr("Справка")
                anchors.left: parent.left
                verticalAlignment: Text.AlignTop
                anchors.top: help_image.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                wrapMode: Text.WordWrap
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                anchors.right: parent.right
                textFormat: Text.AutoText
            }

            MouseArea {
                id: help_mouseArea
                anchors.fill: parent

                onClicked: {
                    select_element(help)
                    show_status('Справка по возможностям и функциям программы')
                }

                onDoubleClicked: {
                    show_status('Запуск справки')
                    start_application('help')
                }
            }
        }
    }
}
