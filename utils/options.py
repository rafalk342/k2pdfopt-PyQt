"""This module handles options."""
import json
from PyQt5 import QtCore


class Options:
    """This class handles options."""
    OPTIONS_FILENAME = "./options.json"
    OPTION_TYPE_TOGGLE = "TOGGLE"
    OPTION_TYPE_DEFAULT = "DEFAULT"
    OPTION_TYPE_MARGIN = "MARGIN"
    OPTION_TYPE_DEVICE = "DEVICE"

    def __init__(self, device_combo_box):
        self.options_json = json.load(open(self.OPTIONS_FILENAME))
        self.device_combo_box = device_combo_box

    def get_device_index(self):
        """Return selected device index."""
        return self.options_json['-dev']['value']

    def is_option_active(self, name):
        """Return if option with given name is turned on."""
        return self.options_json[name]['active']

    def get_option_value(self, name):
        """Return the value of option with given name."""
        return self.options_json[name]['value']

    def get_margin_value(self, side):
        """Return margin value for given side."""
        return self.options_json['-m'][side]

    def save_options_to_file(self):
        """Save options to json file."""
        with open(self.OPTIONS_FILENAME, 'w') as options_file:
            json.dump(self.options_json, options_file, indent=4)

    def change_margin_option(self, side, value):
        """Change margin option for given side."""
        self.options_json['-m'][side] = value
        self.save_options_to_file()

    def toggle_changed(self, checkbox, argument):
        """Handle toggle change."""
        if checkbox.isChecked():
            print('Toggle {} activated'.format(argument))
            self.options_json[argument]['active'] = True
        else:
            print('Toggle {} deactivated'.format(argument))
            self.options_json[argument]['active'] = False
        self.save_options_to_file()

    def get_parsed_options(self):
        """Return a list with parsed options."""
        parsed_options = []
        for option_name, option_dict in self.options_json.items():
            if option_dict['active']:
                if option_dict['type'] == self.OPTION_TYPE_TOGGLE:
                    parsed_options.append(option_name)
                elif option_dict['type'] == self.OPTION_TYPE_DEFAULT and option_dict['value']:
                    parsed_options.append(option_name)
                    parsed_options.append(option_dict['value'])
                elif option_dict['type'] == self.OPTION_TYPE_MARGIN:
                    parsed_options.append(option_name)
                    parsed_options.append(self.get_margin_option_value())
                elif option_dict['type'] == self.OPTION_TYPE_DEVICE:
                    parsed_options.append(option_name)
                    parsed_options.append(
                        self.device_combo_box.itemData(option_dict['value'], QtCore.Qt.UserRole))
        return parsed_options

    def get_margin_option_value(self):
        """Return formatted margin option."""
        return '{}px,{}px,{}px,{}px'.format(self.options_json['-m']['left'],
                                            self.options_json['-m']['top'],
                                            self.options_json['-m']['right'],
                                            self.options_json['-m']['bottom'])

    def set_device_index(self, index):
        """Set device index."""
        self.options_json['-dev']['value'] = index
        self.options_json['-dev']['active'] = index != 0
        self.save_options_to_file()

    def change_option_value(self, option_name, option_value):
        """Change option value."""
        print('Changing option {} to {}'.format(option_name, option_value))
        self.options_json[option_name]['value'] = option_value
        self.save_options_to_file()
