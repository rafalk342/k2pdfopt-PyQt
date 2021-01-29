from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

from Options import Options


class Preview:
    PATH = './k2pdfopt_out.png'

    def generate_preview(self):
        image = QPixmap(self.PATH)
        return image
