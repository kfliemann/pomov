from utils.iconOverwrite import IconOverwrite
from utils.timer import Timer
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import *


class TimerGui():

    appConfig_obj_copy = None
    timer_obj = None
    timer_running = None
    timerWidget = None


    def __init__(self, appConfig_obj):
        self.appConfig_obj_copy = appConfig_obj

        self.timerWidget = QWidget()
        self.timerWidget_layout = QVBoxLayout(self.timerWidget)

        self.timerWidget_layout.addWidget(self.init_timerRing())
        self.timerWidget_layout.addWidget(self.init_startstop())
        self.timerWidget_layout.addWidget(self.init_restart())

        #add all widgets before timer thread gets created
        self.timer_obj = Timer(self, self.appConfig_obj_copy)
        if self.appConfig_obj_copy.readSettings["startonboot"]:
            self.timer_obj.timer_start()

    def init_timerRing(self):
        #progressring
        self.timerRing = ProgressRing()
        self.timerRing.setRange(0, self.appConfig_obj_copy.readSettings["timer"])
        self.timerRing.setValue(self.appConfig_obj_copy.readSettings["timer"])
        self.timerRing.setTextVisible(True)
        self.timerRing.setFixedSize(120, 120)
        self.timerRing.setStrokeWidth(5)
        minutes, seconds = divmod(self.appConfig_obj_copy.readSettings["timer"],60)
        time_text = f"{minutes:02}:{seconds:02}\nminutes left"
        self.timerRing.setFormat(time_text)
        return self.timerRing
    
    def init_startstop(self):
        #button
        self.timer_running = self.appConfig_obj_copy.readSettings["startonboot"] 
        if self.timer_running == True:
            self.startStopButton = PushButton(IconOverwrite.TIMER_OFF, 'Stop Timer')
        else:
            self.startStopButton = PushButton(IconOverwrite.TIMER_ON, 'Start Timer')
        
        self.startStopButton.clicked.connect(self.toggle_timer)
        return self.startStopButton
    
    def init_restart(self):
        #button
        restartButton = PushButton(IconOverwrite.RESTART, 'Restart current Timer')
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

    def update_timerring_label(self, type, newTime):
        minutes, seconds = divmod(newTime, 60)
        match type:
            case "timer":
                time_text = f"{minutes:02}:{seconds:02}\nminutes left timer"
            case "pause":
                time_text = f"{minutes:02}:{seconds:02}\nminutes left pause"
        self.timerRing.setVal(newTime)
        self.timerRing.setFormat(time_text)
        
    def update_timerring_range(self, newTime):
        self.timerRing.setRange(0, newTime)
        
    def reset_ui(self):
        self.timerRing.setRange(0, self.appConfig_obj_copy.readSettings["timer"])
        self.timerRing.setVal(self.appConfig_obj_copy.readSettings["timer"])
        minutes, seconds = divmod(self.appConfig_obj_copy.readSettings["timer"], 60)
        time_text = f"{minutes:02}:{seconds:02}\nminutes left timer"
        self.timerRing.setFormat(time_text)
        self.startStopButton.setIcon(IconOverwrite.TIMER_ON)
        self.startStopButton.setText("Start Timer")
        self.timer_running = False
