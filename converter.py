import asyncio
import subprocess

from PyQt5.QtWidgets import QFileDialog

from utils import run_command_on_file


class Converter:
    def __init__(self, event_loop, log_text, options, tab_widget, input_file_line_edit):
        self.event_loop = event_loop
        self.log_text = log_text
        self.options = options
        self.tab_widget = tab_widget
        self.file_path_line_edit = input_file_line_edit

    def convert(self, opt_file_path):
        print('Output file path {}'.format(opt_file_path))
        parsed_options = self.options.get_parsed_options()
        parsed_options.append('-o {}'.format(opt_file_path))
        self.run_coroutine(parsed_options, lambda status: subprocess.run(['xdg-open', opt_file_path]))
        self.tab_widget.setCurrentIndex(3)

    def convert_preview_page(self, page_number, on_finish):
        self.log_text.clear()
        parsed_options = self.options.get_parsed_options()
        parsed_options.append('-bmp {}'.format(page_number))
        self.run_coroutine(parsed_options, on_finish)

    def run_coroutine(self, parsed_options, on_finish):
        self.log_text.clear()
        print('Converting file {}'.format(self.file_path_line_edit.text()))
        print('Parsed options {}'.format(parsed_options))
        asyncio.run_coroutine_threadsafe(run_command_on_file(parsed_options, self.file_path_line_edit.text(),
                                                             lambda text: self.log_text.appendPlainText(text),
                                                             on_finish),
                                         self.event_loop)
