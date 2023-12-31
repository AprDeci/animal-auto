# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setup(object):
    def setupUi(self, setup):
        setup.setObjectName("setup")
        setup.resize(444, 450)
        setup.setStyleSheet("#setup{\n"
"    background-color: qlineargradient(spread:pad, x1:0.233831, y1:0.267, x2:0.831025, y2:0.880364, stop:0 rgba(245,247,250,1), stop:1 rgba(195,207,226));\n"
"}")
        self.OcrselectWidget = HeaderCardWidget(setup)
        self.OcrselectWidget.setGeometry(QtCore.QRect(0, 80, 431, 111))
        self.OcrselectWidget.setTitle("")
        self.OcrselectWidget.setObjectName("OcrselectWidget")
        self.freeocrApi = LineEdit(self.OcrselectWidget)
        self.freeocrApi.setGeometry(QtCore.QRect(10, 60, 431, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeocrApi.sizePolicy().hasHeightForWidth())
        self.freeocrApi.setSizePolicy(sizePolicy)
        self.freeocrApi.setMinimumSize(QtCore.QSize(0, 40))
        self.freeocrApi.setObjectName("freeocrApi")
        self.splitter = QtWidgets.QSplitter(self.OcrselectWidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 581, 24))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.LocalOcr = RadioButton(self.splitter)
        self.LocalOcr.setObjectName("LocalOcr")
        self.FreeOcr = RadioButton(self.splitter)
        self.FreeOcr.setObjectName("FreeOcr")
        self.layoutWidget = QtWidgets.QWidget(setup)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 44, 408, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SubtitleLabel = SubtitleLabel(self.layoutWidget)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.horizontalLayout.addWidget(self.SubtitleLabel)
        spacerItem = QtWidgets.QSpacerItem(203, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.HyperlinkLabel = HyperlinkLabel(self.layoutWidget)
        self.HyperlinkLabel.setObjectName("HyperlinkLabel")
        self.HyperlinkLabel.setUrl('https://ocr.space/')
        self.horizontalLayout.addWidget(self.HyperlinkLabel)
        self.OK = PrimaryPushButton(setup)
        self.OK.setGeometry(QtCore.QRect(270, 210, 153, 32))
        self.OK.setObjectName("OK")

        self.retranslateUi(setup)
        QtCore.QMetaObject.connectSlotsByName(setup)

    def retranslateUi(self, setup):
        _translate = QtCore.QCoreApplication.translate
        setup.setWindowTitle(_translate("setup", "Form"))
        self.freeocrApi.setPlaceholderText(_translate("setup", "输入你的FreeOcr Api key"))
        self.LocalOcr.setText(_translate("setup", "本地OCR"))
        self.FreeOcr.setText(_translate("setup", "FREEOCR"))
        self.SubtitleLabel.setText(_translate("setup", "OCR选择"))
        self.HyperlinkLabel.setText(_translate("setup", "FreeOCRAPI申请"))
        self.OK.setText(_translate("setup", "确定"))
from qfluentwidgets import HeaderCardWidget, HyperlinkLabel, LineEdit, PrimaryPushButton, RadioButton, SubtitleLabel
