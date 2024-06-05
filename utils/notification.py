import random
from win11toast import toast


class Notification:

    appConfig_obj_copy = None

    notification_message = ["Hey, it's time to get up and stretch!",
        "Come on, take a break and move around!",
        "Get moving, a quick walk will do wonders!",
        "Time to stand up and shake off the cobwebs!",
        "Let's go, take a few steps and re-energize!",
        "Move it! A little exercise can boost your mood!",
        "Get up and stretch those legs!",
        "Come on, it's break time. Get active!",
        "Take a moment to walk around and refresh yourself!",
        "Up you go! A bit of movement will help clear your mind!"]

    def __init__(self, appConfig_obj):
        self.appConfig_obj_copy = appConfig_obj

    def show_notification(self):
        toast('Attention!', 
            self.notification_message[random.randint(0,len(self.notification_message)-1)],
            image=self.appConfig_obj_copy.get_random_gif_path(),
            audio=self.appConfig_obj_copy.get_selected_alarm(),
            app_id = "Pomov")

        