from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from qfluentwidgets import *

class TitlebarGui():

    settings_open = False

    def init_settings_button(self, parent):
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
        self.settings_button.clicked.connect(lambda: self.settings_button_clicked(parent))
        parent.titleBar.layout().insertWidget(0, self.settings_button, 0, Qt.AlignmentFlag.AlignLeft)
        parent.titleBar.layout().insertSpacing(0,8)
        parent.titleBar.raise_()

    def settings_button_clicked(self, parent):
        if self.settings_open == False:
            self.settings_button.setIcon(FluentIcon.HOME)
            self.settings_open = True
            parent.setCurrentStack(1)
        else:
            self.settings_button.setIcon(FluentIcon.SETTING)
            self.settings_open = False
            parent.setCurrentStack(0)