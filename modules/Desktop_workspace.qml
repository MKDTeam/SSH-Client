import QtQuick 1.1
Rectangle {
    id: workspace
    color: "#eae0c8"
    width: 800; height: 600

    signal run_terminal()
    signal run_file_manager()

    function resize_workspace(width, height) {
        workspace.width = width
        workspace.height = height
    }

    Grid {
        id: grid
        anchors.rightMargin: 15
        anchors.leftMargin: 15
        anchors.bottomMargin: 15
        anchors.topMargin: 15
        spacing: 30
        anchors.fill: parent



        Rectangle {
            id: terminal
            width: 80
            height: 110
            color: "#00000000"
            border.color: "#00000000"

            Text {
                id: terminal_text
                x: -100
                y: 100
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

            Image {
                id: terminal_image
                x: -100
                y: 0
                height: 80
                anchors.right: parent.right
                anchors.rightMargin: 0
                anchors.left: parent.left
                anchors.leftMargin: 0
                anchors.top: parent.top
                anchors.topMargin: 0
                source: "images/terminal.png"
            }

            MouseArea {
                id: terminal_mouseArea
                anchors.fill: parent

                onClicked: {
                    show_status('Терминал, используется для отправки текстовых команд на сервер')
                }

                onDoubleClicked: {
                    show_status('Запуск терминала')
                    run_terminal()
                }
            }

        }

        Rectangle {
            id: file_tree
            width: 80
            height: 110
            color: "#00000000"
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

            Image {
                id: file_tree_image
                x: -100
                y: 0
                width: 80
                height: 80
                anchors.topMargin: 0
                source: "images/file_tree.png"
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.left: parent.left
            }

            MouseArea {
                id: file_tree_mouseArea
                anchors.fill: parent

                onClicked: {
                    show_status('Файловый менеджер, используется для работы с файлами на сервере')
                }

                onDoubleClicked: {
                    show_status('Запуск файлового менеджера')
                    run_file_manager()
                }
            }
            border.color: "#00000000"
        }
    }
}
