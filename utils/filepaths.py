import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SETTINGSINI_PATH = os.path.join(BASE_DIR, 'config', 'settings.ini')
APPICON_PATH = os.path.join(BASE_DIR, 'media', 'img', 'logo', 'pomov_icon.ico')
MOVEMENTGIF_PATH = os.path.join(BASE_DIR, 'media', 'img', 'movement_gif')
ICONOVERWRITE_PATH = os.path.join(BASE_DIR, 'media', 'img', 'icon')