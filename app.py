import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget, QComboBox, QCheckBox, QSpinBox, QPushButton
from PySide2.QtCore import Qt, QAbstractListModel, QModelIndex
from random import choice
from serial.tools import list_ports

import yaml

from dis_form.ui_form1 import Ui_MainWindow
from dis_form.ui_form2 import Ui_Form as FormSettingUSB
from dis_form.ui_form3 import Ui_Form as FormHistory
from dis_form.ui_form4 import Ui_widget as FormSettingModem


from lsm_dev.lsm import LSM 

from lsm_dev.form_data import MyListModel, DataСarrier


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



app = QApplication(sys.argv)

window = MainWindow()
setting_usb = SettingUSB()
setting_modem = SettingModem()
history = History()

window.show()
print([(i.name, i.interface, i.description) for i in list_ports.comports(True)])


window.menu.actions()[0].triggered.connect(setting_usb.show)
window.menu.actions()[1].triggered.connect(setting_modem.show)
dict_param = {}
for i in [window, setting_usb, history, setting_modem]:
    for j in [QTextEdit, QComboBox, QSpinBox, QLineEdit, QPushButton]:
        dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  i.findChildren(j) if t.objectName().find('lsm__') >= 0})

print(list(dict_param.keys()))

data_carrier = DataСarrier(dict_param)
lsm = LSM(data_carrier)
print(lsm.setting_modem)
for sm in lsm.setting_modem:
    if sm.type == 'list':
        data_sm = [[v,k] for v,k in zip(sm.param.values, sm.param.keys)]
    elif sm.type == 'step list':
        keys = [f'{sm.param.keys.start +sm.param.keys.step*i} МГц' for i in range(int((sm.param.keys.end - sm.param.keys.start) / sm.param.keys.step)+1)]
        values = [sm.param.values.start + sm.param.values.step*i for i in range(int((sm.param.values.end - sm.param.values.start) / sm.param.values.step)+1)]
        data_sm = [[v,k] for v,k in zip(values, keys)]
    else:
        data_sm = [['-', '-']]
    dict_param[sm.name].setModel(MyListModel(data_sm))


dict_param['power'].setModel(MyListModel([['11','11data'], ['12','12data'],['13','13data']]))
def FlagToTextM0():
    print('ops')
    if dict_param['lsm_module__m0'].toPlainText() == '1':
        dict_param['lsm_module__m0'].setPlainText('Основной')
    if dict_param['lsm_module__m0'].toPlainText() == '0':
        dict_param['lsm_module__m0'].setPlainText('Резерв')
dict_param['lsm_module__m0'].textChanged.connect(FlagToTextM0)

def FlagToTextM1():
    if dict_param['lsm_module__m1'].toPlainText() == '1':
        dict_param['lsm_module__m1'].setPlainText('Основной')
    if dict_param['lsm_module__m1'].toPlainText() == '0':
        dict_param['lsm_module__m1'].setPlainText('Резерв')
dict_param['lsm_module__m1'].textChanged.connect(FlagToTextM1)

def FlagToTextM2():
    if dict_param['lsm_module__m2'].toPlainText() == '1':
        dict_param['lsm_module__m2'].setPlainText('Основной')
    if dict_param['lsm_module__m2'].toPlainText() == '0':
        dict_param['lsm_module__m2'].setPlainText('Резерв')
dict_param['lsm_module__m0'].textChanged.connect(FlagToTextM2)

def FlagToTextM3():
    if dict_param['lsm_module__m3'].toPlainText() == '1':
        dict_param['lsm_module__m3'].setPlainText('Основной')
    if dict_param['lsm_module__m3'].toPlainText() == '0':
        dict_param['lsm_module__m3'].setPlainText('Резерв')
dict_param['lsm_module__m3'].textChanged.connect(FlagToTextM3)


def ConnectModem():
    print('click')
    if ~lsm.initUsbPort():
        print('USB ops')
    rrr = lsm.checkModem()   
    print(rrr) 
    if not rrr:#~lsm.checkModem():
        print('Modem ops')
    pass
dict_param['modem_apply'].released.connect(ConnectModem)

print(id(dict_param))
print(id(dict_param['lsm_module__m3']))


dict_param['usb_port'].setModel(MyListModel([[i.name, i.description] for i in list_ports.comports(True)]))
print('iii')
dict_param['lsm_module__m0'].setPlainText('1')


print([[i.name, i.description] for i in list_ports.comports(True)])




def foo(i):
    dict_param['date'].setPlainText(dict_param['power'].itemData(i))

dict_param['power'].currentIndexChanged.connect(foo)


app.exec_()