from PyQt5 import QtWidgets,uic,QtCore
import PyQt5
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui\main.ui",self)

if __name__ == '__main__a':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()