import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PySide2.QtCore import Qt
from random import choice
from serial.tools import list_ports

import yaml

from lsm_dev.lsm import SimpleCommands
from dis_form.ui_form1 import Ui_MainWindow
from dis_form.ui_form2 import Ui_Form

from lsm_dev.lsm import LSM 


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

class SetingUSB(QWidget, Ui_Form):
    def __init__(self):
        super(SetingUSB, self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
setting_usb = SettingUSB()
window.show()
print([(i.name, i.interface, i.description) for i in list_ports.comports(True)])
lsm = LSM()
window.menu.actions()[0].triggered.connect(setting_usb.show)


app.exec_()