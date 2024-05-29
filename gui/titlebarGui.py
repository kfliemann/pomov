from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from qfluentwidgets import *

class titlebarGui():

    settings_open = False

    def init_settings_button(self, titleBar):
        self.settings_button = TransparentToolButton(FluentIcon.SETTING)
        qss = '''
        TransparentToolButton {
            border-radius: 10px;
        }
        TransparentToolButton:hover {
            background-color: rgb(216,216,216);
        }
        '''
        setCustomStyleSheet(self.settings_button, qss, qss)
        self.settings_button.clicked.connect(self.settings_button_clicked)
        titleBar.layout().insertWidget(0, self.settings_button, 0, Qt.AlignmentFlag.AlignLeft)
        titleBar.layout().insertSpacing(0,8)
        titleBar.raise_()

    def settings_button_clicked(self):
        if self.settings_open == False:
            self.settings_button.setIcon(FluentIcon.HOME)
            self.settings_open = True
        else:
            self.settings_button.setIcon(FluentIcon.SETTING)
            self.settings_open = False
