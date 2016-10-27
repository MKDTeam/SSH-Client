import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import Qt.labs.folderlistmodel 2.1

ApplicationWindow {
    id: desktop
    width: 1100
    height: 800
    visible: false

    function show() {
    	desktop.visible = true
    }

    function function_move(from_path, to_path) {
        move(from_path, to_path)
    }

    function remoteHost_showFolder(list, path) {
        var model = remoteHost_model
        model.folder = path
        if (path == '/') path = ''

        remoteHost_model.clear()
        for (var i = 0; i < list.length; i++) {
            var raw_data = list[i]
            var data = {"mode":         raw_data[0],
                        "fileIsDir" :   false,
                        "fileIsLink" :  false,
                        "fileSize":     parseInt(raw_data[1], 10),
                        "fileName":     raw_data[2],
                        "fileURL":      path + '/' + raw_data[2],
                        "filePath":     path + '/' + raw_data[2]}
            if (data["mode"][0] == '1' || data["mode"][0] == '4') data["fileIsDir"] = true

            if (data["fileIsDir"]) remoteHost_model.insert(0, data)
            else remoteHost_model.append(data)
            //console.log(data["fileName"], ": ", data["mode"])           
        }
    }

    signal new_console_message(string text)

    Page {
        anchors.fill: parent
        header: Item {
            id: header
            height: 80
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.top: parent.top

            ToolBar {
                id: main_menu
                anchors.right: parent.right
                anchors.left: parent.left
                anchors.top: parent.top
                height: 30
                RowLayout {
                    spacing: 5
                    anchors.fill: parent
                    ToolButton {
                        text: "Меню"
                        Layout.alignment: Qt.AlignHCenter | Qt.AlignBaseline
                        Layout.maximumHeight: 25
                        onClicked: menu1.open()

                        Menu {
                            id: menu1
                            y: parent.height

                            MenuItem { text: "Новое соединение" }
                            MenuItem { text: "Настройки" }
                            MenuItem { text: "Выход" }
                        }
                    }
                    ToolButton {
                        text: "Правка"
                        Layout.alignment: Qt.AlignHCenter | Qt.AlignBaseline
                        Layout.maximumHeight: 25
                        onClicked: menu2.open()

                        Menu {
                            id: menu2
                            y: parent.height

                            MenuItem { text: "Скопировать файл" }
                            MenuItem { text: "Удалить файл" }
                            MenuItem { text: "Выгрузить файл с сервера" }
                            MenuItem { text: "Загрузить файл на сервер" }
                        }
                    }
                    ToolButton {
                        text: "Справка"
                        Layout.maximumHeight: 25
                        Layout.alignment: Qt.AlignHCenter | Qt.AlignBaseline
                    }
                    Item { Layout.fillWidth: true }
                }
            }

            ToolBar {
                id: toolbar
                anchors.right: parent.right
                anchors.left: parent.left
                anchors.top: main_menu.bottom
                height: 50
                RowLayout {
                    anchors.leftMargin: 10
                    anchors.fill: parent
                    spacing: 8

                    Repeater {
                        model: [{"source": "images/file_delete.png",
                                "description": qsTr("Удалить файл."),
                                "click": "delete"
                                }, {
                                "source": "images/file_download.png",
                                "description": qsTr("Выгрузить файл c сервера."),
                                "click": "download"
                                }, {
                                "source": "images/file_upload.png",
                                "description": qsTr("Загрузить файл на сервер."),
                                "click": "upload"
                                }, {
                                "source": "images/file_copy.png",
                                "description": qsTr("Создать копию файла в текущей папке."),
                                "click": "copy"                                    
                                }]

                        Image {
                            fillMode: Image.PreserveAspectFit
                            sourceSize.height: toolbar.height - 16
                            source: modelData["source"]

                            Rectangle {
                                anchors.fill: parent
                                color: "#00000000"
                                border.color: "black"
                                opacity: 0

                                MouseArea {
                                    anchors.fill: parent

                                    onClicked: {
                                    }

                                    onEntered: {
                                        parent.opacity = 0.2
                                    }

                                    onExited: {
                                        parent.opacity = 0
                                    }

                                    hoverEnabled: true

                                    ToolTip {
                                        delay: 1000
                                        timeout: 5000
                                        visible: parent.containsMouse 
                                        text: modelData["description"]
                                    }
                                }
                            }
                        } 
                    }
                    Item { Layout.fillWidth: true }
                }
            }
        }

        data: Item {
            id: workspace
            anchors.top: header.bottom
            anchors.right: parent.right
            anchors.bottom: footer.top
            anchors.left: parent.left

            GroupBox {
                id: remoteHost
                anchors.bottomMargin: 2
                anchors.leftMargin: 2
                anchors.rightMargin: 1
                anchors.right: parent.horizontalCenter
                anchors.top: parent.top
                anchors.bottom: remoteConsole_control.top
                anchors.left: parent.left
                title: qsTr("Файлы на удаленной машине")

                ListModel {
                    id: remoteHost_model

                    property var folder

                    Component.onCompleted: function (){
                        remoteHost_model.folder = '/'
                    }

                    function go_back() {
                        var url = remoteHost_model.folder
                        if (url.toString() == '/') {
                            return
                        }
                        var mass = url.toString().split('/')
                        mass.pop()
                        mass.shift()
                        remoteHost_model.folder = '/' + mass.join('/')

                        open_folder(remoteHost_model.folder)
                    }

                    function open_folder(url) {
                        //console.log("|", url, "|")
                        show_dir_list(url)
                        //console.log(remoteHost_model.folder)
                    }
                }

                Loader {
                    anchors.topMargin: 3
                    anchors.bottomMargin: 3
                    anchors.rightMargin: 3
                    anchors.leftMargin: 3
                    anchors.fill: parent
                    visible: status == Loader.Ready

                    Component.onCompleted: function (){
                        setSource("folderView.qml", { "data_model": remoteHost_model,
                                                      "workspace": workspace,
                                                      "function_move": desktop.function_move});
                    }
                }

            }

            GroupBox {
                id: localMachine
                anchors.bottomMargin: 2
                anchors.rightMargin: 2
                anchors.leftMargin: 1
                anchors.left: parent.horizontalCenter
                anchors.right: parent.right
                anchors.bottom: remoteConsole_control.top
                anchors.top: parent.top
                title: qsTr("Файлы на локальной машине")

                FolderListModel {
                    id: localMachine_model
                    //folder: Qt.resolvedUrl("file:///..")
                    //showDotAndDotDot: true
                    showHidden: true
                    showDirs: true
                    showDirsFirst: true
                    showFiles: true
                    sortReversed: true
                    nameFilters: ["*"]

                    Component.onCompleted: function (){
                        localMachine_model.folder = "file:///"
                    }

                    function go_back() {
                        var url = localMachine_model.folder
                        if (url.toString() == "file:///") {
                            return
                        }
                        var mass = url.toString().split('/')
                        mass.pop()
                        mass.shift()
                        mass.shift()
                        mass.shift()
                        localMachine_model.folder = "file:///" + mass.join('/')

                    }

                    function open_folder(url) {
                        //console.log("|", url, "|")
                        localMachine_model.folder = url
                        //console.log(localMachine_model.folder)
                    }
                }

                Loader {
                    anchors.rightMargin: 3
                    anchors.leftMargin: 3
                    anchors.bottomMargin: 3
                    anchors.topMargin: 3
                    anchors.fill: parent
                    visible: status == Loader.Ready

                    Component.onCompleted: function (){
                        setSource("folderView.qml", { "data_model": localMachine_model,
                                                      "workspace": workspace,
                                                      "function_move": desktop.function_move});
                    }
                }
            }

            GroupBox {
                id: remoteConsole_control
                height: 200
                anchors.rightMargin: 2
                anchors.leftMargin: 2
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.left: parent.left

                ListView {
                    id: remoteConsole
                    anchors.top: parent.top
                    clip: true
                    anchors.right: parent.right
                    anchors.left: parent.left
                    anchors.bottom: remoteConsole_input.top
                    highlightFollowsCurrentItem: true

                    Component.onCompleted: function() {
                        desktop.new_console_message.connect(remoteConsole.write_text)
                    }

                    function write_text(string) {
                        var model = remoteConsole_model
                        var raw_data = {"text": ""}

                        if (model.count == 0) {
                            model.append(raw_data)
                        }

                        var last_string = model.get(model.count - 1)

                        for (var index in string) {
                            var leter = string[index]
                            if (leter == '\n') {
                                model.append(raw_data)
                                //console.log(last_string.text)
                                last_string = model.get(model.count - 1)
                            } else {
                                last_string.text = last_string.text + leter
                            }
                        }
                        remoteConsole.currentIndex = model.count - 1
                    }

                    model: ListModel {
                        id: remoteConsole_model
                    }

                    delegate: Text {
                        width: remoteConsole.width
                        wrapMode: Text.Wrap
                        
                        text: model.text
                    }
                }
                TextField {
                    id: remoteConsole_input
                    height: 25
                    anchors.rightMargin: -1
                    anchors.leftMargin: -1
                    anchors.bottomMargin: -1
                    leftPadding: 16
                    bottomPadding: 2
                    topPadding: 2
                    anchors.bottom: parent.bottom
                    anchors.right: parent.right
                    anchors.left: parent.left

                    selectByMouse: true

                    onAccepted: {
                        send_command(text)
                        clear()
                    }

                    Text {
                        text: " >"
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                    }

                    Button {
                        id: button1
                        width: 30
                        height: 15
                        anchors.rightMargin: 8
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right

                        Text {
                            text: "stop"
                            anchors.fill: parent
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            font.pixelSize: 10
                        }

                        onClicked: {
                            send_command(String.fromCharCode(3))
                        }
                    }
                }
            }
        }

        footer: RowLayout {
            id: footer
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.bottom: parent.bottom
            height: 20
            Label { text: "" }
        }
    }
}
