import sys
from .titlebarGui import TitlebarGui
from .timerGui import TimerGui
from .settingsGui import SettingsGui
from .systemtrayGui import SystemtrayGui
from .contactGui import ContactGui
from qframelesswindow import FramelessMainWindow
from qfluentwidgets import *
from PyQt6.QtWidgets import QStackedLayout, QWidget
from PyQt6.QtGui import QIcon
import ctypes

class AppGui(FramelessMainWindow):

    titlebarGui_obj = None
    timerGui_obj = None
    settingsGui_obj = None     
    systemtray_notice_shown = False
    window_width = 400
    window_height = 600


    def __init__(self, appConfig_obj, parent=None):
        super().__init__(parent=parent)

        self.appConfig_obj_copy = appConfig_obj

        #set window icon and name
        self.setWindowTitle("Pomov")
        self.setMinimumSize(self.window_width, self.window_height)
        self.resize(self.window_width, self.window_height)
        self.setWindowIcon(QIcon(self.appConfig_obj_copy.appIconPath))
        setThemeColor(QColor(73,175,213))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('KFliemann.Pomov.1')
        
        #titlebar
        self.titlebarGui_obj = TitlebarGui()
        self.titlebarGui_obj.init_settings_button(self)
        self.titleBar.minBtn.clicked.connect(self.minimizeWindow)

        #main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.main_layout = QStackedLayout(main_widget)
        
        #system tray
        self.systemtrayGui_obj = SystemtrayGui(self)
        self.systemtrayGui_obj.tray_icon.show() 

        #child widgets
        self.timerGui_obj = TimerGui(self.appConfig_obj_copy, self.systemtrayGui_obj)
        self.settingsGui_obj = SettingsGui(self, self.appConfig_obj_copy, self.titlebarGui_obj)
        self.contactGui_obj = ContactGui(self)

        self.main_layout.addWidget(self.timerGui_obj.timerWidget)
        self.main_layout.addWidget(self.settingsGui_obj.settingsWidget)
        self.main_layout.addWidget(self.contactGui_obj.contactWidget)

        #titlebar.raise() needs to be called before show() in order to properly display titlebar
        self.titleBar.raise_()
        self.show()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.titleBar.resize(self.width(), self.titleBar.height())
        self.timerGui_obj.resize_timerring(self)
        self.contactGui_obj.resize_logo(self)

    def setCurrentStack(self, layer):
        self.main_layout.setCurrentIndex(layer)

    def closeEvent(self, event):
        self.timerGui_obj.timer_obj.timer_exit()
        self.settingsGui_obj.audioplayer_obj.audioplayer_exit()
        event.accept()
        sys.exit()

    def minimizeWindow(self):
        if self.appConfig_obj_copy.readSettings["totaskbar"]:
            if self.timerGui_obj.timer_running:
                tray_message = "Pomov is running in the background"
            else:
                tray_message = "Pomov minimized to System Tray"
            if self.systemtray_notice_shown == False:
                self.systemtrayGui_obj.show_minimized_message(tray_message)
                self.systemtray_notice_shown = True
            #TODO: fix minimize button still being hovered after minimizing window
            #only happens when hiding the window, not minimizing
            self.hide()
            self.setVisible(False)
        else:
            self.showMinimized()
