from PyQt5 import QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    """

    Args:
        QtWidgets ([type]): [description]
    """

    # ui -> QtWidgets.QPlainTextEdit

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("ui/mainwindow.ui", self)
        self._setup_connectors()

    def _setup_connectors(self):
        """
        """
        self.ui.btn_clickme.clicked.connect(self.clicked_clickme)
        self.ui.btn_linkme.clicked.connect(self.clicked_linkme)

    def clicked_clickme(self):
        """
        """
        v = "button btn_linkme clicked !!!"
        print(v)
        self._log(v)

    def clicked_linkme(self):
        """
        """
        v = "button btn_linkme clicked !!!! YEAH!"
        print(v)
        self._log(v)

    def _log(self, txt=""):
        """Add text to the plain text box in the GUI

        Args:
            txt (str, optional): [description]. Defaults to "".
        """
        self.ui.plain_text_edit.appendPlainText(txt)


