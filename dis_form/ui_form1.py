# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form1.ui'
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
        MainWindow.resize(679, 498)
        MainWindow.setWindowTitle(u"LSM")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.action_USB = QAction(MainWindow)
        self.action_USB.setObjectName(u"action_USB")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(554, 170, 121, 56))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(550, 340, 126, 56))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(550, 427, 126, 26))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 405, 75, 23))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 430, 75, 23))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(305, 405, 75, 23))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(305, 430, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 405, 56, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 430, 61, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 410, 66, 16))
        self.label_3.setWordWrap(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 335, 541, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(330, 5, 100, 22))
        self.textEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(115, 5, 100, 22))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(220, 5, 100, 22))
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setReadOnly(True)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(15, 5, 91, 16))
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(520, 5, 16, 22))
        self.textEdit_21 = QTextEdit(self.frame)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setGeometry(QRect(434, 5, 86, 22))
        self.textEdit_21.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_21.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_21.setReadOnly(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(265, 310, 131, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(5, 270, 541, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.textEdit_5 = QTextEdit(self.frame_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(331, 5, 100, 20))
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_6 = QTextEdit(self.frame_2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(116, 5, 100, 20))
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_7 = QTextEdit(self.frame_2)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(220, 5, 100, 20))
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setReadOnly(True)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 5, 96, 16))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.textEdit_19 = QTextEdit(self.frame_2)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(435, 5, 100, 20))
        self.textEdit_19.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_19.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_19.setReadOnly(True)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(5, 235, 541, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.textEdit_8 = QTextEdit(self.frame_3)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(331, 5, 100, 20))
        self.textEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setReadOnly(True)
        self.textEdit_9 = QTextEdit(self.frame_3)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(116, 5, 100, 20))
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setReadOnly(True)
        self.textEdit_10 = QTextEdit(self.frame_3)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(220, 5, 100, 20))
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setReadOnly(True)
        self.textEdit_18 = QTextEdit(self.frame_3)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(435, 5, 100, 20))
        self.textEdit_18.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_18.setReadOnly(True)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 96, 26))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(5, 165, 541, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.textEdit_11 = QTextEdit(self.frame_4)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(331, 5, 100, 20))
        self.textEdit_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_11.setReadOnly(True)
        self.textEdit_12 = QTextEdit(self.frame_4)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(116, 5, 100, 20))
        self.textEdit_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_12.setReadOnly(True)
        self.textEdit_13 = QTextEdit(self.frame_4)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(220, 5, 100, 20))
        self.textEdit_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_13.setReadOnly(True)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 5, 96, 16))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.textEdit_20 = QTextEdit(self.frame_4)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setGeometry(QRect(435, 5, 100, 20))
        self.textEdit_20.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_20.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_20.setReadOnly(True)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(5, 200, 541, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.textEdit_14 = QTextEdit(self.frame_5)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(331, 5, 100, 20))
        self.textEdit_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setReadOnly(True)
        self.textEdit_15 = QTextEdit(self.frame_5)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(116, 5, 100, 20))
        self.textEdit_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_15.setReadOnly(True)
        self.textEdit_16 = QTextEdit(self.frame_5)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(220, 5, 100, 20))
        self.textEdit_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_16.setReadOnly(True)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 0, 96, 26))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.textEdit_17 = QTextEdit(self.frame_5)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(435, 5, 100, 20))
        self.textEdit_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_17.setReadOnly(True)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(5, 370, 541, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 96, 26))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.comboBox_2 = QComboBox(self.frame_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(114, 5, 421, 20))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(185, 115, 81, 16))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(395, 115, 81, 16))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(264, 75, 131, 31))
        self.label_14.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 425, 101, 31))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(5, 130, 541, 31))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(1)
        self.textEdit_ = QTextEdit(self.frame_7)
        self.textEdit_.setObjectName(u"textEdit_")
        self.textEdit_.setGeometry(QRect(220, 5, 100, 20))
        self.textEdit_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_.setReadOnly(True)
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 5, 96, 16))
        self.label_15.setAlignment(Qt.AlignCenter)
        self.textEdit_24 = QTextEdit(self.frame_7)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setGeometry(QRect(435, 5, 100, 20))
        self.textEdit_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_24.setReadOnly(True)
        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(115, 4, 102, 22))
        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(330, 4, 102, 22))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 681, 66))
        self.label_16.setPixmap(QPixmap(u"../img/lsm_logo.png"))
        self.label_16.setScaledContents(True)
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(550, 120, 126, 41))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(5, 15, 60, 20))
        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(65, 15, 60, 20))
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(7, 0, 56, 16))
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(67, 0, 56, 16))
        self.label_18.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 395, 666, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(555, 240, 120, 56))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setStyleSheet(u"border: 3px solid #a0a0a0;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 300, 666, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 65, 666, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 679, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_USB)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.action_USB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 USB", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u043e\u0430\u043c\u043c\u0435", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u041c\u043e\u0434\u0435\u043c\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u041e\u041f \u041b\u0421\u041c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u041b\u0421\u041c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422 \u041b\u0421\u041c", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" vertical-align:middle;\">\u0420\u0435\u0437\u0435\u0440\u0432</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0435\u0437\u0435\u0440\u0432</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0432\u0435\u0440\u0442\u043a\u0430", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043b\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0437\u0432\u0435\u0440\u0442\u043a\u0430", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438 \u0438\u0437\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0441 \u0434\u0430\u0442\u0447\u0438\u043a\u043e\u043c \u043e\u0441\u0432\u0435\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u0430\u044f \u0431\u0430\u0448\u043d\u044f", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0430\u044f \u0431\u0430\u0448\u043d\u044f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u041b\u0421\u041c\n"
"\u0432 \u0437\u0430\u0432. \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043b\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.label_19.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        pass
    # retranslateUi

