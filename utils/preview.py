"""Controller for preview tab."""
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit

from utils.converter import Converter


class Preview:
    """Controller for preview tab."""

    PATH = './k2pdfopt_out.png'

    def __init__(self, converter: Converter, image_preview: QLabel, preview_line_edit: QLineEdit):
        self.converter = converter
        self.image_preview = image_preview
        self.preview_line_edit = preview_line_edit

    def set_up_preview(self):
        """Set up image generated under PATH."""
        image = QPixmap(self.PATH)
        self.image_preview.setPixmap(image)

    def handle_preview_button_clicked(self):
        """Handle preview button click."""
        page = self.preview_line_edit.text()
        self.image_preview.setText('Loading preview...')
        self.converter.convert_preview_page(page, lambda status: self.set_up_preview())
