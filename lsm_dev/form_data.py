from PySide2.QtCore import Qt, QAbstractListModel, QModelIndex
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget, QComboBox, QCheckBox, QSpinBox 


class MyListModel(QAbstractListModel):
    def __init__(self, data,  parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)


    def data(self, index=QModelIndex(), role: int = Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._data[index.row()]

            if role == Qt.DisplayRole:
                return item[1]
            elif role == Qt.UserRole:
                return item[0]

class DataСarrier:
    def __init__(self, dict_params):
        self.dict_params = dict_params
    
    def getParam(self):
        res={}
        for k, v in self.dict_params.items():
            if isinstance(v, QTextEdit):
                res[k]=v.toPlainText()
            elif isinstance(v, QLineEdit):
                res[k]=v.text()
            elif isinstance(v, QComboBox):
                res[k]=v.itemData(v.currentIndex())
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
                    c_i = self.dict_params[k].findData(f'{v:0>2x}')
                    self.dict_params[k].setCurrentIndex(c_i)
                elif isinstance(v, QCheckBox):
                    self.dict_params[k].setChecked(v)
