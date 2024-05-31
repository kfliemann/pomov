import sys
import gui.appGui as Gui
import config.appConfig as Config
from PyQt6.QtWidgets import QApplication


class App:

    def __init__(self):
        self.config = Config.AppConfig()
        self.gui = Gui.AppGui(self.config)


if __name__ == "__main__":
    window = QApplication(sys.argv)
    app = App()
    sys.exit(window.exec())