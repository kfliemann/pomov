from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from qfluentwidgets import *

class TimerGui():
    timerWidget = None

    def __init__(self, parent, appConfig_obj):
        self.parent = parent
        self.appConfig_obj_copy = appConfig_obj

        self.timerWidget = QWidget()
        self.timerWidget_layout = QVBoxLayout(self.timerWidget)

        self.timerWidget_layout.addWidget(self.init_timerRing())

    def init_timerRing(self):
        timerRing = ProgressRing()
        timerRing.setRange(0,int(self.appConfig_obj_copy.readSettings["timer"]))
        timerRing.setValue(int(self.appConfig_obj_copy.readSettings["timer"]))
        timerRing.setTextVisible(True)
        timerRing.setFixedSize(120, 120)
        timerRing.setStrokeWidth(5)
        timerRing.setFormat("%v \n minutes left")
        return timerRing