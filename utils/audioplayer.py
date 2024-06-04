import pygame
import threading


class Audioplayer:

    appConfig_obj_copy = None
    currently_playing = False
    

    def __init__(self, appConfig_obj):
        self.appConfig_obj_copy = appConfig_obj
        pygame.init()

        self.audioplayer_load_sound()

        self.audioplayer_thread = None
        self.stop_event = threading.Event()

    def audioplayer_start(self):
        self.stop_event.clear()
        self.sound.play(-1)
        self.currently_playing = True

        self.audioplayer_thread = threading.Thread(target=self.preview_audio_loop)
        self.audioplayer_thread.start()

    def preview_audio_loop(self):
        while not self.stop_event.is_set():
            self.sound.set_volume(int(self.appConfig_obj_copy.readSettings["volume"]) / 100)
            pygame.time.wait(10)

    def audioplayer_stop(self):
        self.stop_event.set()
        self.sound.stop()
        self.currently_playing = False
        if self.audioplayer_thread:
            self.audioplayer_thread.join()
    
    def audioplayer_load_sound(self):
        self.sound = pygame.mixer.Sound(self.appConfig_obj_copy.audioPath + self.appConfig_obj_copy.readSettings["alarmfile"])
        self.sound.set_volume(int(self.appConfig_obj_copy.readSettings["volume"]) / 100)

    def __del__(self):
        pygame.mixer.quit()

    def audioplayer_exit(self):
        self.audioplayer_stop()
        self.__del__()

