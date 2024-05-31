import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QValidator
from qfluentwidgets import *

class SettingsGui():
    settingsWidget = None

    def __init__(self, parent, appConfig_obj, titlebarGui_obj):
        self.parent = parent
        self.appConfig_obj_copy = appConfig_obj
        self.titlebarGui_obj_copy = titlebarGui_obj 

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
        self.timer_lineEdit = LineEdit()
        self.timer_lineEdit.setPlaceholderText("Minutes")
        self.timer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["timer"]))
        self.timer_lineEdit.textEdited.connect(lambda: self.changeSettingsValue("timer", self.timer_lineEdit.text()))

        #input validator
        self.timer_lineEdit.setValidator(ValidateTimer())

        timerRowWidget_layout.addWidget(timer_label)
        timerRowWidget_layout.addWidget(self.timer_lineEdit)
        return timerRowWidget
    
    def init_pauseTimer(self):
        #widget
        pauseTimerRowWidget = QWidget()
        pauseTimerRowWidget_layout = QHBoxLayout(pauseTimerRowWidget)
        
        #label
        pauseTimer_label = BodyLabel("Pause")
        
        #lineedit
        self.pauseTimer_lineEdit = LineEdit()
        self.pauseTimer_lineEdit.setPlaceholderText("Minutes")
        self.pauseTimer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["pausetimer"]))
        self.pauseTimer_lineEdit.textEdited.connect(lambda: self.changeSettingsValue("pausetimer", self.pauseTimer_lineEdit.text()))

        #input validator
        self.pauseTimer_lineEdit.setValidator(ValidatePauseTimer())

        pauseTimerRowWidget_layout.addWidget(pauseTimer_label)
        pauseTimerRowWidget_layout.addWidget(self.pauseTimer_lineEdit)
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
        print(self.appConfig_obj_copy.readSettings)
        if self.playButton_toggled == False:
            self.playToggleButton.setIcon(FluentIcon.PAUSE)
            self.playButton_toggled = True
        else:
            self.playToggleButton.setIcon(FluentIcon.PLAY)
            self.playButton_toggled = False

    def changeSettingsValue(self, settingName, value):
        if value != "":
            self.appConfig_obj_copy.readSettings[settingName] = value
            match settingName:
                case "timer":
                    self.appConfig_obj_copy.readSettings["timer_sec"] = int(value) * 60
                case "pausetimer":
                    self.appConfig_obj_copy.readSettings["pausetimer_sec"] = int(value) * 60                        
        else:
            match settingName:
                case "timer":
                    self.appConfig_obj_copy.readSettings[settingName] = 60
                    self.appConfig_obj_copy.readSettings["timer_sec"] = 60 * 60
                case "pausetimer":
                    self.appConfig_obj_copy.readSettings[settingName] = 5
                    self.appConfig_obj_copy.readSettings["pausetimer_sec"] = 5 * 60      

    def saveSettings(self):
        if self.timer_lineEdit.text() == "":
            self.timer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["timer"]))

        if self.pauseTimer_lineEdit.text() == "":
            self.pauseTimer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["pausetimer"]))  

        self.appConfig_obj_copy.saveSettingsFile()
        self.titlebarGui_obj_copy.settings_button_clicked(self.parent)


class ValidateTimer(QValidator):
    def validate(self, str , index):
        pattern = re.compile("^(?:[1-9]?[0-9]|1[01][0-9]|120)$")
        
        if str == "":
            return QValidator.State.Acceptable, str, index
        
        if pattern.fullmatch(str):
            return QValidator.State.Acceptable, str, index
        else:
            return QValidator.State.Invalid, str, index

class ValidatePauseTimer(QValidator):
    def validate(self, str , index):
        pattern = re.compile("^(?:[0-5]?[0-9]|60)$")
        
        if str == "":
            return QValidator.State.Acceptable, str, index
        
        if pattern.fullmatch(str):
            return QValidator.State.Acceptable, str, index
        else:
            return QValidator.State.Invalid, str, index