from utils.validator import ValidateTimer, ValidatePauseTimer
from utils.audioplayer import Audioplayer
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from qfluentwidgets import *


class SettingsGui():

    appGui_obj_copy = None
    appConfig_obj_copy = None
    titlebarGui_obj_copy = None
    audioplayer_obj = None
    settingsWidget = None


    def __init__(self, appGui_obj, appConfig_obj, titlebarGui_obj):
        self.appGui_obj_copy = appGui_obj
        self.appConfig_obj_copy = appConfig_obj
        self.titlebarGui_obj_copy = titlebarGui_obj 
        self.audioplayer_obj = Audioplayer(self.appConfig_obj_copy)

        self.settingsWidget = QWidget()
        self.settingsWidget_layout = QVBoxLayout(self.settingsWidget)

        #setting elements
        self.settingsWidget_layout.addWidget(self.init_timer())
        self.settingsWidget_layout.addWidget(self.init_pauseTimer())
        self.settingsWidget_layout.addWidget(self.init_autorestart())
        self.settingsWidget_layout.addWidget(self.init_openonboot())
        self.settingsWidget_layout.addWidget(self.init_startonboot())
        self.settingsWidget_layout.addWidget(self.init_totaskbar())
        self.settingsWidget_layout.addWidget(self.init_audiopicker())
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
        autostartCheckbox = CheckBox("Restart Timer after Pause")
        autostartCheckbox.setChecked(self.appConfig_obj_copy.readSettings["autorestart"])
        autostartCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("autorestart", autostartCheckbox.isChecked()))
        return autostartCheckbox
    
    def init_openonboot(self):
        #checkbox
        openonbootCheckbox = CheckBox("Open app on PC Boot")
        openonbootCheckbox.setChecked(self.appConfig_obj_copy.readSettings["openonboot"])
        openonbootCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("openonboot", openonbootCheckbox.isChecked()))
        return openonbootCheckbox 
    
    def init_startonboot(self):
        #checkbox
        startonbootCheckbox = CheckBox("Start Timer on App opening")
        startonbootCheckbox.setChecked(self.appConfig_obj_copy.readSettings["startonboot"])
        startonbootCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("startonboot", startonbootCheckbox.isChecked()))
        return startonbootCheckbox
    
    def init_totaskbar(self):
        #checkbox
        totaskbarCheckbox = CheckBox("Minimize to System Tray")
        totaskbarCheckbox.setChecked(self.appConfig_obj_copy.readSettings["totaskbar"])
        totaskbarCheckbox.stateChanged.connect(lambda: self.changeSettingsValue("totaskbar", totaskbarCheckbox.isChecked()))
        return totaskbarCheckbox
    
    def init_audiopicker(self):
        #audio picker widget
        audiopickerRowWidget = QWidget()
        audiopickerRowWidget_layout = QHBoxLayout(audiopickerRowWidget)
        
        #audio combobox
        audiopickerCombobox = ComboBox()
        audiofiles_list = self.appConfig_obj_copy.get_alarm_paths()
        preselected_file = self.appConfig_obj_copy.readSettings["alarmfile"]
        for x in self.appConfig_obj_copy.get_alarm_paths():
            audiopickerCombobox.addItem(x.split(".")[0], userData=x)
        audiopickerCombobox.setCurrentIndex(audiofiles_list.index(preselected_file))
        audiopickerCombobox.currentIndexChanged.connect(lambda: self.changeSettingsValue("alarmfile", audiopickerCombobox.itemData(audiopickerCombobox.currentIndex())))

        #volume slider for alarm preview
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
        self.playToggleButton.clicked.connect(self.playToggleButton_clicked)
        
        audiopickerRowWidget_layout.addWidget(audiopickerCombobox)
        audiopickerRowWidget_layout.addWidget(volumeSlider)
        audiopickerRowWidget_layout.addWidget(self.timer_label)
        audiopickerRowWidget_layout.addWidget(self.playToggleButton)
        return audiopickerRowWidget
    
    def init_saveSettings(self):
        #button
        saveSettingsButton = PushButton(FluentIcon.SAVE, 'Save Settings')
        saveSettingsButton.clicked.connect(self.saveSettings)
        return saveSettingsButton
    
    def volume_changed(self, currentVol):
        self.timer_label.setText(str(currentVol))
        self.appConfig_obj_copy.readSettings["volume"] = currentVol
        
    def playToggleButton_clicked(self):
        if self.playButton_toggled == False:
            self.playToggleButton.setIcon(FluentIcon.PAUSE)
            self.playButton_toggled = True
            self.audioplayer_obj.audioplayer_start()
        else:
            self.playToggleButton.setIcon(FluentIcon.PLAY)
            self.playButton_toggled = False
            self.audioplayer_obj.audioplayer_stop()

    def playToggleButton_toggle(self):
        if self.playButton_toggled == False:
            self.playToggleButton.setIcon(FluentIcon.PAUSE)
            self.playButton_toggled = True
        else:
            self.playToggleButton.setIcon(FluentIcon.PLAY)
            self.playButton_toggled = False

    def changeSettingsValue(self, settingName, value):
        match settingName:
            case "timer":
                if value != "":
                    self.appConfig_obj_copy.readSettings[settingName] = int(value) 
                else:
                    self.appConfig_obj_copy.readSettings[settingName] = 60
            case "pausetimer":
                if value != "":
                    self.appConfig_obj_copy.readSettings[settingName] = int(value) 
                else:
                    self.appConfig_obj_copy.readSettings[settingName] = 5
            case "alarmfile":
                self.appConfig_obj_copy.readSettings[settingName] = value   
                if self.audioplayer_obj.currently_playing:
                    self.audioplayer_obj.audioplayer_stop()
                    self.audioplayer_obj.audioplayer_load_sound()  
                    self.audioplayer_obj.audioplayer_start()           
                else:              
                    self.audioplayer_obj.audioplayer_stop()
                    self.audioplayer_obj.audioplayer_load_sound()    

            case _:
                self.appConfig_obj_copy.readSettings[settingName] = value   

    def loadNewAudio(self):
        print("loading new audio")

    def saveSettings(self):
        if self.timer_lineEdit.text() == "":
            self.timer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["timer"]))

        if self.pauseTimer_lineEdit.text() == "":
            self.pauseTimer_lineEdit.setText(str(self.appConfig_obj_copy.readSettings["pausetimer"]))  

        self.appConfig_obj_copy.saveSettingsFile()
        self.appGui_obj_copy.timerGui_obj.timer_obj.timer_stop()
        self.appGui_obj_copy.timerGui_obj.reset_ui()
        self.titlebarGui_obj_copy.settings_button_clicked()

    def closeSettings(self):
        self.audioplayer_obj.audioplayer_stop()
        self.playToggleButton_toggle()
