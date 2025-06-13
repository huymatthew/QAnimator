from PyQt5 import QtWidgets,uic,QtCore
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QDockWidget, QFrame, QHBoxLayout, QMenuBar, QSplitter, QWidget
from PyQt5.QtCore import Qt
import PyQt5
import sys
from QHWidgets.QProject.project import QProject
from QHWidgets.QTimeline.qtimeline import QTimeLine
from QHWidgets.QAnimationPlayer.qanimationplayer import QAnimationPlayer
from QHWidgets.QUndoSystem.qundosystem import QUndoSystem,QUndoSystemItem

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/tab.ui",self)
        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(10,10,10))
        self.setPalette(self.pal)
        #self.setStyleSheet("QFrame{border:1px;}")
        self.setMinimumSize(1000,600)

        #self.setLayout(QHBoxLayout(self))
        self.addTab()
        
        self.undoWindow = QDockWidget("Undo System",self)
        self.undoWindow.setFloating(True)
        self.undoWindow.hide()
        self.undoWindow.setWidget(self.tabWidget.currentWidget().undoSystem)

        self.tabWidget.currentChanged.connect(lambda x:self.undoWindow.setWidget(self.tabWidget.currentWidget().undoSystem))

        self.actionNew.triggered.connect(self.newTabAction)
        self.doSystem.triggered.connect(lambda : self.undoWindow.setHidden(not self.undoWindow.isHidden()))

    def newTabAction(self):
        self.addTab()

    def addTab(self,title="Untited*"):
        try:
            newTab = QWidget()
            newTab.setLayout(QHBoxLayout())

            newTab.project = QProject("QHWidgets")
            newTab.timeline = QTimeLine()
            newTab.player = QAnimationPlayer(newTab)
            newTab.mainSplitter = QSplitter(Qt.Horizontal,newTab)
            newTab.editorSplitter = QSplitter(Qt.Vertical,newTab)

            newTab.editorSplitter.addWidget(newTab.player)
            newTab.editorSplitter.addWidget(newTab.timeline)
            newTab.editorSplitter.setPalette(self.pal)

            newTab.mainSplitter.addWidget(newTab.project)
            newTab.mainSplitter.addWidget(newTab.editorSplitter)

            newTab.mainSplitter.setSizes([200,500])

            #undoSystem
            
            newTab.undoSystem = QUndoSystem(newTab)
            

            newTab.layout().addWidget(newTab.mainSplitter)
            newTab.player.load("QHWidgets/QAnimationPlayer/A.png",32,32)

            newTab.player.onTimeUpdate.connect(newTab.timeline.movePointer)
            newTab.timeline.timeChanged.connect(newTab.player.setTime)

            self.tabWidget.setCurrentIndex(self.tabWidget.addTab(newTab,title))

            newTab.timeline.onAddKeys.connect(
                lambda keys: newTab.undoSystem.add(QUndoSystemItem(
                    newTab.timeline._removeKeys,
                    newTab.timeline._addKeys,
                    keys,
                    "QTimeline.addKey"
                )))
        except Exception as e:print(e)
        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()