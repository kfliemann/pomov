from .titlebarGui import TitlebarGui
from .settingsGui import SettingsGui
from qframelesswindow import FramelessMainWindow
from PyQt6.QtWidgets import QStackedLayout, QWidget, QPushButton, QHBoxLayout


class AppGui(FramelessMainWindow):

    def __init__(self, appConfig_obj, parent=None):
        super().__init__(parent=parent)
        self.titlebarGui_obj = TitlebarGui()
        self.titlebarGui_obj.init_settings_button(self)

        #main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.main_layout = QStackedLayout(main_widget)

        #child widgets
        #TODO: replace this placeholder with actual content
        central_widget = QWidget()
        central_layout = QHBoxLayout(central_widget)
        central_layout.addWidget(QPushButton("Central Widget 2"))
        central_widget.setLayout(central_layout)

        self.settingsGui_obj = SettingsGui(self, appConfig_obj, self.titlebarGui_obj)


        self.main_layout.addWidget(central_widget)
        self.main_layout.addWidget(self.settingsGui_obj.settingsWidget)

        #titlebar.raise() needs to be called before show() in order to properly display titlebar
        self.titleBar.raise_()
        self.show()

    def setCurrentStack(self, layer):
        self.main_layout.setCurrentIndex(layer)

