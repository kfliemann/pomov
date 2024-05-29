from .titlebarGui import titlebarGui
from qframelesswindow import FramelessMainWindow

class AppGui(FramelessMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.titlebarGui_obj = titlebarGui()
        self.titlebarGui_obj.init_settings_button(self.titleBar)
        self.show()

