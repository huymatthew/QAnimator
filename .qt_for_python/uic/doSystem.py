# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doSystem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 597)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.undo = QWidget()
        self.undo.setObjectName(u"undo")
        self.verticalLayout_2 = QVBoxLayout(self.undo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.undoListView = QListView(self.undo)
        self.undoListView.setObjectName(u"undoListView")

        self.verticalLayout_2.addWidget(self.undoListView)

        self.tabWidget.addTab(self.undo, "")
        self.redo = QWidget()
        self.redo.setObjectName(u"redo")
        self.verticalLayout_3 = QVBoxLayout(self.redo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.redoListView = QListView(self.redo)
        self.redoListView.setObjectName(u"redoListView")

        self.verticalLayout_3.addWidget(self.redoListView)

        self.tabWidget.addTab(self.redo, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.undo), QCoreApplication.translate("Form", u"Undo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.redo), QCoreApplication.translate("Form", u"Redo", None))
    # retranslateUi

