from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        """

        Args:
            data ([type]): [description]
        """
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        """

        Args:
            index ([type]): [description]
            role ([type]): [description]

        Returns:
            [type]: [description]
        """
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        """

        Args:
            index ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._data.shape[0]

    def columnCount(self, index):
        """

        Args:
            index ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        """

        Args:
            section ([type]): [description]
            orientation ([type]): [description]
            role ([type]): [description]

        Returns:
            [type]: [description]
        """
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
