import asyncio
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from qasync import QEventLoop

from MainWindow import Ui_MainWindow
from utils import run_command_on_file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.chooseFileButton.pressed.connect(self.choose_file)
        self.convertFileButton.pressed.connect(self.convert)

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', './',
                                                   "PDF files (*.pdf)")  # TODO change to QDir.homePath()
        self.inputFilePath.setText(file_path)

    def convert(self):
        # TODO file_path = self.inputFilePath.text()
        file_path = '/home/cst/code/k2pdfopt_PyQt/1.pdf'
        print('Converting file {}'.format(file_path))
        asyncio.run_coroutine_threadsafe(run_command_on_file(file_path, lambda text: self.logText.appendPlainText(text),
                                                             lambda status: print('Got status {}'.format(status))),
                                         event_loop)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    window = MainWindow()
    window.show()
    app.exec_()
    event_loop.run_forever()
