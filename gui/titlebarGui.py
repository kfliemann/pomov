from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from qfluentwidgets import *


class TitlebarGui():

    appGui_obj_copy = None
    settings_open = False
    contact_open = False


    def init_settings_button(self, appGui_obj):
        self.appGui_obj_copy = appGui_obj

        #titlebar buttons
        self.settings_button = TransparentToolButton(FluentIcon.SETTING)
        self.settings_button.clicked.connect(self.settings_button_clicked)

        self.contact_button = TransparentToolButton(FluentIcon.INFO)
        self.contact_button.clicked.connect(self.contact_button_clicked)
        
        #titlebar widget
        self.titlebar_child = QWidget()
        self.titlebar_child_layout = QHBoxLayout(self.titlebar_child)

        #button styling
        qss = '''
        TransparentToolButton {
            border-radius: 10px;
        }
        TransparentToolButton:hover {
            background-color: rgb(216,216,216);
        }
        '''
        setCustomStyleSheet(self.settings_button, qss, qss)
        setCustomStyleSheet(self.contact_button, qss, qss)
        self.contact_button.hide()
        
        #titlebar widget styling
        self.titlebar_child_layout.insertWidget(0, self.settings_button, 0, Qt.AlignmentFlag.AlignLeft)
        self.titlebar_child_layout.insertWidget(1, self.contact_button, 0, Qt.AlignmentFlag.AlignLeft)
        self.titlebar_child_layout.setSpacing(10)
        self.titlebar_child_layout.setContentsMargins(10,0,10,0)

        self.appGui_obj_copy.titleBar.layout().insertWidget(0,self.titlebar_child, 0, Qt.AlignmentFlag.AlignLeft)
        self.appGui_obj_copy.titleBar.raise_()

    def settings_button_clicked(self):
        if self.settings_open == False:
            self.settings_button.setIcon(FluentIcon.HOME)
            self.contact_button.show()
            self.settings_open = True
            self.contact_open = False
            self.appGui_obj_copy.setCurrentStack(1)
        else:
            self.settings_button.setIcon(FluentIcon.SETTING)
            self.contact_button.hide()
            self.settings_open = False
            self.contact_open = False
            if self.appGui_obj_copy.settingsGui_obj.audioplayer_obj.currently_playing:
                self.appGui_obj_copy.settingsGui_obj.closeSettings()
            self.appGui_obj_copy.setCurrentStack(0)

    def contact_button_clicked(self):
        if self.contact_open:
            self.appGui_obj_copy.setCurrentStack(1)
            self.contact_open = False
        else:
            self.appGui_obj_copy.setCurrentStack(2) 
            self.contact_open = True            