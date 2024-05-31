import time

class Timer():

    initial_timer = None
    initial_pausetimer = None

    def __init__(self, appConfig_obj):
        self.appConfig_obj_copy = appConfig_obj
        self.initial_time = self.appConfig_obj_copy.readSettings["timer"]
        self.initial_pausetimer = self.appConfig_obj_copy.readSettings["pausetimer"]