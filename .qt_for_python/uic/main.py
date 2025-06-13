# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AnimtionPlayer(object):
    def setupUi(self, AnimtionPlayer):
        if not AnimtionPlayer.objectName():
            AnimtionPlayer.setObjectName(u"AnimtionPlayer")
        AnimtionPlayer.resize(1128, 581)
        AnimtionPlayer.setStyleSheet(u"")
        self.controller = QFrame(AnimtionPlayer)
        self.controller.setObjectName(u"controller")
        self.controller.setGeometry(QRect(0, 530, 1131, 40))
        self.controller.setStyleSheet(u"background-color:rgb(20,20,20);border:1px solid;border-color:rgb(0,0,0)")
        self.controller.setFrameShape(QFrame.Box)
        self.controller.setFrameShadow(QFrame.Plain)
        self.controller.setLineWidth(1)
        self.controller.setMidLineWidth(0)
        self.startBtn = QPushButton(self.controller)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(20, 10, 24, 24))
        icon = QIcon()
        icon.addFile(u"../icon/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startBtn.setIcon(icon)
        self.startBtn.setIconSize(QSize(24, 24))
        self.skipbackBtn = QPushButton(self.controller)
        self.skipbackBtn.setObjectName(u"skipbackBtn")
        self.skipbackBtn.setGeometry(QRect(50, 10, 24, 24))
        icon1 = QIcon()
        icon1.addFile(u"../icon/skipback.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skipbackBtn.setIcon(icon1)
        self.skipbackBtn.setIconSize(QSize(24, 24))
        self.playBtn = QPushButton(self.controller)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setGeometry(QRect(80, 10, 24, 24))
        self.playBtn.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"../icon/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon2)
        self.playBtn.setIconSize(QSize(24, 24))
        self.playBtn.setCheckable(True)
        self.playBtn.setChecked(False)
        self.playBtn.setFlat(False)
        self.skipforwardBtn = QPushButton(self.controller)
        self.skipforwardBtn.setObjectName(u"skipforwardBtn")
        self.skipforwardBtn.setGeometry(QRect(110, 10, 24, 24))
        icon3 = QIcon()
        icon3.addFile(u"../icon/skip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skipforwardBtn.setIcon(icon3)
        self.skipforwardBtn.setIconSize(QSize(24, 24))
        self.endBtn = QPushButton(self.controller)
        self.endBtn.setObjectName(u"endBtn")
        self.endBtn.setGeometry(QRect(140, 10, 24, 24))
        icon4 = QIcon()
        icon4.addFile(u"../icon/end.png", QSize(), QIcon.Normal, QIcon.Off)
        self.endBtn.setIcon(icon4)
        self.endBtn.setIconSize(QSize(24, 24))
        self.player = QLabel(AnimtionPlayer)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(0, 10, 1131, 521))
        self.player.setStyleSheet(u"background-color:rgb(150,150,150);border:1px solid;border-color:rgb(0,0,0)")
        self.player.setAlignment(Qt.AlignCenter)

        self.retranslateUi(AnimtionPlayer)

        self.playBtn.setDefault(False)


        QMetaObject.connectSlotsByName(AnimtionPlayer)
    # setupUi

    def retranslateUi(self, AnimtionPlayer):
        AnimtionPlayer.setWindowTitle(QCoreApplication.translate("AnimtionPlayer", u"Form", None))
        self.startBtn.setText("")
        self.skipbackBtn.setText("")
        self.playBtn.setText("")
        self.skipforwardBtn.setText("")
        self.endBtn.setText("")
        self.player.setText("")
    # retranslateUi

