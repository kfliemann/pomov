from img.iconOverwrite import IconOverwrite
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import *

class TimerGui():
    timerWidget = None

    def __init__(self, parent, appConfig_obj):
        self.parent = parent
        self.appConfig_obj_copy = appConfig_obj

        self.timerWidget = QWidget()
        self.timerWidget_layout = QVBoxLayout(self.timerWidget)

        self.timerWidget_layout.addWidget(self.init_timerRing())
        self.timerWidget_layout.addWidget(self.init_startstop())
        self.timerWidget_layout.addWidget(self.init_restart())

    def init_timerRing(self):
        #progressring
        timerRing = ProgressRing()
        timerRing.setRange(0,int(self.appConfig_obj_copy.readSettings["timer"]))
        timerRing.setValue(int(self.appConfig_obj_copy.readSettings["timer"]))
        timerRing.setTextVisible(True)
        timerRing.setFixedSize(120, 120)
        timerRing.setStrokeWidth(5)
        timerRing.setFormat("%v \n minutes left")
        return timerRing
    
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
            print("todo timer logic")
        else:
            self.startStopButton.setIcon(IconOverwrite.TIMER_OFF)
            self.startStopButton.setText("Stop Timer")
            self.timer_running = True
            print("todo timer logic")
    
    def restart_timer(self):
        print("todo restarting timer")