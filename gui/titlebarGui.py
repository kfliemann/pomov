from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from qfluentwidgets import *


class TitlebarGui():

    appGui_obj_copy = None
    settings_open = False


    def init_settings_button(self, appGui_obj):
        self.appGui_obj_copy = appGui_obj

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
        self.appGui_obj_copy.titleBar.layout().insertWidget(0, self.settings_button, 0, Qt.AlignmentFlag.AlignLeft)
        self.appGui_obj_copy.titleBar.layout().insertSpacing(0,8)
        self.appGui_obj_copy.titleBar.raise_()

    def settings_button_clicked(self):
        if self.settings_open == False:
            self.settings_button.setIcon(FluentIcon.HOME)
            self.settings_open = True
            self.appGui_obj_copy.setCurrentStack(1)
        else:
            self.settings_button.setIcon(FluentIcon.SETTING)
            self.settings_open = False
            if self.appGui_obj_copy.settingsGui_obj.audioplayer_obj.currently_playing:
                self.appGui_obj_copy.settingsGui_obj.closeSettings()
            self.appGui_obj_copy.setCurrentStack(0)