# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2.ui'
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
        Form.resize(220, 139)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 15, 47, 13))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 45, 47, 13))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 75, 81, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(15, 100, 81, 31))
        self.label_4.setWordWrap(True)
        self.lsm__usb_stop_bit = QLineEdit(Form)
        self.lsm__usb_stop_bit.setObjectName(u"lsm__usb_stop_bit")
        self.lsm__usb_stop_bit.setGeometry(QRect(95, 70, 113, 20))
        self.lsm__usb_check_odd = QCheckBox(Form)
        self.lsm__usb_check_odd.setObjectName(u"lsm__usb_check_odd")
        self.lsm__usb_check_odd.setGeometry(QRect(95, 105, 111, 17))
        self.lsm__usb_port = QComboBox(Form)
        self.lsm__usb_port.setObjectName(u"lsm__usb_port")
        self.lsm__usb_port.setGeometry(QRect(95, 10, 111, 22))
        self.lsm__usb_size_data = QSpinBox(Form)
        self.lsm__usb_size_data.setObjectName(u"lsm__usb_size_data")
        self.lsm__usb_size_data.setGeometry(QRect(95, 40, 111, 22))
        self.lsm__usb_size_data.setMinimum(8)
        self.lsm__usb_size_data.setMaximum(1024)
        self.lsm__usb_size_data.setSingleStep(8)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 USB", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043f\u043e\u0432\u044b\u0439 \u0431\u0438\u0442", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0430 \u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.lsm__usb_check_odd.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043e", None))
    # retranslateUi

