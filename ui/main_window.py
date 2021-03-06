# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setGeometry(QtCore.QRect(0, 0, 986, 753))
        main_window.setMaximumSize(QtCore.QSize(986, 753))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.basicInputWidget = QtWidgets.QWidget(self.tab)
        self.basicInputWidget.setGeometry(QtCore.QRect(10, 10, 331, 151))
        self.basicInputWidget.setObjectName("basicInputWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.basicInputWidget)
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputFilePath = QtWidgets.QLineEdit(self.basicInputWidget)
        self.inputFilePath.setReadOnly(True)
        self.inputFilePath.setObjectName("inputFilePath")
        self.horizontalLayout.addWidget(self.inputFilePath)
        self.choose_file_button = QtWidgets.QPushButton(self.basicInputWidget)
        self.choose_file_button.setObjectName("choose_file_button")
        self.horizontalLayout.addWidget(self.choose_file_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deviceLabel = QtWidgets.QLabel(self.basicInputWidget)
        self.deviceLabel.setObjectName("deviceLabel")
        self.horizontalLayout_2.addWidget(self.deviceLabel)
        self.device_combo_box = QtWidgets.QComboBox(self.basicInputWidget)
        self.device_combo_box.setObjectName("device_combo_box")
        self.horizontalLayout_2.addWidget(self.device_combo_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.convertFileButton = QtWidgets.QPushButton(self.basicInputWidget)
        self.convertFileButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.convertFileButton.setObjectName("convertFileButton")
        self.verticalLayout_3.addWidget(self.convertFileButton, 0, QtCore.Qt.AlignHCenter)
        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tooglesWidget = QtWidgets.QWidget(self.tab_2)
        self.tooglesWidget.setGeometry(QtCore.QRect(10, 10, 361, 421))
        self.tooglesWidget.setObjectName("tooglesWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tooglesWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.autostraighten_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.autostraighten_check_box.setObjectName("autostraighten_check_box")
        self.verticalLayout_4.addWidget(self.autostraighten_check_box)
        self.break_after_each_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.break_after_each_check_box.setObjectName("break_after_each_check_box")
        self.verticalLayout_4.addWidget(self.break_after_each_check_box)
        self.color_output_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.color_output_check_box.setObjectName("color_output_check_box")
        self.verticalLayout_4.addWidget(self.color_output_check_box)
        self.landscape_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.landscape_check_box.setObjectName("landscape_check_box")
        self.verticalLayout_4.addWidget(self.landscape_check_box)
        self.native_PDF_output_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.native_PDF_output_check_box.setObjectName("native_PDF_output_check_box")
        self.verticalLayout_4.addWidget(self.native_PDF_output_check_box)
        self.right_to_left_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.right_to_left_check_box.setObjectName("right_to_left_check_box")
        self.verticalLayout_4.addWidget(self.right_to_left_check_box)
        self.generate_marked_up_source_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.generate_marked_up_source_check_box.setObjectName("generate_marked_up_source_check_box")
        self.verticalLayout_4.addWidget(self.generate_marked_up_source_check_box)
        self.re_flow_text_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.re_flow_text_check_box.setObjectName("re_flow_text_check_box")
        self.verticalLayout_4.addWidget(self.re_flow_text_check_box)
        self.erase_vertical_lines_check_box = QtWidgets.QCheckBox(self.tooglesWidget)
        self.erase_vertical_lines_check_box.setObjectName("erase_vertical_lines_check_box")
        self.verticalLayout_4.addWidget(self.erase_vertical_lines_check_box)
        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.parametersWidget = QtWidgets.QWidget(self.tab_3)
        self.parametersWidget.setGeometry(QtCore.QRect(10, 10, 451, 391))
        self.parametersWidget.setObjectName("parametersWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.parametersWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.max_columns_check_box = QtWidgets.QCheckBox(self.parametersWidget)
        self.max_columns_check_box.setObjectName("max_columns_check_box")
        self.horizontalLayout_3.addWidget(self.max_columns_check_box)
        self.max_columns_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.max_columns_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.max_columns_line_edit.setObjectName("max_columns_line_edit")
        self.horizontalLayout_3.addWidget(self.max_columns_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.resolution_factor_check_box = QtWidgets.QCheckBox(self.parametersWidget)
        self.resolution_factor_check_box.setObjectName("resolution_factor_check_box")
        self.horizontalLayout_4.addWidget(self.resolution_factor_check_box)
        self.resolution_factor_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.resolution_factor_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.resolution_factor_line_edit.setObjectName("resolution_factor_line_edit")
        self.horizontalLayout_4.addWidget(self.resolution_factor_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.crop_margin_check_box = QtWidgets.QCheckBox(self.parametersWidget)
        self.crop_margin_check_box.setObjectName("crop_margin_check_box")
        self.verticalLayout_2.addWidget(self.crop_margin_check_box)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.parametersWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.left_margin_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.left_margin_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.left_margin_line_edit.setObjectName("left_margin_line_edit")
        self.horizontalLayout_5.addWidget(self.left_margin_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.parametersWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.right_margin_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.right_margin_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.right_margin_line_edit.setObjectName("right_margin_line_edit")
        self.horizontalLayout_6.addWidget(self.right_margin_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.parametersWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.top_margin_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.top_margin_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_margin_line_edit.setObjectName("top_margin_line_edit")
        self.horizontalLayout_7.addWidget(self.top_margin_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.parametersWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.bottom_margin_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.bottom_margin_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bottom_margin_line_edit.setObjectName("bottom_margin_line_edit")
        self.horizontalLayout_8.addWidget(self.bottom_margin_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.parametersWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.page_range_line_edit = QtWidgets.QLineEdit(self.parametersWidget)
        self.page_range_line_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.page_range_line_edit.setObjectName("page_range_line_edit")
        self.horizontalLayout_9.addWidget(self.page_range_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.tab_widget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logText = QtWidgets.QPlainTextEdit(self.tab_4)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.verticalLayout_5.addWidget(self.logText)
        self.tab_widget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.preview_line_edit = QtWidgets.QLineEdit(self.tab_5)
        self.preview_line_edit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.preview_line_edit.setObjectName("preview_line_edit")
        self.verticalLayout_8.addWidget(self.preview_line_edit)
        self.preview_button = QtWidgets.QPushButton(self.tab_5)
        self.preview_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.preview_button.setObjectName("preview_button")
        self.verticalLayout_8.addWidget(self.preview_button)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 944, 578))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.image_preview = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image_preview.setText("")
        self.image_preview.setObjectName("image_preview")
        self.verticalLayout_6.addWidget(self.image_preview)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.tab_widget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tab_widget)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 22))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        self.tab_widget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputFilePath.setPlaceholderText(_translate("MainWindow", "File path"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.deviceLabel.setText(_translate("MainWindow", "Device:"))
        self.convertFileButton.setText(_translate("MainWindow", "Convert"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.autostraighten_check_box.setText(_translate("MainWindow", "Autostraighten"))
        self.break_after_each_check_box.setText(_translate("MainWindow", "Break pages after each source page"))
        self.color_output_check_box.setText(_translate("MainWindow", "Color output"))
        self.landscape_check_box.setText(_translate("MainWindow", "Rotate output to landscape"))
        self.native_PDF_output_check_box.setText(_translate("MainWindow", "Native PDF output"))
        self.right_to_left_check_box.setText(_translate("MainWindow", "Right to left text"))
        self.generate_marked_up_source_check_box.setText(_translate("MainWindow", "Generate marked-up source"))
        self.re_flow_text_check_box.setText(_translate("MainWindow", "Re-flow text"))
        self.erase_vertical_lines_check_box.setText(_translate("MainWindow", "Erase vertical lines"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), _translate("MainWindow", "Toggles"))
        self.max_columns_check_box.setText(_translate("MainWindow", "Max columns"))
        self.max_columns_line_edit.setText(_translate("MainWindow", "2"))
        self.resolution_factor_check_box.setText(_translate("MainWindow", "Document resolution factor:"))
        self.resolution_factor_line_edit.setText(_translate("MainWindow", "1.0"))
        self.crop_margin_check_box.setText(_translate("MainWindow", "Crop margins:"))
        self.label.setText(_translate("MainWindow", "Left margin:"))
        self.left_margin_line_edit.setText(_translate("MainWindow", "0.00"))
        self.label_2.setText(_translate("MainWindow", "Right margin:"))
        self.right_margin_line_edit.setText(_translate("MainWindow", "0.00"))
        self.label_3.setText(_translate("MainWindow", "Top margin:"))
        self.top_margin_line_edit.setText(_translate("MainWindow", "0.00"))
        self.label_4.setText(_translate("MainWindow", "Bottom margin:"))
        self.bottom_margin_line_edit.setText(_translate("MainWindow", "0.00"))
        self.label_5.setText(_translate("MainWindow", "Page range:"))
        self.page_range_line_edit.setPlaceholderText(_translate("MainWindow", "(e.g. 1-5,6,9-)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), _translate("MainWindow", "Options"))
        self.logText.setPlaceholderText(_translate("MainWindow", "Log output..."))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), _translate("MainWindow", "Log"))
        self.preview_line_edit.setPlaceholderText(_translate("MainWindow", "Output page..."))
        self.preview_button.setText(_translate("MainWindow", "Preview"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_5), _translate("MainWindow", "Preview"))
