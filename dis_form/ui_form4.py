# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(217, 252)
        self.groupBox = QGroupBox(widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(5, 10, 211, 116))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 86, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 45, 76, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 47, 13))
        self.lsm__SF = QComboBox(self.groupBox)
        self.lsm__SF.setObjectName(u"lsm__SF")
        self.lsm__SF.setGeometry(QRect(95, 15, 111, 21))
        self.lsm__SF.setFrame(False)
        self.lsm__BW = QComboBox(self.groupBox)
        self.lsm__BW.setObjectName(u"lsm__BW")
        self.lsm__BW.setGeometry(QRect(95, 40, 111, 22))
        self.lsm__P = QComboBox(self.groupBox)
        self.lsm__P.setObjectName(u"lsm__P")
        self.lsm__P.setGeometry(QRect(95, 65, 111, 22))
        self.lsm__CH = QComboBox(self.groupBox)
        self.lsm__CH.setObjectName(u"lsm__CH")
        self.lsm__CH.setGeometry(QRect(95, 90, 111, 22))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 95, 47, 13))
        self.groupBox_2 = QGroupBox(widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(5, 130, 206, 91))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 86, 16))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 45, 76, 16))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 70, 47, 13))
        self.Status_MC1 = QLabel(self.groupBox_2)
        self.Status_MC1.setObjectName(u"Status_MC1")
        self.Status_MC1.setGeometry(QRect(95, 20, 86, 16))
        self.Status_MC2 = QLabel(self.groupBox_2)
        self.Status_MC2.setObjectName(u"Status_MC2")
        self.Status_MC2.setGeometry(QRect(95, 45, 81, 16))
        self.Status_MC3 = QLabel(self.groupBox_2)
        self.Status_MC3.setObjectName(u"Status_MC3")
        self.Status_MC3.setGeometry(QRect(95, 70, 86, 16))
        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(5, 225, 106, 23))
        self.pushButton_2 = QPushButton(widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(114, 225, 96, 23))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043c\u043e\u0434\u0435\u043c\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043c\u043e\u0434\u0435\u043c\u0430", None))
        self.label.setText(QCoreApplication.translate("widget", u"SpreadingFactor", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"Bandwidth", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"Power", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"Channel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("widget", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"\u041c\u0421-1", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"M\u0421-2", None))
        self.label_7.setText(QCoreApplication.translate("widget", u"MC-3", None))
        self.Status_MC1.setText(QCoreApplication.translate("widget", u"\u043d\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043e", None))
        self.Status_MC2.setText(QCoreApplication.translate("widget", u"\u043d\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043e", None))
        self.Status_MC3.setText(QCoreApplication.translate("widget", u"\u043d\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

