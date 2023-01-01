from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import home
import red

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def mainUi():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_red.clicked.connect(red_UI)
    MainWindow.show()

def red_UI():
    global ui
    ui = red.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back.clicked.connect(mainUi)
    MainWindow.show()



mainUi()
sys.exit(app.exec_())