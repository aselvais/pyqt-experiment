import sys
from PyQt5 import QtWidgets
from libs.ui.MainWindow import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
