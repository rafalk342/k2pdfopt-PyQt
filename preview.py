from PyQt5.QtGui import QPixmap


class Preview:
    PATH = './k2pdfopt_out.png'

    def __init__(self, converter, image_preview, preview_line_edit):
        self.converter = converter
        self.image_preview = image_preview
        self.preview_line_edit = preview_line_edit

    def generate_preview(self):
        image = QPixmap(self.PATH)
        return image

    def handle_preview_button_clicked(self):
        page = self.preview_line_edit.text()
        self.image_preview.setText('Loading preview...')
        self.converter.convert_preview_page(page, lambda status: self.image_preview.setPixmap(
            self.generate_preview()))
