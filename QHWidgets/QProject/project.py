from PyQt5 import QtCore, QtWidgets,Qt, QtGui
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QAbstractScrollArea, QApplication, QDirModel, QFileSystemModel, QHBoxLayout, QHeaderView, QListWidget, QScrollArea, QScrollBar, QSplitter, QTreeView, QTreeWidget, QWidget
import typing
import sys



class QProject(QWidget):
    def __init__(self,path,parent=None) -> None:
        super().__init__(parent=parent)

        self.setWindowTitle("Projector")
        self.setGeometry(900,200,400,800)
        self.mainPath = path
        self.submain = None

        self.setLayout(QHBoxLayout())

        self.mainWidget = QTreeView()
        self.folderWidget = QTreeView()
        
        self.dirm = QDirModel()
        self.dirm.setFilter(QtCore.QDir.Filter.Dirs|QtCore.QDir.Filter.NoDotAndDotDot)

        #self.dirm.setRootPath(QtCore.QDir.rootPath())

        self.mainWidget.setModel(self.dirm)
        self.mainWidget.setRootIndex(self.dirm.index(path))
        self.mainWidget.setColumnHidden(1,True)
        self.mainWidget.setColumnHidden(2,True)
        self.mainWidget.setColumnHidden(3,True)
        #self.mainWidget.setHeaderHidden(True)
        self.mainWidget.setColumnWidth(0,400)
        self.mainWidget.setExpandsOnDoubleClick(True)
        self.mainWidget.expandAll()
        self.mainWidget.doubleClicked.connect(self.t)
        self.mainWidget.setAcceptDrops(True)

        self.splitter = QSplitter()
        self.splitter.addWidget(self.mainWidget)
        self.splitter.addWidget(self.folderWidget)
        self.splitter.setSizes([200,200])

        self.layout().addWidget(self.splitter)
        self.folderWidget.setDragEnabled(True)

        self.setStyleSheet("QWidget{background-color:rgb(30,30,30);color:rgb(230,230,230)}QHeaderView{color:black}")

    def reload(self):
        self.fim = QDirModel()
        self.fim.setFilter(QtCore.QDir.Filter.Files|QtCore.QDir.Filter.NoDotAndDotDot)
        try:
            self.fim.setNameFilters(["*.jpg","*.png"])
        except Exception as e:print(e)

        self.folderWidget.setModel(self.fim)
        self.folderWidget.setRootIndex(self.fim.index(self.submain))
        self.folderWidget.setColumnHidden(1,True)
        self.folderWidget.setColumnHidden(2,True)
        self.folderWidget.setColumnHidden(3,True)
        self.folderWidget.setColumnWidth(0,400)
        self.folderWidget.setExpandsOnDoubleClick(True)
        self.folderWidget.expandAll()
        self.folderWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    def t(self,a:QtCore.QModelIndex):
        self.submain = self.dirm.filePath(a)
        self.reload()
    def dragEnterEvent(self, e):
        print(e)
		
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
			
    def dropEvent(self, e):
        print(e.mimeData().text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = QProject("C:/Users/NHATMINH/Desktop")
    wid.show()
    sys.exit(app.exec_())