from PyQt5 import QtCore, QtWidgets,Qt, QtGui
from PyQt5.QtGui import QColor, QKeySequence, QPalette
from PyQt5.QtWidgets import QAbstractScrollArea, QApplication, QDirModel, QFileSystemModel, QHBoxLayout, QHeaderView, QListWidget, QListWidgetItem, QScrollArea, QScrollBar, QShortcut, QSplitter, QTabWidget, QTreeView, QTreeWidget, QVBoxLayout, QWidget
import typing
import sys

class QUndoSystem(QWidget):
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent=parent)
        self.setLayout(QVBoxLayout(self))

        self.undoWidget = QListWidget()
        self.redoWidget = QListWidget()
        self.undoItems = []
        self.redoItems = []
        self.tabWidget = QTabWidget(self)
        self.tabWidget.addTab(self.undoWidget,"Undo")
        self.tabWidget.addTab(self.redoWidget,"Redo")

        self.undoShortcut = QShortcut(QKeySequence("Ctrl+Z"),controller)
        self.undoShortcut.activated.connect(self.undo)
        self.redoShortcut = QShortcut(QKeySequence("Ctrl+Y"),controller)
        self.redoShortcut.activated.connect(self.redo)

        self.layout().addWidget(self.tabWidget)
        self.reload()

    def add(self,item):
        self.undoItems = [item] + self.undoItems
        self.redoItems.clear()
        self.reload()
        print("true")

    def undo(self):
        if len(self.undoItems):
            item = self.undoItems[0]
            item.undo()
            self.undoItems.remove(item)
            self.redoItems = [item] + self.redoItems
            self.reload()
    def redo(self):
        if len(self.redoItems):
            item = self.redoItems[0]
            item.redo()
            self.redoItems.remove(item)
            self.undoItems = [item] + self.undoItems
            self.reload()
    def reload(self):
        self.undoWidget.clear()
        self.redoWidget.clear()
        self.undoWidget.addItems([i.name for i in self.undoItems])
        self.redoWidget.addItems([i.name for i in self.redoItems])
    
class QUndoSystemItem():
    def __init__(self, undoAction, redoAction, argv, name) -> None:
        self.undoAction = undoAction
        self.redoAction = redoAction
        self.argv = argv
        self.name = name

    def undo(self):
        self.undoAction(self.argv)

    def redo(self):
        self.redoAction(self.argv)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QUndoSystem()
    window.show()
    sys.exit(app.exec_())