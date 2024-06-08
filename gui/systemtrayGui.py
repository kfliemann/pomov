from PyQt6.QtWidgets import QStackedLayout, QWidget, QPushButton, QHBoxLayout, QSystemTrayIcon, QMenu, QLabel, QWidgetAction
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QSize, Qt, QEvent

class SystemtrayGui():

    appGui_obj_copy = None


    def __init__(self, appGui_obj):
        self.appGui_obj_copy = appGui_obj

        #system tray icon
        self.tray_icon = QSystemTrayIcon(self.appGui_obj_copy)
        self.tray_icon.setIcon(QIcon(self.appGui_obj_copy.appConfig_obj_copy.appIconPath))
        
        #menu is assigned to the tray icon
        self.tray_menu = QMenu()
        self.timer_label = QLabel(f"\nTimer: {self.appGui_obj_copy.appConfig_obj_copy.time_to_string(self.appGui_obj_copy.appConfig_obj_copy.readSettings['timer'])}\n")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_action = QWidgetAction(self.tray_menu)
        label_action.setDefaultWidget(self.timer_label)
        
        #tray icon on right click actions
        show_action = QAction("Open", self.appGui_obj_copy)
        close_action = QAction("Close", self.appGui_obj_copy)
        show_action.triggered.connect(self.appGui_obj_copy.showNormal)
        close_action.triggered.connect(self.appGui_obj_copy.close)
        
        self.tray_menu.addAction(label_action)
        self.tray_menu.addAction(show_action)
        self.tray_menu.addAction(close_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_clicked)

    def show_minimized_message(self, tray_message):
        self.tray_icon.showMessage(
            "Pomov",
            tray_message,
            QSystemTrayIcon.MessageIcon.Information,
            2000
        )

    def update_timer_label(self, type, newTime):
        match type:
            case "timer":
                time_text = f"\nTimer: {self.appGui_obj_copy.appConfig_obj_copy.time_to_string(newTime)}\n"
            case "pause":
                time_text = f"\nPause: {self.appGui_obj_copy.appConfig_obj_copy.time_to_string(newTime)}\n"
        self.timer_label.setText(time_text)

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.appGui_obj_copy.setVisible(True)
            self.appGui_obj_copy.showNormal()


