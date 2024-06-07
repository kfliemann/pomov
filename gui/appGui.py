from .titlebarGui import TitlebarGui
from .timerGui import TimerGui
from .settingsGui import SettingsGui
from qframelesswindow import FramelessMainWindow
from PyQt6.QtWidgets import QStackedLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon
import ctypes


class AppGui(FramelessMainWindow):

    titlebarGui_obj = None
    timerGui_obj = None
    settingsGui_obj = None     


    def __init__(self, appConfig_obj, parent=None):
        super().__init__(parent=parent)

        self.appConfig_obj_copy = appConfig_obj

        #set window icon and name
        self.setWindowTitle("Pomov")
        self.setWindowIcon(QIcon(self.appConfig_obj_copy.appIconPath))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('kfliemann.pomov.1')
        
        #titlebar
        self.titlebarGui_obj = TitlebarGui()
        self.titlebarGui_obj.init_settings_button(self)

        #main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.main_layout = QStackedLayout(main_widget)

        #child widgets
        self.timerGui_obj = TimerGui(self.appConfig_obj_copy)
        self.settingsGui_obj = SettingsGui(self, self.appConfig_obj_copy, self.titlebarGui_obj)

        self.main_layout.addWidget(self.timerGui_obj.timerWidget)
        self.main_layout.addWidget(self.settingsGui_obj.settingsWidget)

        #titlebar.raise() needs to be called before show() in order to properly display titlebar
        self.titleBar.raise_()
        self.show()

    def setCurrentStack(self, layer):
        self.main_layout.setCurrentIndex(layer)

    def closeEvent(self, event):
        self.timerGui_obj.timer_obj.timer_exit()
        self.settingsGui_obj.audioplayer_obj.audioplayer_exit()
        event.accept()

