"""This module takes all parsed options and runs a subprocess to convert the file."""
import asyncio
import re
import subprocess

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


async def run_command_on_file(options, file_path, callback_change, callback_finish):
    """Run subprocess in the background and call callback on every new stdout line."""
    cmd = 'k2pdfopt -ui- -x {} {}'.format(' '.join(options), file_path)
    print('Running command {}'.format(cmd))
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    while True:
        line = await proc.stdout.readline()
        if line:
            decoded_line = ansi_escape.sub('', line.decode()).strip()
            print(decoded_line)
            callback_change(decoded_line)
        else:
            await proc.communicate()
            print('Return code {}'.format(proc.returncode))
            callback_finish(proc.returncode)
            break


class Converter:
    """This class takes all parsed options and runs a subprocess to convert the file."""
    def __init__(self, event_loop, log_text, options, input_file_line_edit):
        self.event_loop = event_loop
        self.log_text = log_text
        self.options = options
        self.file_path_line_edit = input_file_line_edit

    def convert(self, opt_file_path):
        """Run a conversion coroutine and open file at the end."""
        print('Output file path {}'.format(opt_file_path))
        parsed_options = self.options.get_parsed_options()
        parsed_options.append('-o {}'.format(opt_file_path))
        self.run_coroutine(parsed_options,
                           lambda status: subprocess.run(['xdg-open', opt_file_path], check=False))

    def convert_preview_page(self, page_number, on_finish):
        """Create a preview page."""
        self.log_text.clear()
        parsed_options = self.options.get_parsed_options()
        parsed_options.append('-bmp {}'.format(page_number))
        self.run_coroutine(parsed_options, on_finish)

    def run_coroutine(self, parsed_options, on_finish):
        """Run a coroutine in the background."""
        self.log_text.clear()
        print('Converting file {}'.format(self.file_path_line_edit.text()))
        print('Parsed options {}'.format(parsed_options))
        asyncio.run_coroutine_threadsafe(
            run_command_on_file(parsed_options, self.file_path_line_edit.text(),
                                self.log_text.appendPlainText,
                                on_finish),
            self.event_loop)
