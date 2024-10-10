from utils.iconOverwrite import IconOverwrite
from utils.timer import Timer
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QSize
from qfluentwidgets import *


class TimerGui():

    appConfig_obj_copy = None
    systemtrayGui_obj_copy = None
    timer_obj = None
    timer_running = None
    timerWidget = None
    timerring_height = 400
    timerring_width = 300


    def __init__(self, appConfig_obj, systemtrayGui_obj):
        self.appConfig_obj_copy = appConfig_obj
        self.systemtrayGui_obj_copy = systemtrayGui_obj

        self.timerWidget = QWidget()
        self.timerWidget_layout = QVBoxLayout(self.timerWidget)
        self.timerWidget_layout.setSpacing(30)
        self.timerWidget_layout.setContentsMargins(15,0,15,50)
        
        #button styling
        self.qss = 'PushButton{font-size: 18px;}'
        self.iconsize = QSize(18,18)

        self.timerWidget_layout.insertWidget(0, self.init_timerRing(), 0, Qt.AlignmentFlag.AlignCenter)
        self.timerWidget_layout.addWidget(self.init_startstop())
        self.timerWidget_layout.addWidget(self.init_restart())

        #add all widgets before timer thread gets created
        self.timer_obj = Timer(self, self.appConfig_obj_copy, self.systemtrayGui_obj_copy)
        if self.appConfig_obj_copy.readSettings["startonboot"]:
            self.timer_obj.timer_start()

    def init_timerRing(self):
        #progressring
        transformed_timer = self.appConfig_obj_copy.readSettings["timer"] * 60
        self.timerRing = ProgressRing()
        self.timerRing.setRange(0, transformed_timer)
        self.timerRing.setValue(transformed_timer)
        self.timerRing.setTextVisible(True)
        self.timerRing.setFixedSize(self.timerring_width, self.timerring_height)
        self.timerRing.setStrokeWidth(17)
        self.timerRing.setCustomBarColor(QColor(145,178,135),QColor(145,178,135))
        self.timerRing.setStyleSheet(f"""
            QProgressBar {{
                font-size: 25px;
                font-weight: 630;
            }}
        """)
        time_text = f"Timer: \n{self.appConfig_obj_copy.time_to_string(transformed_timer)}"
        self.timerRing.setFormat(time_text)
        return self.timerRing
    
    def init_startstop(self):
        #button
        self.timer_running = self.appConfig_obj_copy.readSettings["startonboot"] 
        if self.timer_running == True:
            self.startStopButton = PushButton(IconOverwrite.TIMER_OFF, 'Stop Timer')
        else:
            self.startStopButton = PushButton(IconOverwrite.TIMER_ON, 'Start Timer')
        setCustomStyleSheet(self.startStopButton, self.qss, self.qss)
        self.startStopButton.setIconSize(self.iconsize)

        self.startStopButton.clicked.connect(self.toggle_timer)
        return self.startStopButton
    
    def init_restart(self):
        #button
        restartButton = PushButton(IconOverwrite.RESTART, 'Restart Timer')
        setCustomStyleSheet(restartButton, self.qss, self.qss)
        restartButton.setIconSize(self.iconsize)
        restartButton.clicked.connect(self.restart_timer)
        return restartButton

    def toggle_timer(self):
        if self.timer_running == True:
            self.startStopButton.setIcon(IconOverwrite.TIMER_ON)
            self.startStopButton.setText("Start Timer")
            self.timer_running = False
            self.timer_obj.timer_pause()
        else:
            self.startStopButton.setIcon(IconOverwrite.TIMER_OFF)
            self.startStopButton.setText("Stop Timer")
            self.timer_running = True
            self.timer_obj.timer_start()
    
    def restart_timer(self):
        self.timer_obj.timer_stop()
        self.reset_ui()

    def resize_timerring(self, appGui_obj):
        aspect = self.timerring_width / self.timerring_height
        possible_h = appGui_obj.width() / aspect
        possible_w = appGui_obj.height() * aspect

        if possible_h <= appGui_obj.height():
            new_height = possible_h-200
            new_width = appGui_obj.width()-100
        else:
            new_height = appGui_obj.height()-200
            new_width = possible_w-100
        self.timerRing.setFixedSize(int(round(new_width)),int(round(new_height)))

    def update_timerring(self, type, newTime):
        match type:
            case "timer":
                time_text = f"Timer: \n{self.appConfig_obj_copy.time_to_string(newTime)}"
                self.timerRing.setCustomBarColor(QColor(145,178,135),QColor(145,178,135))
            case "pause":
                time_text = f"Break: \n{self.appConfig_obj_copy.time_to_string(newTime)}"
                self.timerRing.setCustomBarColor(QColor(231,162,58),QColor(231,162,58))
        self.timerRing.setVal(newTime)
        self.timerRing.setFormat(time_text)
        
    def update_timerring_range(self, newTime):
        self.timerRing.setRange(0, newTime)
        
    def reset_ui(self):
        self.timerRing.setRange(0, self.appConfig_obj_copy.readSettings["timer"])
        self.timerRing.setVal(self.appConfig_obj_copy.readSettings["timer"])
        self.timerRing.setCustomBarColor(QColor(145,178,135),QColor(145,178,135))
        time_text = f"Timer: \n{self.appConfig_obj_copy.time_to_string(self.appConfig_obj_copy.readSettings["timer"])}"
        self.timerRing.setFormat(time_text)
        self.startStopButton.setIcon(IconOverwrite.TIMER_ON)
        self.startStopButton.setText("Start Timer")
        self.timer_running = False
