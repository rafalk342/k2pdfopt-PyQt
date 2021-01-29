import asyncio
import json
import subprocess
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from qasync import QEventLoop

from MainWindow import Ui_MainWindow
from models.DeviceComboBoxModel import DeviceComboBoxModel
from utils import run_command_on_file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    OPTIONS_FILENAME = "./options.json"
    OPTION_TYPE_TOGGLE = "TOGGLE"
    OPTION_TYPE_DEFAULT = "DEFAULT"
    OPTION_TYPE_MARGIN = "MARGIN"
    OPTION_TYPE_DEVICE = "DEVICE"

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.options_json = json.load(open(self.OPTIONS_FILENAME))
        self.set_up_toggles()
        self.set_up_options()
        self.set_up_margin_option()
        self.chooseFileButton.pressed.connect(self.choose_file)
        self.convertFileButton.pressed.connect(self.convert)
        self.deviceComboBox.setModel(DeviceComboBoxModel())
        self.deviceComboBox.setCurrentIndex(self.options_json['-dev']['value'])
        self.deviceComboBox.activated.connect(self.device_changed)
        self.tabWidget.setCurrentIndex(0)

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
            checkbox.setChecked(self.options_json[name]['active'])
            checkbox.stateChanged.connect(lambda checked, name=name, checkbox=checkbox: self.toggle_changed(checkbox, name))

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
                checkbox.setChecked(self.options_json[option_name]['active'])
                checkbox.stateChanged.connect(lambda checked, option_name=option_name, checkbox=checkbox: self.toggle_changed(checkbox, option_name))
            line_edit.setText(self.options_json[option_name]['value'])
            line_edit.textChanged.connect(lambda text, option_name=option_name: self.option_line_edit_changed(option_name, text))

    def set_up_margin_option(self):
        self.cropMarginCheckBox.setChecked(self.options_json['-m']['active'])
        self.leftMarginLineEdit.setText(self.options_json['-m']['left'])
        self.topMarginLineEdit.setText(self.options_json['-m']['top'])
        self.rightMarginLineEdit.setText(self.options_json['-m']['right'])
        self.bottomMarginLineEdit.setText(self.options_json['-m']['bottom'])
        self.cropMarginCheckBox.stateChanged.connect(
            lambda: self.toggle_changed(self.cropMarginCheckBox, '-m'))
        self.leftMarginLineEdit.textChanged.connect(
            lambda text: self.change_margin_option('left', text))
        self.topMarginLineEdit.textChanged.connect(
            lambda text: self.change_margin_option('top', text))
        self.rightMarginLineEdit.textChanged.connect(
            lambda text: self.change_margin_option('right', text))
        self.bottomMarginLineEdit.textChanged.connect(
            lambda text: self.change_margin_option('bottom', text))

    def change_margin_option(self, side, value):
        self.options_json['-m'][side] = value
        self.save_options_to_file()

    def toggle_changed(self, checkbox, argument):
        if checkbox.isChecked():
            print('Toggle {} activated'.format(argument))
            self.options_json[argument]['active'] = True
        else:
            print('Toggle {} deactivated'.format(argument))
            self.options_json[argument]['active'] = False
        self.save_options_to_file()

    def save_options_to_file(self):
        with open(self.OPTIONS_FILENAME, 'w') as options_file:
            json.dump(self.options_json, options_file, indent=4)

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
        for option_name, option_dict in self.options_json.items():
            if option_dict['active']:
                if option_dict['type'] == self.OPTION_TYPE_DEFAULT and option_dict['value']:
                    parsed_options.append(option_name)
                    parsed_options.append(option_dict['value'])
                elif option_dict['type'] == self.OPTION_TYPE_MARGIN:
                    parsed_options.append(option_name)
                    parsed_options.append(self.get_margin_option_value())
                elif option_dict['type'] == self.OPTION_TYPE_DEVICE:
                    parsed_options.append(option_name)
                    parsed_options.append(self.deviceComboBox.itemData(option_dict['value'], QtCore.Qt.UserRole))

        print('Converting file {}'.format(file_path))
        print('Parsed options {}'.format(parsed_options))
        asyncio.run_coroutine_threadsafe(run_command_on_file(parsed_options, file_path,
                                                             lambda text: self.logText.appendPlainText(text),
                                                             lambda status: subprocess.run(
                                                                 ['xdg-open', opt_file_path])),
                                         event_loop)
        self.tabWidget.setCurrentIndex(3)

    def device_changed(self, index):
        text = self.deviceComboBox.itemText(index)
        data = self.deviceComboBox.itemData(index, QtCore.Qt.UserRole)
        print('User chose {} which corresponds to {}'.format(text, data))
        self.options_json['-dev']['value'] = index
        self.options_json['-dev']['active'] = index != 0
        self.save_options_to_file()

    def option_line_edit_changed(self, option_name, option_value):
        print('Changing option {} to {}'.format(option_name, option_value))
        self.options_json[option_name]['value'] = option_value
        self.save_options_to_file()

    def get_margin_option_value(self):
        return '{}px,{}px,{}px,{}px'.format(self.options_json['-m']['left'], self.options_json['-m']['top'],
                                            self.options_json['-m']['right'], self.options_json['-m']['bottom'])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    window = MainWindow()
    window.show()
    app.exec_()
