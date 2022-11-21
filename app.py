import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget, QComboBox, QCheckBox
from PySide2.QtCore import Qt
from random import choice
from serial.tools import list_ports

import yaml

from dis_form.ui_form1 import Ui_MainWindow
from dis_form.ui_form2 import Ui_Form as FormSettingUSB
from dis_form.ui_form3 import Ui_Form as FormHistory
from dis_form.ui_form4 import Ui_widget as FormSettingModem


from lsm_dev.lsm import LSM 


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

class SettingUSB(QWidget, FormSettingUSB):
    def __init__(self):
        super(SettingUSB, self).__init__()
        self.setupUi(self)

class SettingModem(QWidget, FormSettingModem):
    def __init__(self):
        super(SettingModem, self).__init__()
        self.setupUi(self)

class History(QWidget, FormHistory):
    def __init__(self):
        super(History, self).__init__()
        self.setupUi(self)


class DataСarrier:
    def __innit__(self, dict_params):
        self.dict_params = dict_params
    
    def getParam(self):
        res={}
        for k, v in self.dict_params.items():
            if isinstance(v, QTextEdit):
                res[k]=v.toPlainText()
            elif isinstance(v, QLineEdit):
                res[k]=v.text()
            elif isinstance(v, QComboBox):
                res[k]=v.currentIndex()
            elif isinstance(v, QCheckBox):
                    res[k]=v.isChecked()
        return res
    
    def setParam(self, set_param):
        for k, v in self.set_param.items():
            if k in self.dict_params:
                if isinstance(self.dict_params[k], QTextEdit):
                    self.dict_params[k].setPlainText(v)
                elif isinstance(v, QLineEdit):
                    self.dict_params[k].text(v)
                elif isinstance(v, QComboBox):
                    self.dict_params[k].setCurrentIndex(v)
                elif isinstance(v, QCheckBox):
                    self.dict_params[k].setChecked(v)




app = QApplication(sys.argv)

window = MainWindow()
setting_usb = SettingUSB()
setting_modem = SettingModem()
history = History()

window.show()
print([(i.name, i.interface, i.description) for i in list_ports.comports(True)])
lsm = LSM()

window.menu.actions()[0].triggered.connect(setting_usb.show)
window.menu.actions()[1].triggered.connect(setting_modem.show)
#print(dir(window.findChildren(QTextEdit)[0]))

dict_param = {'__'.join(t.objectName().split('__')[1:]):t for t in  window.findChildren(QTextEdit) if t.objectName().find('lsm__') >= 0}
dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  window.findChildren(QComboBox) if t.objectName().find('lsm__') >= 0}) 
dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  setting_usb.findChildren(QTextEdit) if t.objectName().find('lsm__') >= 0}) 
dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  setting_usb.findChildren(QComboBox) if t.objectName().find('lsm__') >= 0}) 
dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  history.findChildren(QTextEdit) if t.objectName().find('lsm__') >= 0}) 
dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  history.findChildren(QComboBox) if t.objectName().find('lsm__') >= 0}) 

data_carrier = DataСarrier(dict_param)
app.exec_()