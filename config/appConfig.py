import configparser

class AppConfig:
    #need to match settings.ini / createSettingsFile method
    basicSettings = [
        "timer",
        "pausetimer",
        "autorestart",
        "openonboot",
        "startonboot",
        "totaskbar",
        "volume"
    ]
    readSettings = {}
    settingsPath = "./pomov/config/settings.ini"
    

    def __init__(self) -> None:
        self.checkSettingsIntegrity()

    def checkSettingsIntegrity(self):
        configParser = configparser.ConfigParser()
        
        #file not found
        if len(configParser.read(self.settingsPath)) == 0:
            self.createSettingsFile()
            return 
        
        #settings header not found
        errorCase = False if configParser.sections()[0] == "Settings" else True
        if errorCase:
            self.createSettingsFile()
            return 

        #a specific setting not found
        for k in self.basicSettings:
            if k not in configParser["Settings"]:
                self.createSettingsFile()
                return 

        #user added a setting for some reason
        if len(self.basicSettings) != len(configParser["Settings"]):
            self.createSettingsFile()
            return 

        #save read in settings in dictionary
        for j in configParser["Settings"]:
            self.readSettings[j] = self.str_to_bool(configParser["Settings"][j])
        return

    def createSettingsFile(self):
        configParser = configparser.ConfigParser()
        configParser['Settings'] = {
            '#attention!\n'
            '#the program rewrites the settings if any errors were found\n'
            '#messing with this file might result in losing your customized settings to fallback standard settings.\n'
            '#only changes numeric values and boolean values, but keep the structure intact\n'
            '\n#time unit is in minutes\n'
            'timer': 60,
            '\n#time unit in minutes, how long you want to move yourself\n'
            'pausetimer': 5,
            '\n#defines if the timer should automatically start after the pause timer ran out or user input is needed\n'
            'autorestart': True,
            '\n#if this is true, the program will open as autostart\n'
            'openonboot': True,
            '\n#if this is true, the timer will start instantly on after booting pc\n'
            'startonboot': True,
            '\n#defines if the program should close to taskbar if pressed on x or be closed\n'
            'totaskbar': True,
            '\n#defines the volume of the sound\n'
            'volume': 50,
        }

        with open(self.settingsPath, 'w') as configfile:
            configParser.write(configfile)
        
        self.checkSettingsIntegrity()
        return
   
    def saveSettingsFile(self):
        configParser = configparser.ConfigParser()
        configParser['Settings'] = {
            '#attention!\n'
            '#the program rewrites the settings if any errors were found\n'
            '#messing with this file might result in losing your customized settings to fallback standard settings.\n'
            '#only changes numeric values and boolean values, but keep the structure intact\n'
            '\n#time unit is in minutes\n'
            'timer': self.readSettings["timer"],
            '\n#time unit in minutes, how long you want to move yourself\n'
            'pausetimer': self.readSettings["pausetimer"],
            '\n#defines if the timer should automatically start after the pause timer ran out or user input is needed\n'
            'autorestart': self.readSettings["autorestart"],
            '\n#if this is true, the program will open as autostart\n'
            'openonboot': self.readSettings["openonboot"],
            '\n#if this is true, the timer will start instantly on after booting pc\n'
            'startonboot': self.readSettings["startonboot"],
            '\n#defines if the program should close to taskbar if pressed on x or be closed\n'
            'totaskbar': self.readSettings["totaskbar"],
            '\n#defines the volume of the sound\n'
            'volume': self.readSettings["volume"],
        }

        with open(self.settingsPath, 'w') as configfile:
            configParser.write(configfile)

    def str_to_bool(self, s):
        if s == "True":
            return True
        elif s == "False":
            return False
        else:
            return s
