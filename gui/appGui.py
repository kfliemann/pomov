import sys
from .titlebarGui import TitlebarGui
from .timerGui import TimerGui
from .settingsGui import SettingsGui
from .systemtrayGui import SystemtrayGui
from qframelesswindow import FramelessMainWindow
from PyQt6.QtWidgets import QStackedLayout, QWidget
from PyQt6.QtGui import QIcon
import ctypes

class AppGui(FramelessMainWindow):

    titlebarGui_obj = None
    timerGui_obj = None
    settingsGui_obj = None     
    systemtray_notice_shown = False


    def __init__(self, appConfig_obj, parent=None):
        super().__init__(parent=parent)

        self.appConfig_obj_copy = appConfig_obj

        #set window icon and name
        self.setWindowTitle("Pomov")
        self.setWindowIcon(QIcon(self.appConfig_obj_copy.appIconPath))
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
