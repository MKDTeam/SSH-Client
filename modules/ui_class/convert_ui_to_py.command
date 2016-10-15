#!/bin/bash
cd $(dirname $0)
pyuic5 ui_Desktop.ui -o 		ui_Desktop.py
pyuic5 ui_Connection.ui -o  	ui_Connection.py
pyuic5 ui_FileTree.ui -o  		ui_FileTree.py
pyuic5 ui_LoadSettings.ui -o 	ui_LoadSettings.py
exit 0