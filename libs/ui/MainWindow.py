"""
For tabular data check https://www.learnpyqt.com/courses/model-views/qtableview-modelviews-numpy-pandas/
for tech talk project :)

"""
# from typeguard import typechecked
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsView, QProgressBar, QCommandLinkButton, QTableView, QPlainTextEdit
from libs.logmanagement.Analyzer import Analyzer
from libs.ui.TableModel import TableModel
import time

class MainWindow(QtWidgets.QMainWindow):

    ui: QtWidgets
    model: TableModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("ui/mainwindow.ui", self)
        self._setup_connectors()
        self._get_progress_bar().setValue(0)
        view: QGraphicsView = self._get_graphics_view()
        view.setStyleSheet("background-image: url(./assets/images/backgroundtile.jpg)")
        # text_edit_message
        # text_edit_funcname
        # text_edit_process
        # combo_box_levelname
        # date_edit
        # graphics_view
        # progress_bar

    def _setup_connectors(self):
        self._get_btn_submit().clicked.connect(self.clicked_btn_submit)

    def _get_btn_submit(self) -> QCommandLinkButton:
        return self.ui.btn_submit

    def _get_graphics_view(self) -> QGraphicsView:
        return self.ui.graphics_view
    
    def _get_progress_bar(self) -> QProgressBar:
        return self.ui.progress_bar

    def _get_table_view(self) -> QTableView:
        return self.ui.table_view

    def _get_plain_text_edit(self) -> QPlainTextEdit:
        return self.ui.plain_text_edit

    def clicked_btn_submit(self):
        """
        when clicking the linkme button
        """
        self._log("button btn_submit clicked !!!! YEAH!")
        self._get_progress_bar().setValue(50)
        self.add_table_data()

    def _log(self, txt: str = ""):
        """
        Add text to the plain text box in the GUI

        Args:
            txt (str, optional): [description]. Defaults to "".
        """
        self._get_plain_text_edit().appendPlainText(txt)

    def add_table_data(self):
        """
        Push data to the data grid
        """
        self._get_table_view().setModel(self.get_data())
        self._get_progress_bar().setValue(100)
        time.sleep(1)
        self._get_progress_bar().setValue(0)


    def get_data(self):
        """
        Return a TableModel class with log data

        Returns:
            TableModel: log data
        """
        _analyzer = Analyzer([
            # 'DlxSnapshotsUtils.log.2020-09-04',
            # 'DlxSnapshotsUtils.log.2020-09-03',
            'DlxSnapshotsUtils.log',
        ])
        self.model = TableModel(_analyzer.get_simple_df())
        return self.model
