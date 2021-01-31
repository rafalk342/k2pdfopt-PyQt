"""This module is a top level GUI controller."""
import asyncio
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog
from qasync import QEventLoop  # type: ignore

from ui.main_window import Ui_MainWindow
from models.device_combo_box_model import DeviceComboBoxModel
from utils.options import Options
from utils.preview import Preview
from utils.converter import Converter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """This class is a top level window of application."""

    def __init__(self, event_loop: QEventLoop):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.options = Options(self.device_combo_box)
        self.converter = Converter(event_loop, self.logText, self.options, self.inputFilePath)
        self.preview = Preview(self.converter, self.image_preview, self.preview_line_edit)
        self.set_up_toggles()
        self.set_up_options()
        self.set_up_margin_option()
        self.choose_file_button.pressed.connect(self.choose_file)
        self.convertFileButton.pressed.connect(self.convert)
        self.device_combo_box.setModel(DeviceComboBoxModel())
        self.device_combo_box.setCurrentIndex(self.options.get_device_index())
        self.device_combo_box.activated.connect(self.device_changed)
        self.tab_widget.setCurrentIndex(0)
        self.preview_button.clicked.connect(self.preview.handle_preview_button_clicked)
        self.set_up_validators()

    def set_up_toggles(self):
        """Set up toggles states and connect on change functions."""
        toggles_map = {
            '-as': self.autostraighten_check_box,
            '-bp': self.break_after_each_check_box,
            '-c': self.color_output_check_box,
            '-ls': self.landscape_check_box,
            '-n': self.native_PDF_output_check_box,
            '-r': self.right_to_left_check_box,
            '-sm': self.generate_marked_up_source_check_box,
            '-wrap': self.re_flow_text_check_box,
            '-evl 1': self.erase_vertical_lines_check_box
        }
        for name, checkbox in toggles_map.items():
            checkbox.setChecked(self.options.is_option_active(name))
            checkbox.stateChanged.connect(
                lambda checked, name=name, checkbox=checkbox: self.options.toggle_changed(checkbox,
                                                                                          name))

    def set_up_options(self):
        """Set up options with input field."""
        options_map = {
            '-col': {'checkbox': self.max_columns_check_box,
                     'line_edit': self.max_columns_line_edit},
            '-dr': {'checkbox': self.resolution_factor_check_box,
                    'line_edit': self.resolution_factor_line_edit},
            '-p': {'checkbox': None, 'line_edit': self.page_range_line_edit}
        }
        for option_name, option_dict in options_map.items():
            checkbox = option_dict['checkbox']
            line_edit = option_dict['line_edit']
            if checkbox:
                checkbox.setChecked(self.options.is_option_active(option_name))
                checkbox.stateChanged.connect(
                    lambda checked, option_name=option_name,
                           checkbox=checkbox: self.options.toggle_changed(checkbox,
                                                                          option_name))
            line_edit.setText(self.options.get_option_value(option_name))
            line_edit.textChanged.connect(
                lambda text, option_name=option_name: self.options.change_option_value(option_name,
                                                                                       text))

    def set_up_margin_option(self):
        """Set up margin option."""
        self.crop_margin_check_box.setChecked(self.options.is_option_active('-m'))
        self.left_margin_line_edit.setText(self.options.get_margin_value('left'))
        self.top_margin_line_edit.setText(self.options.get_margin_value('top'))
        self.right_margin_line_edit.setText(self.options.get_margin_value('right'))
        self.bottom_margin_line_edit.setText(self.options.get_margin_value('bottom'))
        self.crop_margin_check_box.stateChanged.connect(
            lambda: self.options.toggle_changed(self.crop_margin_check_box, '-m'))
        self.left_margin_line_edit.textChanged.connect(
            lambda text: self.options.change_margin_option('left', text))
        self.top_margin_line_edit.textChanged.connect(
            lambda text: self.options.change_margin_option('top', text))
        self.right_margin_line_edit.textChanged.connect(
            lambda text: self.options.change_margin_option('right', text))
        self.bottom_margin_line_edit.textChanged.connect(
            lambda text: self.options.change_margin_option('bottom', text))

    def set_up_validators(self):
        """Set up validators for input fields."""
        reg_exp_whole_number = QRegExp(r'\d*')
        whole_number_inputs = [self.max_columns_line_edit, self.left_margin_line_edit,
                               self.top_margin_line_edit,
                               self.right_margin_line_edit, self.bottom_margin_line_edit,
                               self.preview_line_edit]
        for line_edit in whole_number_inputs:
            line_edit_validator = QRegExpValidator(reg_exp_whole_number, line_edit)
            line_edit.setValidator(line_edit_validator)

        reg_exp_float = QRegExp(r'[0-9]+.?[0-9]+')
        resolution_factor_validator = QRegExpValidator(reg_exp_float,
                                                       self.resolution_factor_line_edit)
        self.resolution_factor_line_edit.setValidator(resolution_factor_validator)

        reg_exp_page_range = QRegExp(r'\d+-?\d*')
        page_range_validator = QRegExpValidator(reg_exp_page_range, self.page_range_line_edit)
        self.page_range_line_edit.setValidator(page_range_validator)

    def choose_file(self):
        """Allow user to choose file to be converted."""
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', './',
                                                   "PDF/DjVu files (*.pdf *.djvu)")
        self.inputFilePath.setText(file_path)

    def device_changed(self, index: int):
        """Handle event when device is changed."""
        text = self.device_combo_box.itemText(index)
        data = self.device_combo_box.itemData(index, QtCore.Qt.UserRole)
        print('User chose {} which corresponds to {}'.format(text, data))
        self.options.set_device_index(index)

    def convert(self):
        """Allow user to choose save file path and trigger a convert process."""
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', './',
                                                   "PDF/DjVu files (*.pdf *.djvu)")
        self.converter.convert(file_path)
        self.tab_widget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app_event_loop = QEventLoop(app)
    asyncio.set_event_loop(app_event_loop)
    window = MainWindow(app_event_loop)
    window.show()
    app.exec_()
