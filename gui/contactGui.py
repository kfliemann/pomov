from utils.validator import ValidateTimer, ValidatePauseTimer
from utils.audioplayer import Audioplayer
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import *


class ContactGui():


    def __init__(self):

        self.contactWidget = QWidget()
        self.contactWidget_layout = QVBoxLayout(self.contactWidget)

        label = BodyLabel("Testlabel")
        label2 = BodyLabel("Testlabel 2")
        label3 = HyperlinkLabel(QUrl('https://github.com/kfliemann/pomov'), 'GitHub Project')

        image = ImageLabel("./pomov/media/img/icon/pomov_logo.png")

        # Scale proportionally to a specified height
        image.scaledToHeight(400)
        image.scaledToWidth(400)

        self.contactWidget_layout.addWidget(image)
        self.contactWidget_layout.addWidget(label)
        self.contactWidget_layout.addWidget(label2)
        self.contactWidget_layout.addWidget(label3)

