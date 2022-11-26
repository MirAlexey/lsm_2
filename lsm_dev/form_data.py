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
        #print(id(self.dict_params))
        #print(id(self.dict_params['lsm_module__m3']))
        for k, v in self.dict_params.items():
            if isinstance(v, QTextEdit):
                #print(k, v.toPlainText())
                cur_v = v.toPlainText()
                if (cur_v == 'Вкл') or (cur_v =='Выкл'):
                    cur_v = cur_v == 'Вкл'
                res[k]=cur_v
            elif isinstance(v, QLineEdit):
                res[k]=v.text()
            elif isinstance(v, QComboBox):
                res[k]=v.itemData(v.currentIndex())
            elif isinstance(v, QCheckBox):
                    res[k]=v.isChecked()
            elif isinstance(v, QSpinBox):
                    res[k]=v.value()
        #print(res)
        return res
    
    def setParam(self, set_param):
        
        for k, v in set_param.items():
            if k in self.dict_params:
                if isinstance(self.dict_params[k], QTextEdit):
                    self.dict_params[k].setPlainText(str(v) if type(v) != bool else 'Вкл' if v else 'Выкл')
                elif isinstance(v, QLineEdit):
                    self.dict_params[k].text(v)
                elif isinstance(v, QComboBox):
                    c_i = self.dict_params[k].findData(f'{v:0>2x}')
                    self.dict_params[k].setCurrentIndex(c_i)
                elif isinstance(v, QCheckBox):
                    self.dict_params[k].setChecked(bool(v))
                elif isinstance(v, QSpinBox):
                    self.dict_params[k].setValue(int(v))