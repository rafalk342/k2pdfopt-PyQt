import asyncio
import subprocess
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from qasync import QEventLoop

from MainWindow import Ui_MainWindow
from models.DeviceComboBoxModel import DeviceComboBoxModel
from utils import run_command_on_file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.chooseFileButton.pressed.connect(self.choose_file)
        self.convertFileButton.pressed.connect(self.convert)
        self.deviceComboBox.setModel(DeviceComboBoxModel())
        self.deviceComboBox.activated.connect(self.device_changed)
        self.autostraightenCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.autostraightenCheckBox, '-as'))
        self.breakAfterEachCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.breakAfterEachCheckBox, '-bp'))
        self.colorOutputCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.colorOutputCheckBox, '-c'))
        self.landscapeCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.landscapeCheckBox, '-ls'))
        self.nativePDFOutputCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.nativePDFOutputCheckBox, '-n'))
        self.rightToLeftCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.rightToLeftCheckBox, '-r'))
        self.generateMarkedUpSourceCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.generateMarkedUpSourceCheckBox, '-sm'))
        self.reFlowTextCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.reFlowTextCheckBox, '-wrap'))
        self.eraseVerticalLinesCheckBox.stateChanged.connect(
            lambda: self.checkbox_changed(self.eraseVerticalLinesCheckBox, '-evl 1'))
        self.options = {'-dev': ''}
        self.arguments = set()
        self.tabWidget.setCurrentIndex(0)

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', './',
                                                   "PDF files (*.pdf)")  # TODO change to QDir.homePath()
        self.inputFilePath.setText(file_path)

    def convert(self):
        # TODO file_path = self.inputFilePath.text()
        self.logText.clear()
        file_path = '/home/cst/code/k2pdfopt_PyQt/1.pdf'
        opt_file_path = '/home/cst/code/k2pdfopt_PyQt/1_k2opt.pdf'
        parsed_options = []
        for option, value in self.options.items():
            if value:
                parsed_options.append(option)
                parsed_options.append(value)
        print('Converting file {}'.format(file_path))
        asyncio.run_coroutine_threadsafe(run_command_on_file(list(self.arguments), parsed_options, file_path,
                                                             lambda text: self.logText.appendPlainText(text),
                                                             lambda status: subprocess.run(['xdg-open', opt_file_path])),
                                         event_loop)
        self.tabWidget.setCurrentIndex(3)

    def device_changed(self, index):
        text = self.deviceComboBox.itemText(index)
        data = self.deviceComboBox.itemData(index, QtCore.Qt.UserRole)
        print('User chose {} which corresponds to {}'.format(text, data))
        self.options['-dev'] = data

    def checkbox_changed(self, checkbox, argument):
        if checkbox.isChecked():
            print('Adding {} to arguments'.format(argument))
            self.arguments.add(argument)
        else:
            print('Removing {} from arguments'.format(argument))
            self.arguments.remove(argument)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    window = MainWindow()
    window.show()
    app.exec_()
