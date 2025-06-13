# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 568)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPefencies = QAction(MainWindow)
        self.actionPefencies.setObjectName(u"actionPefencies")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.doSystem = QAction(MainWindow)
        self.doSystem.setObjectName(u"doSystem")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        palette = QPalette()
        self.tabWidget.setPalette(palette)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 1px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background: rgb(90,90,90);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(100,100,100);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"min-width: 32ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: rgb(20,20,20);\n"
"border-color: rgb(255,125,0);\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: rgb(255,125,0);\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 1px; /* make non-selected tabs look smaller */\n"
"}\n"
"QSplitter::handle{\n"
"background-color:rgb(10,10,10);\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 22))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"background-color: black;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"color : white;\n"
"spacing: 3px;\n"
"margin-top:2px;\n"
"margin-left:2px;\n"
"padding: 1px 10px;\n"
"background: transparent;\n"
"border:1px solid rgb(50,50,50);\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"border:1px solid rgb(255,125,0);\n"
"}\n"
"\n"
"QMenu {\n"
"background-color: black;\n"
"}\n"
"\n"
"QMenu::item {\n"
"color : white;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"background-color:rgb(40,40,40);\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSetting.addAction(self.actionPefencies)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuWindow.addAction(self.doSystem)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New..", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As ..", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPefencies.setText(QCoreApplication.translate("MainWindow", u"Preferences..", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.doSystem.setText(QCoreApplication.translate("MainWindow", u"Undo/Redo System", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

