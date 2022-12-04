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
from dis_form.ui_form5 import Ui_Form as FormAdditionalParams


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

class AdditionalParams(QWidget, FormAdditionalParams):
    def __init__(self):
        super(AdditionalParams, self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
setting_usb = SettingUSB()
setting_modem = SettingModem()
history = History()
spec_params = AdditionalParams()

window.show()
print([(i.name, i.interface, i.description) for i in list_ports.comports(True)])


window.menu.actions()[0].triggered.connect(setting_usb.show)
window.menu.actions()[1].triggered.connect(setting_modem.show)
dict_param = {}
for i in [window, setting_usb, history, setting_modem, spec_params]:
    for j in [QTextEdit, QComboBox, QSpinBox, QLineEdit, QPushButton, QCheckBox]:
        dict_param.update({'__'.join(t.objectName().split('__')[1:]):t for t in  i.findChildren(j) if t.objectName().find('lsm__') >= 0})

print(list(dict_param.keys()))

data_carrier = DataСarrier(dict_param)
lsm = LSM(data_carrier)
#print(lsm.setting_modem)
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


def ConnectModem():
    res0, prm0 = lsm.initUsbPort()
    res1, prm1 = lsm.checkModem() 
dict_param['modem_apply'].released.connect(ConnectModem)

def LinkRequestK1():
    LinkRequest('k1')

def LinkRequestK2():
    LinkRequest('k2')

def LinkRequest(dest):
    res0, prm0 = lsm.initUsbPort()
    if not res0:
        return 0
    res1, prm1 = lsm.ComLinkRequest(dest)
    if not res1:
        return 0
    if prm1 is not None:
        data_carrier.setParam(prm1)

    # res2, prm2 = lsm.ComShortStatus()

    # if res2 and (prm2 is not None):
    #     data_carrier.setParam(prm2)
    


dict_param['link_request_k1'].released.connect(LinkRequestK1)
dict_param['link_request_k2'].released.connect(LinkRequestK2)

def StartLsm():
    res, prm = lsm.ComStartLsm()

dict_param['start'].released.connect(StartLsm)

def StoptLsm():
    res, prm = lsm.ComStopLsm()

dict_param['stop'].released.connect(StoptLsm)

def ResetLsm():
    res, prm = lsm.ComResetLsm()

dict_param['reset'].released.connect(ResetLsm)

def HardResetLsm():
    res, prm = lsm.ComHardResetLsm()

dict_param['hard_reset'].released.connect(HardResetLsm)

def GetShortStatusLsm():
    res, prm = lsm.ComShortStatus()
    if res and (prm is not None):
        data_carrier.setParam(prm)

dict_param['short_status'].released.connect(GetShortStatusLsm)

def SetLsmParams():
    res, prm = lsm.ComSetModeLSM()

dict_param['set_setting'].released.connect(SetLsmParams)

spec_params.show()





dict_param['usb_port'].setModel(MyListModel([[i.name, i.description] for i in list_ports.comports(True)]))


def ChangePowerSetting():
    i = dict_param['power'].itemData(dict_param['power'].currentIndex())
    dict_param['fotoavtomat__m'].setChecked(bool(i&1))
    dict_param['dynamic_power__m'].setChecked(bool(i>>1&1))
    dict_param['max_nom_power__m'].setChecked(bool(i>>2&1))
    dict_param['current_illumination__m'].setChecked(bool(i>>3&1))

dict_param['power'].currentIndexChanged.connect(ChangePowerSetting)


app.exec_()