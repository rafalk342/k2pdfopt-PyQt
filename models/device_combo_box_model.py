"""This module provides a model for device combo box."""
from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class DeviceComboBoxModel(QStandardItemModel):
    """A model for device combo box."""
    def __init__(self):
        super().__init__(0, 1)
        devices = [('Select device', ''),
                   ('Kindle 1-5', 'k2'),
                   ('Kindle DX', 'dx'),
                   ('Kindle Paperwhite', 'kpw'),
                   ('Kindle Paperwhite 2', 'kp2'),
                   ('Kindle Paperwhite 3', 'kp3'),
                   ('Kindle Voyage/PW3+/Oasis', 'kv'),
                   ('Kindle Oasis 2', 'ko2'),
                   ('Pocketbook Basic 2', 'pb2'),
                   ('Nook Simple Touch', 'nookst'),
                   ('Kobo Touch', 'kbt'),
                   ('Kobo Glo', 'kbg'),
                   ('Kobo Glo HD', 'kghd'),
                   ('Kobo Glo HD Full Screen', 'kghdfs'),
                   ('Kobo Mini', 'kbm'),
                   ('Kobo Aura', 'kba'),
                   ('Kobo Aura HD', 'kbhd'),
                   ('Kobo H2O', 'kbh2o'),
                   ('Kobo H2O Full Screen', 'kbh2ofs'),
                   ('Kobo Aura One', 'kao'),
                   ('Nexus 7', 'nex7')]
        for text, data in devices:
            item = QStandardItem(text)
            item.setData(data, QtCore.Qt.UserRole)
            self.appendRow(item)
