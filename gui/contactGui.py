import webbrowser
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from qfluentwidgets import *


class ContactGui():

    appGui_obj_copy = None


    def __init__(self, appGui_obj):

        self.appGui_obj_copy = appGui_obj

        #contact widget
        self.contactWidget = QWidget()
        self.contactWidget_layout = QVBoxLayout(self.contactWidget)

        self.contactWidget_layout.addWidget(self.init_logo())
        self.contactWidget_layout.addWidget(self.init_info())
        
    def init_logo(self):
        #logo widget
        self.logo_widget = QWidget()
        self.logo_widget.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        logo_widget_layout = QVBoxLayout(self.logo_widget)
        logo_widget_layout.setContentsMargins(0,0,0,0)
        
        self.image = ImageLabel("./media/img/logo/pomov_logo.png")
        self.image.scaledToWidth(self.appGui_obj_copy.width()-20)

        logo_widget_layout.insertSpacing(0, self.appGui_obj_copy.titleBar.height())
        logo_widget_layout.addWidget(self.image)
        return self.logo_widget
    
    def init_info(self):
        #info text
        self.info_widget = QWidget()
        info_widget_layout = QVBoxLayout(self.info_widget)

        #thank you text
        self.label_1 = SubtitleLabel()
        #i still dont understand where the margins / paddings come from, so fire at every existing possibility
        text = f'''
            <p style='margin: 0 0 0 0; padding: 0 0 0 0;'>Hey there!</p>
            <p style='margin: 0 0 0 0; padding: 0 0 0 0; font-size: 18px; font-weight: 500; text-decoration-thickness: 10px;'><u style='text-decoration-color: rgb(73,175,213);'>Thank you for using my app!</u></p>
            <p style='margin: 0 0 0 0; padding: 0 0 0 0; font-size: 18px; font-weight: 500;'>If you have any questions, please refer to the README file.</p>
            <p style='margin: 0 0 0 0; padding: 0 0 0 0; font-size: 18px; font-weight: 500;'>For reporting bugs or submitting feature requests, feel free to use the GitHub project below.</p>
        '''
        self.label_1.setText(text)
        self.label_1.setWordWrap(True)
        self.label_1.setMaximumWidth(self.appGui_obj_copy.width()-20)
        
        #github button
        button = PushButton(FluentIcon.GITHUB, "Pomov")
        button.clicked.connect(lambda: webbrowser.open('https://github.com/kfliemann/pomov'))

        #python libs text
        self.label_2 = SubtitleLabel()
        text = f'''
            <p style='margin: 0 0 0 0; padding: 0 0 0 0;'>Project made using:</p>
            <p style='margin: 0 0 0 0; padding: 0 0 0 0; font-size: 18px; font-weight: 500'>PyQt6, PyQt-Frameless-Window, PyQt-Fluent-Widgets, win11toast and Pygame</p>
        '''
        self.label_2.setText(text)
        self.label_2.setWordWrap(True)
        self.label_2.setMaximumWidth(self.appGui_obj_copy.width()-20)

        #credits
        dev_by = BodyLabel("<p style='font-weight: 600;'>developed by: kfliemann</p>")
        dev_by.setAlignment(Qt.AlignmentFlag.AlignBottom)

        info_widget_layout.addWidget(self.label_1)
        info_widget_layout.addWidget(button)
        info_widget_layout.insertSpacing(2, 40)
        info_widget_layout.addWidget(self.label_2)
        info_widget_layout.addWidget(dev_by)
        return self.info_widget

    def resize_logo(self, appGui_obj):
        #subtracting 20 was my first guess which seems to be working
        self.image.scaledToWidth(appGui_obj.width()-20)
        self.label_1.setMaximumWidth(self.appGui_obj_copy.width()-20)
        self.label_2.setMaximumWidth(self.appGui_obj_copy.width()-20)

