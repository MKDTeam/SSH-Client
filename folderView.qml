import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import Qt.labs.folderlistmodel 2.1

Item {
    property var data_model
    property var workspace
    property var function_move

	ToolBar {
	    id: toolbar
	    height: 30
	    z: 2
	    anchors.right: parent.right
	    anchors.left: parent.left
	    anchors.top: parent.top

	    RowLayout {
	        anchors.leftMargin: spacing
	        anchors.fill: parent
	        spacing: 8

            Repeater {
                id: repeater1
	            model: [{//"source": "images/to_parentDirectory.png",
	                    //"description": qsTr("Перейти на уровень выше."),
	                    //"click": "go_to_parent"
	                    //}, {
	                    "source": "images/arrow_back.png",
	                    "description": qsTr("Отменить переход."),
	                    "click": "go_back"
                    }]

                Image {
	                fillMode: Image.PreserveAspectFit
	                sourceSize.height: toolbar.height - 8
	                source: modelData["source"]

	                Rectangle {
	                    anchors.fill: parent
	                    color: "#00000000"
	                    border.color: "black"
	                    opacity: 0

	                    MouseArea {
	                        anchors.fill: parent

	                        onClicked: {
	                            if (modelData["click"] == "go_to_parent") {
                                    //data_model.open_folder_relatively("/..")
	                            }
	                            if (modelData["click"] == "go_back") {
	                                data_model.go_back()
	                            }
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

	        TextEdit {
	            height: toolbar.height - parent.spacing * 2
	            Layout.fillWidth: true
	            font.pixelSize: 12
	            text: data_model.folder
	            clip: true
	            selectByMouse: true
	            readOnly: true
	        }
	    }
	}

	DropArea {
		id: globalDropArea

		anchors.topMargin: 3
	    anchors.top: toolbar.bottom
	    anchors.right: parent.right
	    anchors.bottom: parent.bottom
	    anchors.left: parent.left
	    state: "NORMAL"

	    Rectangle {
            anchors.fill: parent
	    	id: globalHighlight
	    	color: "#adadad"
	    	opacity: 0
	    }

        onEntered: {
            globalDropArea.state = "HIGHLIGHT"
        }

        onExited: {
            globalDropArea.state = "NORMAL"
        }

        states: [
        	State {
        		name: "HIGHLIGHT"
        		PropertyChanges {
        			target: globalDropArea
        			onDropped: {
        				function_move(drag.source.path, data_model.folder)
			            //console.log("Copy '" + drag.source.path + "' to '" + data_model.folder + "")
			        }
        		}
        		PropertyChanges {
        			target: globalHighlight
        			opacity: 0.3
        		}
        	},
        	State {
        		name: "NORMAL"
        		PropertyChanges {
        			target: globalDropArea
					onDropped: {}
        		}
        		PropertyChanges {
        			target: globalHighlight
        			opacity: 0
        		}
        	}
        ]

	    GridView {
	        id: gridView
	        cellWidth: 100
	        cellHeight: 110
	        contentWidth: cellWidth
	        contentHeight: cellHeight
        	anchors.fill: parent
        	anchors.topMargin: 3
		    clip: true

	        model: data_model
	        delegate: Rectangle {

		        Image {
		        	id: item_image
		        	x: (gridView.cellWidth - width) / 2
	                anchors.top: parent.top
	                anchors.topMargin: 3
	                height: 50
		            smooth: true
		            antialiasing: true
		            mipmap: false
		            fillMode: Image.PreserveAspectFit
		            source: {
		                if (fileIsDir && fileSize > 100) {
		                    return "images/folder_filled.png"
		                } else if (fileIsDir && fileSize <= 100){
		                    return "images/folder.png"
		                } else {
		                    return "images/file.png"
		                }
		            }

		            Rectangle {
	                    id: highlight
	                    visible: model.index == gridView.currentIndex
	                    color: "#00000000"
	                    border.color: "#555555"
	                    width: parent.width + 4
	                    height: parent.height + 4
	                    x: -2
	                    y: -2
	            	}

	            	Image {
	            		id: ghost
	            		source: item_image.source
	            		height: item_image.height.toString()
	            		width: item_image.width.toString()
	            		opacity: 0.5
	            		visible: false

	            		property var path: fileURL

	            		function stop_drag() {
	            			Drag.drop()
	            			globalDropArea.state = "NORMAL"
	                        ghost.x = 0
	                        ghost.y = 0
	            		}

	            		Drag.active: dragArea.drag.active
	            		Drag.dragType: Qt.MoveAction
	        			Drag.hotSpot.x: Drag.active ? Drag.hotSpot.x: dragArea.mouseX
	       				Drag.hotSpot.y: Drag.active ? Drag.hotSpot.y: dragArea.mouseY
	       				Drag.onDragStarted: {
	       					console.log("Start")
	       				}

	       				states: [
		       				State {
		                        when: ghost.Drag.active
		                        ParentChange {
		                            target: ghost
		                            parent: workspace
		                        }

		                        AnchorChanges {
		                            target: ghost
		                            anchors.horizontalCenter: undefined
		                            anchors.verticalCenter: undefined
		                        }

		                        PropertyChanges {
		                        	target: ghost
		                        	visible: true
		                        }
		                    }
	                    ]
	            	}

	            	DropArea {
	            		id: dropArea
				        anchors.fill: parent

	                    onEntered: {
	                        gridView.currentIndex = model.index
                            globalDropArea.state = "NORMAL"
	                    }

	                    onExited: {
	                        gridView.currentIndex = -1
                            globalDropArea.state = "HIGHLIGHT"
	                    }

                        onDropped: {
                        	function_move(drag.source.path, fileURL)
	                        //console.log("Drop '" + drag.source.path + "' to '" + filePath + "'")
	                    }
				    }

		            MouseArea {
		            	id: dragArea
		                anchors.fill: parent
		                drag.target: ghost

	                    onDoubleClicked: {
		                    data_model.open_folder(fileURL)
		                }

	                    onClicked: {
	                        gridView.currentIndex = model.index
	                        gridView.focus = true
	                    }

	                   
	                    onEntered: {
	                    	//globalDropArea.state = "NORMAL"
	                    }

	                    onExited: {
	                    	//globalDropArea.state = "HIGHLIGHT"
	                    }
	                    

	                    onReleased: {
	                        ghost.stop_drag()
	                    }

		                hoverEnabled: true

		                ToolTip {
		                    visible: parent.containsMouse 
		                    text: {
		                        var name = fileName + '\n' + qsTr("Размер файла: ")
		                        var size = parseInt(fileSize, 10)
		                        if (size > 1024 * 1024 * 1024) return (name + Math.round(size / (1024 * 1024 * 1024)).toString() + ' GB')
		                        if (size > 1024 * 1024)        return (name + Math.round(size / (1024 * 1024)).toString() + ' MB')
		                        if (size > 1024)               return (name + Math.round(size / (1024)).toString() + ' KB')
		                        return (name + size.toString() + ' B')
		                    }
		                }
		            }

		            Text {
	                    x: 4 - (gridView.cellWidth - parent.width) / 2
		                anchors.top: parent.bottom
		                width: gridView.cellWidth - 8
		                height: gridView.cellHeight - parent.height - 8                                
	                    text: fileName
	                    horizontalAlignment: Text.AlignHCenter
		                clip: true
		                wrapMode: Text.WrapAtWordBoundaryOrAnywhere
		            }
		        }
		    }
		}	
	} 
}
