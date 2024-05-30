from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from qfluentwidgets import *

class SettingsGui():
    settingsWidget = None

    def __init__(self, parent, appConfig_obj):
        self.parent = parent
        self.appConfig_obj_copy = appConfig_obj

        self.settingsWidget = QWidget()
        self.settingsWidget_layout = QVBoxLayout(self.settingsWidget)

        #setting elements
        self.settingsWidget_layout.addWidget(self.init_timer())
        self.settingsWidget_layout.addWidget(self.init_pauseTimer())
        self.settingsWidget_layout.addWidget(self.init_autorestart())
        self.settingsWidget_layout.addWidget(self.init_openonboot())
        self.settingsWidget_layout.addWidget(self.init_startonboot())
        self.settingsWidget_layout.addWidget(self.init_totaskbar())
        self.settingsWidget_layout.addWidget(self.init_volume())
        self.settingsWidget_layout.addWidget(self.init_saveSettings())
    
    def init_timer(self):
        #widget
        timerRowWidget = QWidget()
        timerRowWidget_layout = QHBoxLayout(timerRowWidget)
        
        #label
        timer_label = BodyLabel("Timer")
        
        #lineedit
        timer_lineEdit = LineEdit()
        timer_lineEdit.setPlaceholderText("Minutes")
        timer_lineEdit.setText(self.appConfig_obj_copy.readSettings["timer"])
        timer_lineEdit.textEdited.connect(lambda: self.changeSettingsValue("timer", timer_lineEdit.text()))

        timerRowWidget_layout.addWidget(timer_label)
        timerRowWidget_layout.addWidget(timer_lineEdit)
        return timerRowWidget
    
    def init_pauseTimer(self):
        #widget
        pauseTimerRowWidget = QWidget()
        pauseTimerRowWidget_layout = QHBoxLayout(pauseTimerRowWidget)
        
        #label
        pauseTimer_label = BodyLabel("Pause")
        
        #lineedit
        pauseTimer_lineEdit = LineEdit()
        pauseTimer_lineEdit.setPlaceholderText("Minutes")
        pauseTimer_lineEdit.setText(self.appConfig_obj_copy.readSettings["pausetimer"])
        pauseTimer_lineEdit.textEdited.connect(lambda: self.changeSettingsValue("timer", pauseTimer_lineEdit.text()))

        pauseTimerRowWidget_layout.addWidget(pauseTimer_label)
        pauseTimerRowWidget_layout.addWidget(pauseTimer_lineEdit)
        return pauseTimerRowWidget
    
    def init_autorestart(self):
        #checkbox
        autostartCheckbox = CheckBox("autorestart")
        autostartCheckbox.setChecked(self.appConfig_obj_copy.readSettings["autorestart"])
        autostartCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("autorestart", autostartCheckbox.isChecked()))
        return autostartCheckbox
    
    def init_openonboot(self):
        #checkbox
        openonbootCheckbox = CheckBox("openonboot")
        openonbootCheckbox.setChecked(self.appConfig_obj_copy.readSettings["openonboot"])
        openonbootCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("openonboot", openonbootCheckbox.isChecked()))
        return openonbootCheckbox 
    
    def init_startonboot(self):
        #checkbox
        startonbootCheckbox = CheckBox("startonboot")
        startonbootCheckbox.setChecked(self.appConfig_obj_copy.readSettings["startonboot"])
        startonbootCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("startonboot", startonbootCheckbox.isChecked()))
        return startonbootCheckbox
    
    def init_totaskbar(self):
        #checkbox
        totaskbarCheckbox = CheckBox("totaskbar")
        totaskbarCheckbox.setChecked(self.appConfig_obj_copy.readSettings["totaskbar"])
        totaskbarCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("totaskbar", totaskbarCheckbox.isChecked()))
        return totaskbarCheckbox
    
    def init_volume(self):
        #widget
        volumeRowWidget = QWidget()
        volumeRowWidget_layout = QHBoxLayout(volumeRowWidget)

        #slider
        volumeSlider = Slider(Qt.Orientation.Horizontal)
        volumeSlider.setRange(0, 100)
        volumeSlider.setValue(int(self.appConfig_obj_copy.readSettings["volume"]))
        volumeSlider.valueChanged.connect(lambda: self.volume_changed(volumeSlider.value()))
        
        #label
        self.timer_label = BodyLabel(str(volumeSlider.value()))
        qss = '''
        BodyLabel {
            padding-bottom: 1px;
        }
        '''
        setCustomStyleSheet(self.timer_label, qss, qss)

        #preview play/pause toggle button
        self.playButton_toggled = False
        self.playToggleButton = ToolButton(FluentIcon.PLAY)
        qss = '''
        ToolButton {
            width: 9px;
            height: 9px;
        }
        '''
        setCustomStyleSheet(self.playToggleButton, qss, qss)
        self.playToggleButton.clicked.connect(lambda: self.playToggleButton_clicked())
        
        volumeRowWidget_layout.addWidget(volumeSlider)
        volumeRowWidget_layout.addWidget(self.timer_label)
        volumeRowWidget_layout.addWidget(self.playToggleButton)
        return volumeRowWidget
    
    def init_saveSettings(self):
        #button
        saveSettingsButton = PushButton(FluentIcon.SAVE, 'Save Settings')
        saveSettingsButton.clicked.connect(lambda: self.saveSettings())
        return saveSettingsButton
    


    #helper function section
    
    def volume_changed(self, currentVol):
        self.timer_label.setText(str(currentVol))
        self.appConfig_obj_copy.readSettings["volume"] = currentVol
        
    def playToggleButton_clicked(self):
        if self.playButton_toggled == False:
            self.playToggleButton.setIcon(FluentIcon.PAUSE)
            self.playButton_toggled = True
        else:
            self.playToggleButton.setIcon(FluentIcon.PLAY)
            self.playButton_toggled = False

    def changeSettingsValue(self, settingName, value):
        self.appConfig_obj_copy.readSettings[settingName] = value

    def saveSettings(self):
        self.appConfig_obj_copy.saveSettingsFile()
        self.parent.setCurrentStack(1)