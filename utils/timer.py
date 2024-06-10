import time
import threading
from utils.notification import Notification


class Timer():

    appConfig_obj_copy = None
    timerGui_obj_copy = None
    systemtrayGui_obj_copy = None
    notification_obj = None

    initial_timer = None
    initial_pausetimer = None
    current_timer = None
    current_pausetimer = None

    def __init__(self, timerGui, appConfig_obj, systemtrayGui_obj):
        self.appConfig_obj_copy = appConfig_obj
        self.timerGui_obj_copy = timerGui
        self.systemtrayGui_obj_copy = systemtrayGui_obj
        self.notification_obj = Notification(self.appConfig_obj_copy)

        self.timer_reset()

        self._timer_thread = None
        self._pause_event = threading.Event()
        self._stop_event = threading.Event()

    def timer_start(self):
        if self._timer_thread and self._timer_thread.is_alive():
            self.timer_resume()
            return
        
        self._stop_event.clear()
        self._pause_event.set()

        self._timer_thread = threading.Thread(target=self.timer_loop, args=("timer",))
        self._timer_thread.start()

    def timer_loop(self, timer_type):
        while not self._stop_event.is_set():
            match timer_type:
                case "timer":
                    self.timerGui_obj_copy.update_timerring("timer", self.initial_timer)
                    self.timerGui_obj_copy.update_timerring_range(self.initial_timer)
                    self.systemtrayGui_obj_copy.update_timer_label("timer", self.initial_timer)
                    
                    while self.current_timer > 0 and not self._stop_event.is_set():
                        self.current_timer -= 1
                        self.timer_sleep()
                        self.timerGui_obj_copy.update_timerring("timer", self.current_timer)
                        self.systemtrayGui_obj_copy.update_timer_label("timer", self.current_timer)

                    #time over
                    if not self._stop_event.is_set():
                        self.current_timer = self.initial_timer
                        self.notification_obj.show_notification()
                        timer_type= "pause"
                
                    
                case "pause":    
                    self.timerGui_obj_copy.update_timerring("pause", self.initial_pausetimer)
                    self.timerGui_obj_copy.update_timerring_range(self.initial_pausetimer)
                    self.systemtrayGui_obj_copy.update_timer_label("pause", self.initial_pausetimer)
                    
                    while self.current_pausetimer >= 0 and not self._stop_event.is_set():
                        self.systemtrayGui_obj_copy.update_timer_label("pause", self.current_pausetimer)
                        self.current_pausetimer -= 1
                        self.timer_sleep()
                        self.timerGui_obj_copy.update_timerring("pause", self.current_pausetimer)
                    
                    #time over
                    self.current_pausetimer = self.initial_pausetimer
                    self.systemtrayGui_obj_copy.update_timer_label("timer", self.initial_timer)
                    if self.appConfig_obj_copy.readSettings["autorestart"]:
                        timer_type= "timer"
                    else:
                        self.timerGui_obj_copy.reset_ui()
                        return
    
    def timer_sleep(self):
        for x in range(100):
            if self._stop_event.is_set():
                return
            time.sleep(0.01)
            self._pause_event.wait()

    def timer_pause(self):
        self._pause_event.clear()

    def timer_resume(self):
        self._pause_event.set()

    def timer_stop(self):
        self._stop_event.set()
        self._pause_event.set()
        if self._timer_thread:
            self._timer_thread.join()
        self.timer_reset()

    def timer_reset(self):
        #TODO: add * 60 to each line when done testing.
        self.initial_timer = self.current_timer = self.appConfig_obj_copy.readSettings["timer"] 
        self.initial_pausetimer = self.current_pausetimer = self.appConfig_obj_copy.readSettings["pausetimer"] 

    def timer_exit(self):
        if self._timer_thread:
            self._stop_event.set()
            self._pause_event.set()
            self._timer_thread.join()
            self._timer_thread = None
