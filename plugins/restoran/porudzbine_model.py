from PySide2 import QtCore
import csv


class PorudzbineModel(QtCore.QAbstractTableModel):

    def __init__(self, path=""):

        super().__init__()

        self._data = []
        self.load_data(path)

    def rowCount(self, index):

        return len(self._data)

    def columnCount(self, index):

        return 6

    def data(self, index, role):

        element = self.get_element(index)
        if element is None:
            return None

        if role == QtCore.Qt.DisplayRole:
            return element

    def headerData(self, section, orientation, role):

        if orientation != QtCore.Qt.Vertical:
            if (section == 0) and (role == QtCore.Qt.DisplayRole):
                return "Restoran"
            elif (section == 1) and (role == QtCore.Qt.DisplayRole):
                return "Adresa restorana"
            elif (section == 2) and (role == QtCore.Qt.DisplayRole):
                return "Napomena"
            elif (section == 3) and (role == QtCore.Qt.DisplayRole):
                return "Cena"
            elif (section == 4) and (role == QtCore.Qt.DisplayRole):
                return "Adresa dostave"
            elif (section == 5) and (role == QtCore.Qt.DisplayRole):
                return "Status"

    def setData(self, index, value, role):

        try:
            if value == "":
                return False
            self._data[index.row()][index.column()] = value
            self.dataChanged()
            return True
        except:
            return False

    def get_element(self, index: QtCore.QModelIndex):

        if index.isValid():
            element = self._data[index.row()][index.column()]
            if element:
                return element
        return None

    def load_data(self, path=""):

        with open(path, "r", encoding="utf-8") as fp:
            self._data = list(csv.reader(fp, dialect=csv.unix_dialect))

    def get_data(self):
        return self._data
