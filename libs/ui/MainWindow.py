"""
For tabular data check https://www.learnpyqt.com/courses/model-views/qtableview-modelviews-numpy-pandas/
for tech talk project :)

"""
# from typeguard import typechecked
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QCommandLinkButton, QTableView, QColumnView, QPlainTextEdit
import pandas as pd
from libs.logmanagement.Analyzer import Analyzer

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QtWidgets.QMainWindow):

    ui: QtWidgets

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("ui/mainwindow.ui", self)
        self._setup_connectors()

    def _get_btn_clickme(self) -> QPushButton:
        return self.ui.btn_clickme

    def _get_btn_linkme(self) -> QCommandLinkButton:
        return self.ui.btn_linkme

    def _get_table_view(self) -> QTableView:
        return self.ui.table_view

    def _get_column_view(self) -> QColumnView:
        return self.ui.column_view

    def _get_plain_text_edit(self) -> QPlainTextEdit:
        return self.ui.plain_text_edit

    def _setup_connectors(self):
        self._get_btn_clickme().clicked.connect(self.clicked_clickme)
        self._get_btn_linkme().clicked.connect(self.clicked_linkme)

    def clicked_clickme(self):
        self._log("button btn_linkme clicked !!!")

    def clicked_linkme(self):
        self._log("button btn_linkme clicked !!!! YEAH!")
        self.get_data()

    def _log(self, txt: str = ""):
        """Add text to the plain text box in the GUI

        Args:
            txt (str, optional): [description]. Defaults to "".
        """
        self._get_plain_text_edit().appendPlainText(txt)

    def add_table_data(self):
        # setModel(self, model: QtCore.QAbstractItemModel) -> None: ...
        tbl = self._get_table_view()
        tbl.setModel()

    def get_data(self):
        _analyzer = Analyzer(['DlxSnapshotsUtils.log'])
        data = _analyzer.get_simple_df()
        self.model = TableModel(data)
        self._get_table_view().setModel(self.model)


