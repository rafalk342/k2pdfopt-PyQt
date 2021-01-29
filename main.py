import asyncio
import subprocess
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from qasync import QEventLoop

from MainWindow import Ui_MainWindow
from Options import Options
from Preview import Preview
from models.DeviceComboBoxModel import DeviceComboBoxModel
from utils import run_command_on_file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.options = Options()
        self.set_up_toggles()
        self.set_up_options()
        self.set_up_margin_option()
        self.chooseFileButton.pressed.connect(self.choose_file)
        self.convertFileButton.pressed.connect(self.convert)
        self.deviceComboBox.setModel(DeviceComboBoxModel())
        self.deviceComboBox.setCurrentIndex(self.options.get_device_index())
        self.deviceComboBox.activated.connect(self.device_changed)
        self.tabWidget.setCurrentIndex(0)
        self.preview = Preview()
        self.previewButton.clicked.connect(self.handle_preview_button_clicked)

    def set_up_toggles(self):
        toggles_map = {
            '-as': self.autostraightenCheckBox,
            '-bp': self.breakAfterEachCheckBox,
            '-c': self.colorOutputCheckBox,
            '-ls': self.landscapeCheckBox,
            '-n': self.nativePDFOutputCheckBox,
            '-r': self.rightToLeftCheckBox,
            '-sm': self.generateMarkedUpSourceCheckBox,
            '-wrap': self.reFlowTextCheckBox,
            '-evl 1': self.eraseVerticalLinesCheckBox
        }
        for name, checkbox in toggles_map.items():
            checkbox.setChecked(self.options.is_option_active(name))
            checkbox.stateChanged.connect(
                lambda checked, name=name, checkbox=checkbox: self.options.toggle_changed(checkbox, name))

    def set_up_options(self):
        options_map = {
            '-col': {'checkbox': self.maxColumnsCheckBox, 'line_edit': self.maxColumnsLineEdit},
            '-dr': {'checkbox': self.resolutionFactorCheckBox, 'line_edit': self.resolutionFactorLineEdit},
            '-p': {'checkbox': None, 'line_edit': self.pageRangeLineEdit}
        }
        for option_name, option_dict in options_map.items():
            checkbox = option_dict['checkbox']
            line_edit = option_dict['line_edit']
            if checkbox:
                checkbox.setChecked(self.options.is_option_active(option_name))
                checkbox.stateChanged.connect(
                    lambda checked, option_name=option_name, checkbox=checkbox: self.options.toggle_changed(checkbox,
                                                                                                            option_name))
            line_edit.setText(self.options.get_option_value(option_name))
            line_edit.textChanged.connect(
                lambda text, option_name=option_name: self.options.change_option_value(option_name, text))

    def set_up_margin_option(self):
        self.cropMarginCheckBox.setChecked(self.options.is_option_active('-m'))
        self.leftMarginLineEdit.setText(self.options.get_margin_value('left'))
        self.topMarginLineEdit.setText(self.options.get_margin_value('top'))
        self.rightMarginLineEdit.setText(self.options.get_margin_value('right'))
        self.bottomMarginLineEdit.setText(self.options.get_margin_value('bottom'))
        self.cropMarginCheckBox.stateChanged.connect(
            lambda: self.options.toggle_changed(self.cropMarginCheckBox, '-m'))
        self.leftMarginLineEdit.textChanged.connect(
            lambda text: self.options.change_margin_option('left', text))
        self.topMarginLineEdit.textChanged.connect(
            lambda text: self.options.change_margin_option('top', text))
        self.rightMarginLineEdit.textChanged.connect(
            lambda text: self.options.change_margin_option('right', text))
        self.bottomMarginLineEdit.textChanged.connect(
            lambda text: self.options.change_margin_option('bottom', text))

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', './',
                                                   "PDF files (*.pdf)")  # TODO change to QDir.homePath()
        self.inputFilePath.setText(file_path)

    def convert(self):
        # TODO file_path = self.inputFilePath.text()
        self.logText.clear()
        file_path = '/home/cst/code/k2pdfopt_PyQt/1.pdf'
        opt_file_path = '/home/cst/code/k2pdfopt_PyQt/1_k2opt.pdf'
        parsed_options = self.options.get_parsed_options(self.deviceComboBox)

        print('Converting file {}'.format(file_path))
        print('Parsed options {}'.format(parsed_options))
        asyncio.run_coroutine_threadsafe(run_command_on_file(parsed_options, file_path,
                                                             lambda text: self.logText.appendPlainText(text),
                                                             lambda status: subprocess.run(
                                                                 ['xdg-open', opt_file_path])),
                                         event_loop)
        self.tabWidget.setCurrentIndex(3)

    def handle_preview_button_clicked(self):
        self.logText.clear()
        page = self.previewLineEdit.text()
        self.imagePreview.setText('Loading preview...')
        file_path = '/home/cst/code/k2pdfopt_PyQt/1.pdf'
        parsed_options = self.options.get_parsed_options(self.deviceComboBox)
        parsed_options.append('-bmp {}'.format(page))

        print('Converting file {}'.format(file_path))
        print('Parsed options {}'.format(parsed_options))
        asyncio.run_coroutine_threadsafe(run_command_on_file(parsed_options, file_path,
                                                             lambda text: self.logText.appendPlainText(text),
                                                             lambda status: self.imagePreview.setPixmap(self.preview.generate_preview())),
                                         event_loop)

    def device_changed(self, index):
        text = self.deviceComboBox.itemText(index)
        data = self.deviceComboBox.itemData(index, QtCore.Qt.UserRole)
        print('User chose {} which corresponds to {}'.format(text, data))
        self.options.set_device_index(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    window = MainWindow()
    window.show()
    app.exec_()
