#!/bin/bash
cd $(dirname $0)
pyuic5 ui_Connection.ui -o  	ui_Connection.py
pyuic5 ui_LoadSettings.ui -o 	ui_LoadSettings.py
exit 0